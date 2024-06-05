import streamlit as st
import datetime

def reset_value():
    st.session_state.author_name = None
    st.session_state.author_email = None
    st.session_state.meeting_agenda = None
    st.session_state.meeting_notes = None
    
st.set_page_config(page_title="Minutes of Meeting", page_icon="📋")
st.markdown("# Minutes of Meeting - Form")
with st.form("MofM_form"):
   st.text_input("**Author's Name:**", placeholder="Enter your name here.", key="author_name")
   st.text_input("**Author's Email ID:**", placeholder="Enter your email address here.", key="author_email")
   st.date_input("**Date of the Meeting:**", value="today", format="MM/DD/YYYY", key="meeting_date")
   st.text_input("**Agenda of the Meeting:**", placeholder="Specify the meeting's agenda here.", key="meeting_agenda")
   st.text_area("**Minutes of the Meeting:**", placeholder="Mention the meeting minutes here.", key="meeting_notes")
   submitted = st.form_submit_button("Submit")
   st.form_submit_button('Reset', on_click=reset_value)
   if submitted:
       st.success('Submitted successfully!', icon="✅")