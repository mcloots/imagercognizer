import streamlit as st

st.title("Project Discovery Week")
st.header("This is my very first app")
st.write("Hello world")
st.text("This is a text")
st.markdown("_Markdown_ is als possible")
st.code("for i in range(8): dosomething")
image = st.camera_input("Take a picture")

if image:
    st.image(image, caption="Gemaakte foto", use_column_width=True)