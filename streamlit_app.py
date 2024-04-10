import pandas as pd
import numpy as np
import streamlit as st

st.title("Chào mừng bạn đến với trang chủ")
st.header("Mời bạn nhập dữ liệu tại đây")

ten = st.text_input("Nhập tên của bạn:")
st.text_input("Nhập dữ liệu:")
tep = st.file_uploader("Chọn file")

