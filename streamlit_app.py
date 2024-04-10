import pandas as pd
import numpy as np
import streamlit as st

st.title("Mời bạn nhập dữ liệu")
st.header("Tên công ty")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

