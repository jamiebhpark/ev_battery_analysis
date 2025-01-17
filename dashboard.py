import pandas as pd
import streamlit as st

# Streamlit 대시보드
st.title("EV Battery Analysis & BMS Simulation")

# 데이터 업로드
uploaded_file = st.file_uploader("Upload Battery Data CSV", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data.head())

    # SoC 시각화
    st.line_chart(data[['Voltage_measured', 'Current_measured', 'Temperature_measured']])
