import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Live Dashboard", layout="wide")

st.title("🌐 Live Internet Dashboard (No Sensor)")

# Initialize data storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Value"])

# Create chart
chart = st.line_chart(st.session_state.data.set_index("Time"))

# Simulate live data
placeholder = st.empty()

for i in range(1000):
    new_value = np.random.randint(50, 100)

    new_data = pd.DataFrame({
        "Time": [i],
        "Value": [new_value]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_data],
        ignore_index=True
    )

    chart.add_rows(new_data.set_index("Time"))

    placeholder.metric("Current Value", new_value)

    time.sleep(1)