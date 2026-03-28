import streamlit as st
import pandas as pd
import numpy as np
from streamlit_autorefresh import st_autorefresh

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Advanced Live Dashboard", layout="wide")

# -------------------- AUTO REFRESH --------------------
st_autorefresh(interval=1000, key="live")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
}
.metric-title {
    font-size: 18px;
    color: #aaa;
}
.metric-value {
    font-size: 35px;
    font-weight: bold;
    color: #00ffcc;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown("<h1 style='text-align:center; color:#00ffcc;'>⚡ Live System Dashboard</h1>", unsafe_allow_html=True)

# -------------------- SESSION STATE (IMPORTANT) --------------------
if "data" not in st.session_state:
    st.session_state.data = np.random.randint(50, 100, 20).tolist()

# Generate new value
new_value = np.random.randint(50, 100)

# Keep fixed length (NO SCROLL)
st.session_state.data.pop(0)
st.session_state.data.append(new_value)

# -------------------- METRICS (RIBBON STYLE) --------------------
col1, col2, col3 = st.columns(3)

def metric_card(title, value, color):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color:{color}">{value}</div>
    </div>
    """, unsafe_allow_html=True)

with col1:
    metric_card("Load", new_value, "#00ffcc")

with col2:
    metric_card("Temperature (°C)", np.random.randint(20, 40), "#ffcc00")

with col3:
    metric_card("Pressure", np.random.randint(70, 120), "#ff4d4d")

st.markdown("---")

# -------------------- GRAPH (NO SCROLL, FIXED WINDOW) --------------------
chart_placeholder = st.empty()

df = pd.DataFrame({
    "Time": list(range(len(st.session_state.data))),
    "Load": st.session_state.data
})

chart_placeholder.line_chart(df.set_index("Time"))

# -------------------- STATUS --------------------
if new_value > 90:
    st.error("🔴 Critical Condition")
elif new_value > 75:
    st.warning("🟡 High Load")
else:
    st.success("🟢 System Stable")
