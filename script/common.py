from typing import Any, Optional
import pandas as pd
import streamlit as st
from bokeh import plotting as plt
from bokeh.models import ColumnDataSource
from streamlit.runtime.uploaded_file_manager import UploadedFile


def dataframe(data: pd.DataFrame) -> None:
    st.dataframe(data=data, use_container_width=True)

def line_chart(ts: Any, x: Any, y: Any, x_label: str, y_label: str, **fig_kwargs: Any) -> None:
    fig = plt.figure(active_scroll="wheel_zoom", tools="pan,wheel_zoom,box_zoom,save,reset", tooltips=[("ts", "@ts"), ("(x, y)", "(@x, @y)")], x_axis_label=x_label, y_axis_label=y_label, **fig_kwargs)
    fig.line(source=ColumnDataSource({
        "ts": ts,
        "x": x,
        "y": y,
    }), x="x", y="y")
    st.bokeh_chart(fig, use_container_width=True)

def file_uploader() -> Optional[UploadedFile]:
    return st.file_uploader("choose a log file")

def idx_selectbox(default_idx: int, name: str, row_len: int) -> int:
    return st.selectbox(f"choose column index of {name}", range(row_len), index=default_idx)

def range_select_slider(data: pd.DataFrame, ts_idx: int) -> tuple[int, int]:
    return st.select_slider("choose plot range", options=range(len(data.index)), format_func=lambda idx: data.iat[idx, ts_idx], value=(0, len(data.index) - 1))

def read_csv(file: UploadedFile) -> pd.DataFrame:
    return pd.read_csv(file, header=None)
