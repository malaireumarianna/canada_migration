'''import plotly.express as px
import streamlit as st

data_frame = {'India': 4500,
              'Australia': 2500,
              'Japan': 1053,
              'America': 500
 }

fig = px.pie(
    hole = 0.2,
    labels = data_frame.values(),
    names = data_frame.keys(),
)
st.header("Donut chart")
st.plotly_chart(fig)'''


import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_dynamic_filters import DynamicFilters

data = pd.read_csv('Canada.csv')
map_data = pd.read_csv('world_country_and_usa_states_latitude_and_longitude_values.csv')

data.drop(columns = data.iloc[:,-8:].columns.tolist(), inplace=True)
data.drop(index = data.loc[data['AREA']==999].index.tolist(), inplace=True)

melted_df = data.melt(id_vars=['Type', 'Coverage', 'OdName','AREA', 'AreaName', 'REG', 'RegName','DEV','DevName'], var_name='Year', value_name='Value')
melted_df = melted_df.merge(map_data, left_on='OdName', right_on='country')

print(melted_df[['OdName', 'country']])

melted_df.to_csv('C:/Users/Marianna/PycharmProjects/example_stream/melted.csv')
