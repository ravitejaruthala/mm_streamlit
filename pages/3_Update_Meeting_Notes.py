# 3_Update_Meeting_Notes.py
import streamlit as st
from support_file import *
from datetime import datetime

page_configuration("Update Meeting Notes", "📝")

st.subheader("Update Meeting Notes")

unique_code = st.text_input("Enter the Unique Code:", max_chars=16)

if st.button("Fetch Meeting Notes"):
    meeting_data = fetch_meeting_notes(unique_code)
    if meeting_data:
        st.write("Current Meeting Notes:")
        st.write(dict(meeting_data))
        st.write("---")
        st.subheader("Update Meeting Information:")
        
        with st.form(key='update_form'):
            new_author_name = st.text_input("Author's Name:", value=meeting_data['author_name'])
            new_author_email = st.text_input("Author's Email:", value=meeting_data['author_email'])
            
            # Handle meeting_date
            if meeting_data['meeting_date']:
                current_date = datetime.strptime(meeting_data['meeting_date'], '%Y-%m-%d')
            else:
                current_date = datetime.now()
            
            new_meeting_date = st.date_input("Meeting Date:", value=current_date)
            
            new_meeting_agenda = st.text_input("Meeting Agenda:", value=meeting_data['meeting_agenda'])
            new_meeting_notes = st.text_area("Meeting Notes:", value=meeting_data['meeting_notes'])
            
            submit_button = st.form_submit_button("Update Meeting Notes")
            
            if submit_button:
                update_meeting_notes(
                    unique_code,
                    new_author_name,
                    new_author_email,
                    new_meeting_date.strftime('%Y-%m-%d'),
                    new_meeting_agenda,
                    new_meeting_notes
                )
                st.success("Meeting Notes Updated Successfully!")
                
                # Optionally clear session state or form inputs after successful update
                st.session_state.new_author_name = ""
                st.session_state.new_author_email = ""
                st.session_state.new_meeting_agenda = ""
                st.session_state.new_meeting_notes = ""
                
    else:
        st.error("No meeting found with that Unique Code.")
