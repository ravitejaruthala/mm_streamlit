from support_file import *

page_configuration("Update Meeting Notes", "📝")
search_container = st.container()
unique_code = search_container.text_input("**Enter the Meeting ID**", placeholder="Search here...", max_chars=16)
searched = search_container.button("Fetch Meeting notes")
if searched:
    if len(unique_code) == 0:
        st.warning("Oops!! you forgot to enter the meeting ID.", icon="⚠️")
    else:
        fetched_result = fetch_meeting_notes(unique_code)
        if fetched_result != None:
            edit_meeting_notes(unique_code, fetched_result)
            st.session_state.unique_code = None       
        else:
            st.warning("Oops!! there is no such meeting ID with us.", icon="⚠️")
            st.session_state.unique_code = None