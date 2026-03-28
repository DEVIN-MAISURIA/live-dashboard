import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE CONFIGimport streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Dashboard",
    layout="wide"
)

# ---------------- LIGHT THEME STYLE ----------------
st.markdown("""
    <style>
    .stApp {
        background-color: #F5F7FA;
    }
    .title {
        text-align: center;
        color: #2C3E50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #7F8C8D;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='title'>📊 Live Monitoring Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Real-time data visualization (Cloud Based)</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Value"])

# ---------------- METRIC LAYOUT ----------------
col1, col2, col3 = st.columns(3)

# ---------------- CHART ----------------
chart = st.line_chart(st.session_state.data.set_index("Time"))

# ---------------- LIVE LOOP ----------------
for i in range(1000):

    value = np.random.randint(50, 100)
    temp = np.random.randint(20, 40)
    pressure = np.random.randint(70, 120)

    # Store data
    new_data = pd.DataFrame({
        "Time": [i],
        "Value": [value]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_data],
        ignore_index=True
    )

    # ---------------- METRICS ----------------
    col1.metric("Load", value)
    col2.metric("Temperature (°C)", temp)
    col3.metric("Pressure", pressure)

    # ---------------- STATUS BAR ----------------
    if value > 90:
        st.error("🔴 Critical Load - Immediate Attention Required")
    elif value > 75:
        st.warning("🟡 High Load - Monitor System")
    else:
        st.success("🟢 System Stable")

    # ---------------- INSIGHT ----------------
    st.markdown("### System Insight")

    if value > 90:
        st.write("The system is experiencing excessive load. Risk of failure is high.")
    elif value > 75:
        st.write("Load is elevated. Continuous monitoring is recommended.")
    else:
        st.write("System is functioning within normal limits.")

    # ---------------- UPDATE GRAPH ----------------
    chart.add_rows(new_data.set_index("Time"))

    time.sleep(1) ----------------
st.set_page_config(
    page_title="Live Dashboard",
    layout="wide"
)

# ---------------- LIGHT THEME STYLE ----------------
st.markdown("""
    <style>
    .stApp {
        background-color: #F5F7FA;
    }
    .title {
        text-align: center;
        color: #2C3E50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #7F8C8D;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='title'>📊 Live Monitoring Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Real-time data visualization (Cloud Based)</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Value"])

# ---------------- METRIC LAYOUT ----------------
col1, col2, col3 = st.columns(3)

# ---------------- CHART ----------------
chart = st.line_chart(st.session_state.data.set_index("Time"))

# ---------------- LIVE LOOP ----------------
for i in range(1000):

    value = np.random.randint(50, 100)
    temp = np.random.randint(20, 40)
    pressure = np.random.randint(70, 120)

    # Store data
    new_data = pd.DataFrame({
        "Time": [i],
        "Value": [value]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_data],
        ignore_index=True
    )

    # ---------------- METRICS ----------------
    col1.metric("Load", value)
    col2.metric("Temperature (°C)", temp)
    col3.metric("Pressure", pressure)

    # ---------------- STATUS BAR ----------------
    if value > 90:
        st.error("🔴 Critical Load - Immediate Attention Required")
    elif value > 75:
        st.warning("🟡 High Load - Monitor System")
    else:
        st.success("🟢 System Stable")

    # ---------------- INSIGHT ----------------
    st.markdown("### System Insight")

    if value > 90:
        st.write("The system is experiencing excessive load. Risk of failure is high.")
    elif value > 75:
        st.write("Load is elevated. Continuous monitoring is recommended.")
    else:
        st.write("System is functioning within normal limits.")

    # ---------------- UPDATE GRAPH ----------------
    chart.add_rows(new_data.set_index("Time"))

    time.sleep(1)
