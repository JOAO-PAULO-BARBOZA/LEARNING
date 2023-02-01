# Necessary importations

import streamlit as st
import pandas as pd
import plotly.express as px
import folium as fl
from haversine import haversine

# Data uploading

df = pd.read_csv('train.csv')

# Cleaning the datas

df2 = df.copy()
df2 = df2[df2['Delivery_person_Age'] != 'NaN ']
df2 = df2[df2['City'] != 'NaN ']
df2 = df2[df2['multiple_deliveries'] != 'NaN ']
df2 = df2[df2['Road_traffic_density'] != 'NaN ']
df2 = df2[df2['Festival'] != 'NaN ']

df2['ID'] = df2['ID'].str.strip() # It's needed to call the method 'str' before the 'strip'
df2['Road_traffic_density'] = df2['Road_traffic_density'].str.strip()
df2['Type_of_order'] = df2['Type_of_order'].str.strip()
df2['Type_of_vehicle'] = df2['Type_of_vehicle'].str.strip()
df2['City'] = df2['City'].str.strip()

#============================================================
#                STREAMLIT SIDERBAR        
#===========================================================

st.header('Marketplace - Customer View') 















