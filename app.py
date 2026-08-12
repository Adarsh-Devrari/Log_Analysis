import streamlit as st
from parser import read_logs, parse_log
from detector import count_log_levels

st.set_page_config(page_title="Log Analysis Dashboard", layout="wide")

st.title("🛡️ Log Analysis & SIEM Dashboard")

logs = read_logs("logs/sample.log")

parsed_logs = []

for log in logs:
    parsed_logs.append(parse_log(log))

counts = count_log_levels(parsed_logs)

st.header("Log Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("INFO", counts["INFO"])
col2.metric("WARNING", counts["WARNING"])
col3.metric("ERROR", counts["ERROR"])
import pandas as pd

st.header("Parsed Logs")

df = pd.DataFrame(parsed_logs)

st.dataframe(df, use_container_width=True)
import pandas as pd

chart_data = pd.DataFrame({
    "Level": ["INFO", "WARNING", "ERROR"],
    "Count": [
        counts["INFO"],
        counts["WARNING"],
        counts["ERROR"]
    ]
})
st.subheader("Log Level Distribution")

st.bar_chart(
    chart_data,
    x="Level",
    y="Count"
)
left, right = st.columns([1, 2])

with left:
    st.subheader("Log Level Distribution")
    st.bar_chart(
        chart_data,
        x="Level",
        y="Count"
    )

with right:
    st.subheader("Parsed Logs")
    df = pd.DataFrame(parsed_logs)
    st.dataframe(df, use_container_width=True)