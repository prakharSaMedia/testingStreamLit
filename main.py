import streamlit as st

st.title("My First Streamlit App")

# Add a text input
user_input = st.text_input("Enter your name:", "")

# Add a button
if st.button("Say Hello"):
    if user_input:
        st.write(f"Hello, {user_input}! 👋")
    else:
        st.write("Please enter your name above! 😊")

# Add a slider
number = st.slider("Pick a number", 0, 100)
st.write(f"Your number squared is: {number * number}")

# Add a sidebar element
st.sidebar.header("About")
st.sidebar.write("This is a simple Streamlit demo app!")
