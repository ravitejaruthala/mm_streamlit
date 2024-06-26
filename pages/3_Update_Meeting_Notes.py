from support_file import *

page_configuration("Update Meeting Notes", "📝")
with st.form("Update_Notes", clear_on_submit=True):
    unique_code = st.text_input("**Enter the Meeting ID**", placeholder="Search here...", key="meeting_ID", max_chars=16)
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        searched = st.form_submit_button("Fetch Meeting notes")
    with columns[1]:
        reseted = st.form_submit_button('Reset')
    if searched:
        if len(unique_code) == 0:
            st.warning("Oops!! you forgot to enter the meeting ID.", icon="⚠️")
        else:
            fetched_result = fetch_meeting_notes(unique_code)
            if fetched_result != None:
                edit_meeting_notes(unique_code, fetched_result)
            else:
                st.warning("Oops!! there is no such meeting ID with us.", icon="⚠️")
    elif reseted:
        st.toast('The meeting ID was cleared!', icon="🧹")