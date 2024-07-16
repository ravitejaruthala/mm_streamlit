from support_file import *

page_configuration("Record Meeting Notes", "✍️")

with st.form("MofM_form", clear_on_submit=True):
    input_name = st.text_input("**Author's Name:**", placeholder="Enter your name here.", key="author_name", max_chars=50)
    input_email = st.text_input("**Author's Email ID:**", placeholder="Enter your email address here.", key="author_email", max_chars=50)
    input_date = st.date_input("**Date of the Meeting:**", key="meeting_date")
    input_agenda = st.text_input("**Agenda of the Meeting:**", placeholder="Specify the meeting's agenda here.", key="meeting_agenda")
    input_notes = st.text_area("**Minutes of the Meeting:**", placeholder="Mention the meeting minutes here.", key="meeting_notes")
    st.write('***:red[Before clicking on Submit button, make sure all the fields are filled properly with valid data. Else you will lose your meeting notes.]***')
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        submitted = st.form_submit_button("Submit")  
    with columns[1]:
        reseted = st.form_submit_button('Reset')
    if submitted:
        if(len(input_name) or len(input_email) or len(input_agenda) or len(input_notes)==0):
            st.warning("Oops!! we can't record your empty inputs.", icon="⚠️")
        else:
            save_meeting_notes(input_name, input_email, input_date, input_agenda, input_notes)
            form_success_notification()
    elif reseted:
        st.toast('Your input was cleared!', icon="🧹")