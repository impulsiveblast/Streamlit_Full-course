import streamlit as st

a,b,c=st.columns(3)

with a:
  st.write("sl. no")


with b:
  st.write("Name :")

with c:
  st.write("Age :")    

  
with a:
    st.write("1")

with b:
    st.write("Brahamjeet")
    vote_1=st.button("candidate 1")

with c:
    st.write("24")


with a:
    st.write("2")

with b:
    st.write("Rahul")
    vote_2=st.button("candidate 2")

with c:
    st.write("25")


with a:
    st.write("3")

with b:
    st.write("Aman")
    vote_3=st.button("candidate 3")

with c:
    st.write("23")


with a:
    st.write("4")

with b:
    st.write("Priya")
    vote_4=st.button("candidate 4")
with c:
    st.write("22")




if vote_1:
    st.success("Brahamjeet won!")
elif vote_2:
    st.success("Rahul won")
elif vote_3:
    st.success("Aman won")
elif vote_4:
    st.success("Priya won")
