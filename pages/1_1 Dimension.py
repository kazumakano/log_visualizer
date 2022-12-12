import os.path as path
import streamlit as st
import script.common as common


st.title(path.splitext(path.basename(__file__))[0][2:])

log_file = common.file_uploader()

if log_file is not None:
    data = common.read_csv(log_file)

    common.dataframe(data)

    ts_idx = common.idx_selectbox(0, "timestamp", len(data.columns))
    y_idx = common.idx_selectbox(1, "y-axis", len(data.columns))

    begin_idx, end_idx = common.range_select_slider(data, ts_idx)

    fig = common.line_chart(data.index[begin_idx:end_idx + 1], data.iloc[begin_idx:end_idx + 1, y_idx], "timestamp", "y")
