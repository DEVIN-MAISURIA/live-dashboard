import streamlit as st
import pandas as pd
import numpy as np

# Page setup
st.set_page_config(page_title="Live Dashboard", layout="wide")

st.title("📊 Live Monitoring Dashboard")

# Auto refresh every 1 second
st.autorefresh(interval=1000, key="refresh")

# Generate live values
value = np.random.randint(50, 100)
temp = np.random.randint(20, 40)
pressure = np.random.randint(70, 120)

# Ribbon (metrics)
col1, col2, col3 = st.columns(3)
col1.metric("Load", value)
col2.metric("Temperature (°C)", temp)
col3.metric("Pressure", pressure)

st.markdown("---")

# Fixed-size data (no scrolling)
x = list(range(20))
y = np.random.randint(50, 100, size=20)

df = pd.DataFrame({"x": x, "y": y})

# Graph updates in same place
st.line_chart(df.set_index("x"))

# Status message
if value > 90:
    st.error("🔴 Critical Condition")
elif value > 75:
    st.warning("🟡 High Load")
else:
    st.success("🟢 System Stable")
