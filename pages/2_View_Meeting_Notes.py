from support_file import *

page_configuration("View Meeting Notes", "📖")
search_container = st.container()
selected = search_container.text_input("**Enter the Meeting ID**", placeholder="Search here...")
searched = search_container.button("Fetch Meeting notes")
if searched:
    if len(selected) == 0:
        st.warning("Oops!! you forgot to enter the meeting ID.", icon="⚠️")
    else:
        fetched_result = fetch_meeting_notes(selected)
        if fetched_result != None:
            display_meeting_notes(fetched_result)
        else:
            st.warning("Oops!! there is no such meeting ID with us.", icon="⚠️")