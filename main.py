import streamlit as st
from datetime import date
from datetime import datetime

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to :blue[_HowLongAgo_]")
st.header("Calculate days between two dates easily")

default = date(2000,1,1)


try:
    first_date = st.date_input("Enter the starting date in format ( YYYY-MM-DD ): ", value=default,  max_value=date.today())
    # first_date = datetime.strptime(first_date, "%Y-%m-%d")
    
except ValueError:
    print("❌ Invalid format! Please use YYYY-MM-DD.\n")

try:
    second_date = st.date_input("Enter the ending date in format ( YYYY-MM-DD ): ", max_value=date.today())
    # second_date = datetime.strptime(second_date, "%Y-%m-%d")

except ValueError:
    print("❌ Invalid format! Please use YYYY-MM-DD.\n")

days_passed = (second_date - first_date)

choice = st.radio("Do you also want to know minutes and seconds?", ["No", "Yes"])

if st.button("Calculate"):
    if second_date < first_date:
        print("\n⚠️ Ending date is before the starting date!")

    else:
        st.write(f"\n{days_passed.days} days have been passed between {first_date} and {second_date}")
        if choice == "Yes":
            total_seconds = days_passed.total_seconds()
            total_minutes = total_seconds // 60
            st.info(f"That's approximately {int(total_minutes):,} minutes or {int(total_seconds):,} seconds.")