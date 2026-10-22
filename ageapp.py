import streamlit as st
from datetime import date

today = date.today()

dob = st.date_input(
    "Enter your DOB",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),    # earliest selectable date
    max_value=today                # latest selectable date (today, in 2026)
)

if st.button("Calculate age"):
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1

    if months < 0:
        years -= 1
        months += 12

    st.success(f"Your age is {years} years and {months} months")