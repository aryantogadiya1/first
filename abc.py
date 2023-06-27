import streamlit as st
import pandas as pd
st.write("# hello")
a = pd.DataFrame({
    'first': [1, 2, 3, 4],
    'second': [10, 20, 30, 40],
})
st.write(a)
