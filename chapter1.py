import streamlit as st

st.title("i am the title")
st.subheader("i am subheader")
st.text("i am inner text")

job=st.selectbox("Select job title:",["Data Analyst","QA","SDE 1","SDE 2","Data science"])

st.write(f"i am interested for the job of : {job}")

st.success("Selected job profile sent to secruiter")