from support_file import *

page_configuration("View Meeting Notes", "📖")
with st.form("View_Notes", clear_on_submit=True):
    selected = st.text_input("**Enter the Meeting ID**", placeholder="Search here...", key="meeting_ID", max_chars=16)
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        searched = st.form_submit_button("Fetch Meeting notes")
    with columns[1]:
        reseted = st.form_submit_button('Reset')
if searched:
    if len(selected) == 0:
        st.warning("Oops!! you forgot to enter the meeting ID.", icon="⚠️")
    else:
        fetched_result = fetch_meeting_notes(selected)
        if fetched_result != None:
            display_meeting_notes(fetched_result)
        else:
            st.warning("Oops!! there is no such meeting ID with us.", icon="⚠️")
elif reseted:
    st.toast('Your input was cleared!', icon="🧹")