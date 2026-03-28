import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Live Dashboard", layout="wide")

st.title("📊 Live Monitoring Dashboard")

# Refresh every 1 second
st.experimental_autorefresh(interval=1000, key="refresh")

# Generate fresh data (replaces old)
value = np.random.randint(50, 100)
temp = np.random.randint(20, 40)
pressure = np.random.randint(70, 120)

# Metrics (Ribbon style)
col1, col2, col3 = st.columns(3)

col1.metric("Load", value)
col2.metric("Temperature (°C)", temp)
col3.metric("Pressure", pressure)

st.markdown("---")

# Fixed graph (no scrolling, updates in place)
x = np.arange(20)
y = np.random.randint(50, 100, size=20)

df = pd.DataFrame({"x": x, "y": y})

st.line_chart(df.set_index("x"))

# Status
if value > 90:
    st.error("🔴 Critical Condition")
elif value > 75:
    st.warning("🟡 High Load")
else:
    st.success("🟢 System Stable")
