# Redbus_scraping_and_filtering_through_streamlit

Project Statement:

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to collect, analyze, and visualizing bus travel data.

My workflow :

By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability.

By using SQL connector pushing the data into my local sql server.

By using streamlit will visualise the data collected by importing it from my local SQL server and create a search engine to visualise data.

This project can significantly improve operational efficiency and strategic planning in the transportation industry.

Features :

Automated Web Scraping: Collect detailed bus travel data including routes, schedules, prices, and seat availability from the Redbus website.
Data Analysis: Analyze the scraped data to extract meaningful insights and trends.
Data Filtering: Filter the data based on various criteria such as route, price, departure time,seats availability, rating, reaching time

Tools:

Python, Selenium(Web scraping), Mysql, Streamlit (Visualisation) , Pandas(Library), DateTime(Library)

Approach

Python: The primary programming language used for scripting and data processing.
Selenium: A web automation tool used for scraping websites and gathering data.
Streamlit: A framework for building interactive web applications.
Pandas: A library for data manipulation and analysis.
MySQL: A database system for storing scraped data and integrating it with Streamlit's filtering processes.
Regular Expressions (re): A module used for string operations and data cleaning.

Findings

Accumulating a substantial amount of data, which will be valuable for future critical and competitive analysis

Prerequesting Libraries

import streamlit as st
import mysql.connector
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


