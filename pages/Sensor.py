import os.path as path
import pandas as pd
import streamlit as st
from bokeh import plotting as plt


st.title(path.splitext(path.basename(__file__))[0])

log_file = st.file_uploader("choose a log file")

if log_file is not None:
    data = pd.read_csv(log_file, header=None)

    st.dataframe(data=data, use_container_width=True)

    ts_idx = st.selectbox("choose column index of timestamp", data.columns)
    y_idx = st.selectbox("choose column index of y-axis", data.columns)

    if ts_idx is not None and y_idx is not None:
        begin_idx, end_idx = st.select_slider("choose plot range", options=range(len(data.index)), format_func=lambda idx: data.iat[idx, ts_idx], value=(0, len(data.index) - 1))

        fig = plt.figure()
        fig.line(x=data.index[begin_idx:end_idx + 1], y=data.iloc[begin_idx:end_idx + 1, y_idx])
        st.bokeh_chart(fig, use_container_width=True)
