import streamlit as st
import datetime

time_off = st.text_input("Enter time for alarm to go off:" )
if st.button("Save"):
    st.info("Alarm going off at: " + time_off)

    while True:
        if datetime.datetime.now().strftime("%H:%M:%S") == time_off:
            break
    
    st.write("Alarm going off")
