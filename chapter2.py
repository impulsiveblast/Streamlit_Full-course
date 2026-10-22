import streamlit as st

st.title("Job Application")

button=st.button("Submit")

if button:
  st.success("Application sucessfully submitted")


job=st.checkbox("I have completed my graduation in cse/it")



job_dis=st.radio("Job title :",["QA","SDE 1","SDE 2","Data Analyst","Data Scientist"])

st.write(f"{job_dis} selected as the job discription to apply") 

if job:
  st.write("Eligible to apply")


move=st.slider("Years of Experience: ",0,2,4)

st.number_input("Enter you age: ",min_value=1,max_value=10,step=1)

st.text_input("Graduation college: ")

st.date_input("Today's date?")