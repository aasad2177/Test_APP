import pandas as pd
import plotly.graph_objects as go  
import streamlit as st
import openpyxl

st.header('GW2')

# Read Excel file
df = pd.read_excel("datasheet.xlsx")

# Create figure
fig = go.Figure()

# Add area chart (cogent_l4)
fig.add_trace(go.Scatter(
    x=df["Time"],
    y=df["cogent_l3"],
    fill='tozeroy', 
    mode='none',     
    name="cogent_l3",
    fillcolor='#17becf'  
))

# Add line chart (cogent_l2)
fig.add_trace(go.Scatter(
    x=df["Time"],
    y=df["cogent_l2"],
    mode='lines', 
    name="cogent_l2",
    line=dict(color='red', width=2) 
))

# Update layout
fig.update_layout(
    title="Test",
    xaxis_title="Time",
    yaxis_title="Values",
    template="plotly_white"
)

# Display dataframe
st.write(df)

# Display chart
st.plotly_chart(fig)

    


