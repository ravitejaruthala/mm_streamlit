import streamlit as st
from support_file import *

st.set_page_config(page_title="Minutes of Meeting", page_icon="📋")
st.markdown(streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Minutes of Meeting - Form</h1>", unsafe_allow_html=True)
with st.form("MofM_form"):
   input_name = st.text_input("**Author's Name:**", placeholder="Enter your name here.", key="author_name", max_chars=50)
   input_email = st.text_input("**Author's Email ID:**", placeholder="Enter your email address here.", key="author_email", max_chars=50)
   input_date = st.date_input("**Date of the Meeting:**", value="today", format="MM/DD/YYYY", key="meeting_date")
   input_agenda = st.text_input("**Agenda of the Meeting:**", placeholder="Specify the meeting's agenda here.", key="meeting_agenda")
   input_notes = st.text_area("**Minutes of the Meeting:**", placeholder="Mention the meeting minutes here.", key="meeting_notes")
   columns = st.columns([12,1.5], gap="small")
   with columns[0]:
    submitted = st.form_submit_button("Submit", on_click=input_validation)
   with columns[1]:
    reset_button = st.form_submit_button('Reset', on_click=reset_value)
   if submitted:
       st.toast('Submitted successfully!', icon="✅")
       st.balloons()