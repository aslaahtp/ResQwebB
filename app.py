import imp
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt

df = pd.read_csv("district_wise_details.csv")

# Display the DataFrame
# st.write("DataFrame from Uploaded CSV:")
# st.write(df)

# Plot the data
# fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size
# ax.plot(df.iloc[:, 0], df.iloc[:, 1])  # Plot column 0 on x-axis and column 1 on y-axis
# ax.set_xlabel("Districts")  # Set x-axis label
# ax.set_ylabel("Fatalities")  # Set y-axis label
# ax.set_title("Districts vs Fatalities")  # Set plot title
# ax.grid(True)  # Enable grid
# st.pyplot(fig)  # Display the plot in Streamlit
def load_data():
    return pd.read_csv("district_wise_details.csv")  # Replace "keralafloods2018_dataset.csv" with your dataset path

data = load_data()
selected_districts = st.multiselect("Select Districts", data["district"].unique())

# Select a single attribute for comparison
selected_attribute = st.selectbox("Select Attribute", ["fatalities", "no_of_camps", "actual_rainfall_in_mm", "normal_rainfall_in_mm", "no_of_landslides", "full_damaged_houses"])

# Filter the dataset based on the selected districts
district_data = data[data["district"].isin(selected_districts)]

# Plot the selected attribute for each district
fig, ax = plt.subplots(figsize=(10, 6))
for district in selected_districts:
    district_subset = district_data[district_data["district"] == district]
    ax.bar(district_subset.index, district_subset[selected_attribute], label=district)

# Customize the plot
ax.set_xlabel("Index")
ax.set_ylabel(selected_attribute.capitalize())
ax.set_title(f"{selected_attribute.capitalize()} Comparison")
ax.legend()

# Display the plot
st.pyplot(fig)
#BREAK#

st.header('3D Visualization on EarthQuake')

#a=st.pydeck_chart
#b=

data=pd.read_csv('Indian_earthquake_data.csv')

#layers setting
layers=pdk.Layer('HexagonLayer',
    data,
    get_position=['Longitude', 'Latitude'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,                 
    coverage=1)

#view Port Location
view_state=pdk.ViewState(longitude=78.348516,
    latitude=22.824289,
    zoom=6,
    min_zoom=1,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

# Render
r = pdk.Deck(layers=[layers], initial_view_state=view_state)
st.write(r)


