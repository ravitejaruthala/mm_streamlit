import streamlit as st
import datetime

st.set_page_config(page_title="Minutes of Meeting", page_icon="📋")
st.markdown("# Minutes of Meeting - Form")
with st.form("MofM_form"):
   st.text_input("**Author's Name:**", placeholder="Enter your name here.")
   st.text_input("**Author's Email ID:**", placeholder="Enter your email address here.")
   st.date_input("**Date of the Meeting:**", value="today", format="MM/DD/YYYY", key='date')
   st.text_input("**Agenda of the Meeting:**", placeholder="Specify the meeting's agenda here.")
   st.text_area("**Minutes of the Meeting:**", placeholder="Mention the meeting minutes here.")
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.success('Submitted successfully!', icon="✅")