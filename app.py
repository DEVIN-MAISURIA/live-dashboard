import streamlit as st
import random

# -------------------- PAGE --------------------
st.set_page_config(page_title="Light Dashboard", layout="wide")

st.title("⚡ Live Dashboard")

# -------------------- SESSION DATA --------------------
if "value" not in st.session_state:
    st.session_state.value = 70

# -------------------- UPDATE VALUE --------------------
st.session_state.value = random.randint(50, 100)

# -------------------- METRICS --------------------
col1, col2, col3 = st.columns(3)

col1.metric("Load", st.session_state.value)
col2.metric("Temp", random.randint(20, 40))
col3.metric("Pressure", random.randint(70, 120))

st.markdown("---")

# -------------------- SIMPLE GRAPH --------------------
data = [random.randint(50, 100) for _ in range(20)]

st.line_chart(data)

# -------------------- STATUS --------------------
if st.session_state.value > 90:
    st.error("Critical")
elif st.session_state.value > 75:
    st.warning("High")
else:
    st.success("Stable")
