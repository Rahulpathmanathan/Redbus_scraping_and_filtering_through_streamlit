import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime

st.title('Redbus Booking') 

def get_data_from_db(query):
    # Creating connection
    MYDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="redbus"
    )
    try:
        cursor = MYDB.cursor()
        df = pd.read_sql(query, MYDB) # Sql to pandas conversion
        MYDB.commit()
        
    finally:
        MYDB.close()
    return df


query = "SELECT * FROM busdetails" # Select query to import data
dfs = get_data_from_db(query) 

route = dfs["Route_name"].unique()


time_ranges = {
    "Morning (6:00 to 12:00)": ("06:00:00", "12:00:00"),
    "Afternoon (12:00 to 18:00) ": ("12:00:00", "18:00:00"),
    "Evening (18:00 to 24:00 )": ("18:00:00", "24:00:00"),
    "Night (00:00 to 06:00)" : ("00:00:00","06:00:00")
}

with st.form("my_form"): # using Streamlit form method to build search engine
    st.write('Bus Details')
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_route = st.selectbox("Route", route)
        Min_price = st.text_input("starts from")
        Max_price = st.text_input("upto")

    with col2:
        bus_type = st.selectbox("Bus Type",("sleeper", "seater"))
        selected_rating = st.slider("Star Rating", 0.0, 5.0)
        selected_time_range = st.selectbox("Time of Day", list(time_ranges.keys()))
        start_time, end_time = time_ranges[selected_time_range]   
        
    submitted = st.form_submit_button("Search")


if submitted:
    query = f"""
    SELECT * FROM busdetails
    WHERE Route_name = '{selected_route}'
    AND price BETWEEN '{Min_price}' AND '{Max_price}' 
    AND bustype LIKE '%{bus_type}%' AND star_rating >= {selected_rating} 
    AND departing_time between '{start_time}' AND '{end_time}' """

    dfs = get_data_from_db(query) 
    dfs['departing_time'] = dfs['departing_time'].astype(str).apply(lambda x: x.split()[-1]) # converting timedelta to str
    dfs['reaching_time'] = dfs['reaching_time'].astype(str).apply(lambda x: x.split()[-1])
    st.dataframe(dfs) #to print output as Dataframe
       
        

    
         


