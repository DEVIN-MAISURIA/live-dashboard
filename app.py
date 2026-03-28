import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Industrial Live Dashboard",
    layout="wide",
)

# ---------------- CUSTOM CSS (DARK UI) ----------------
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
    }
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    .metric-box {
        padding: 15px;
        border-radius: 10px;
        background: linear-gradient(145deg, #1f2630, #131720);
        box-shadow: 5px 5px 15px #0b0f14, -5px -5px 15px #1c2230;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center; color:#00E5FF;'>⚡ Industrial Smart Monitoring Dashboard</h1>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Value"])

# ---------------- LAYOUT ----------------
col1, col2, col3 = st.columns(3)

# ---------------- SIMULATION LOOP ----------------
chart = st.line_chart(st.session_state.data.set_index("Time"))

placeholder = st.empty()

for i in range(1000):
    value = np.random.randint(50, 100)
    temp = np.random.randint(20, 40)
    pressure = np.random.randint(60, 120)

    new_data = pd.DataFrame({
        "Time": [i],
        "Value": [value]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_data],
        ignore_index=True
    )

    # ---------------- METRICS ----------------
    with col1:
        st.metric("📊 Load", value)

    with col2:
        st.metric("🌡 Temperature (°C)", temp)

    with col3:
        st.metric("ضغط Pressure", pressure)

    # ---------------- ALERT LOGIC ----------------
    if value > 90:
        st.error("🚨 CRITICAL: System overload detected!")
        status = "CRITICAL"
    elif value > 75:
        st.warning("⚠️ WARNING: High load condition")
        status = "WARNING"
    else:
        st.success("✅ NORMAL: System stable")
        status = "NORMAL"

    # ---------------- AI-LIKE INSIGHT ----------------
    st.markdown("### 🧠 System Insight")

    if status == "CRITICAL":
        st.write("System is under extreme stress. Immediate action required to prevent failure.")
    elif status == "WARNING":
        st.write("Load is increasing. Monitor closely to avoid critical condition.")
    else:
        st.write("System is operating within safe parameters.")

    # ---------------- UPDATE CHART ----------------
    chart.add_rows(new_data.set_index("Time"))

    time.sleep(1)
