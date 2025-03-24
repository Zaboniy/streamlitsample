import streamlit as st
import numpy as np

st.file_uploader("Upload a CSV")

# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))