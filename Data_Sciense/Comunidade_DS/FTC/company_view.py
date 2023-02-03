# Necessary importations

import streamlit as st
import pandas as pd
import plotly.express as px
import folium as fl
from streamlit_folium import folium_static
from haversine import haversine
from PIL import Image
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
df2['Delivery_person_Age'] = df2['Delivery_person_Age'].astype(int)
df2['Delivery_person_Ratings'] = df2['Delivery_person_Ratings'].astype(float)
df2['Order_Date'] = pd.to_datetime(df2['Order_Date'], format="%d-%m-%Y")
df2['multiple_deliveries'] = df2['multiple_deliveries'].astype(int)
df2['Road_traffic_density'] = df2['Road_traffic_density'].str.strip()
df2['Type_of_order'] = df2['Type_of_order'].str.strip()
df2['Type_of_vehicle'] = df2['Type_of_vehicle'].str.strip()
df2['City'] = df2['City'].str.strip()

#============================================================
#                STREAMLIT SIDEBAR  
#===========================================================

# Image loading

img = Image.open('fast-time.png') # 'Image' was imported from PIL lib.
st.sidebar.image(img, width=120)
#--------------------------------------------------------------------

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown('''___''')

# Filter

date_slider = st.sidebar.slider(
    'Date limit',
    value=pd.datetime(2022, 4, 13),
    min_value=pd.datetime(2022, 2, 11),
    max_value=pd.datetime(2022, 4, 6),
    format='DD-MM-YYYY'
 )

st.sidebar.markdown('''___''')

traffic_opt = st.sidebar.multiselect(
        'Traffic Conditions',
        ['Low', 'Medium', 'High', 'Jam'],
    default=['Low', 'Medium', 'High', 'Jam']
)

selected_lines = df2[df2['Order_Date'] < date_slider]

df2 = selected_lines

selected_lines = df2[df2['Road_traffic_density'].isin(traffic_opt)]
df2 = selected_lines 


#---------------------------------------------------------------------------

st.sidebar.markdown('''___''')
st.sidebar.markdown('###### Powered by J. Paulo B. Barboza')

st.header('Marketplace - Customer View') 

#============================================================================================
#                STREAMLIT LAYOUT  
#===========================================================================================

# Creating the tables

managerial_view, tactical_view, geographical_view = st.tabs(['Managerial View', 'Tactical View', 'Geographical View'])


# Order quantity per day.

with managerial_view:
    
    with st.container():        
    
        #Line selection     
        df_aux = df2.loc[:, ['ID', 'Order_Date']].groupby('Order_Date').count().reset_index()
    
        #drawing the graphic
        fig = px.bar(df_aux, x='Order_Date', y='ID')

        st.plotly_chart(fig, use_container_width=True)
    with st.container():
        col01, col02 = st.columns(2)

        with col01:
    
            # Order distribution by type of traffic
            df_aux = df2[['ID', 'Road_traffic_density']].groupby('Road_traffic_density').count().reset_index()
            df_aux['percentage'] = df_aux['ID']/df_aux['ID'].sum()
            #drawing the graphic
            fig = px.pie(df_aux, values='percentage', names='Road_traffic_density')
            st.plotly_chart(fig, use_container_width=True)

        with col02:
            
            # Order's volume Comparison by city and type of traffic
            df_aux = (df2[['ID', 'City', 'Road_traffic_density']]
                    .groupby(['City', 'Road_traffic_density'])
                    .count()
                    .reset_index())
            
            #drawing the graphic
            fig = px.scatter(df_aux, x='City', y='Road_traffic_density', size='ID', color='City')
            st.plotly_chart(fig, use_container_width=True)            

with tactical_view:
     
    with st.container():

        # Order quantity per Week.
        df2['week_of_year'] = df2['Order_Date'].dt.strftime('%U') #('%U') The counting of the days start from sunday
        df_aux = df2[['ID', 'week_of_year']].groupby('week_of_year').count().reset_index()
        px.line(df_aux, x='week_of_year', y='ID')
        
        #drawing the graphic
        fig = px.line(df_aux, x='week_of_year', y='ID')
        st.plotly_chart(fig, use_container_width=True)
    
    with st.container():
        
        # Grouping the quantity of orders by week of year
        df_aux01 = df2[['ID', 'week_of_year']].groupby('week_of_year').count().reset_index()
        
        # Grouping the quantity of orders by unique id of delivery person
        df_aux02 = df2[['Delivery_person_ID', 'week_of_year']].groupby('week_of_year').nunique().reset_index()
        
        # merging both dataframes
        df_aux = pd.merge(df_aux01, df_aux02, how='inner')
        
        # Quantity of delivery by each delivery person in a certain week of the year = qd_bydp_week
        df_aux['qd_bydp_week'] = df_aux['ID']/df_aux['Delivery_person_ID']

        #drawing the graphic
        fig = px.line(df_aux, x='week_of_year', y='qd_bydp_week')
        st.plotly_chart(fig, use_container_width=True)




with geographical_view:    
    
    # The central location of each city by type of traffic
    df_aux = (df2[['City', 'Road_traffic_density', 'Delivery_location_latitude', 'Delivery_location_longitude']]
            .groupby(['City', 'Road_traffic_density'])
            .median()
            .reset_index())

    #drawing the graphic
    _map = fl.Map()

    for index, location in df_aux.iterrows():
        fl.Marker([location['Delivery_location_latitude'], 
                location['Delivery_location_longitude']]).add_to(_map)
    folium_static(_map, width=1024, height=600)









