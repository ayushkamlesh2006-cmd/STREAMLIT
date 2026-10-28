
import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write(":streamlit: This is my first Streamlit app")
st.text("Let's get started")

# Conditional logic with widgets
name = st.text_input("Enter your name")

if st.button("Greet"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name.")

# Displaying data and charts
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["A", "B"]
)

st.line_chart(df)
st.bar_chart(df)

# File uploading and displaying data
upload_file = st.file_uploader("Upload a CSV file", type="csv")

if upload_file is not None:
    df_uploaded = pd.read_csv(upload_file)
    st.dataframe(df_uploaded)

# Text and Markdown demo
st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5):\n    print(i)", language="python")

# Input widgets
st.text_input("What is your name?")
st.text_area("What is your address?")
st.number_input(
    "Enter a number",
    min_value=0,
    max_value=100,
    value=50,
    step=5
)
st.slider(
    "Select a range of values",
    min_value=0,
    max_value=100,
    value=(25, 75),
    step=5
)
st.selectbox("Select a fruit", options=["apple", "banana", "orange"])
st.multiselect("Select multiple fruits", options=["apple", "banana", "orange"])
st.radio("Select a gender", options=["male", "female", "other"])
st.checkbox("I agree to the terms and conditions")

if st.checkbox("Show details"):
    st.write("Here are the details!")
st.info("here are more details")

option=st.radio("Choose view", ["Show Chart","Show Table"])
if option == "show chart":
    st.write("Chart Would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username= st.text_input("username")
    password = st.text_input("password", type = "password")
    submmitted = st.form_submit_button ("login")

    if submitted:
        st.success(f"welcome, {username}!")

st.image(
    "https://via.placeholder.com/300",
    caption="Sample Image",
    use_container_width=True
)

st.video("https://www.youtube.com/watch?v=VqgUkEPvLY")
         