import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Live Dashboard", layout="wide")

st.title("📊 Live Monitoring Dashboard")

# Store data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Value"])

col1, col2, col3 = st.columns(3)

chart = st.line_chart(st.session_state.data.set_index("Time"))

i = 0
while True:
    value = np.random.randint(50, 100)
    temp = np.random.randint(20, 40)
    pressure = np.random.randint(70, 120)

    new_data = pd.DataFrame({"Time": [i], "Value": [value]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

    col1.metric("Load", value)
    col2.metric("Temp (°C)", temp)
    col3.metric("Pressure", pressure)

    if value > 90:
        st.error("🔴 Critical")
    elif value > 75:
        st.warning("🟡 Warning")
    else:
        st.success("🟢 Normal")

    chart.add_rows(new_data.set_index("Time"))

    i += 1
    time.sleep(1)
