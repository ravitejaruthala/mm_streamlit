from support_file import *

page_configuration("Retrieve Meeting IDs", "📨")

with st.form("Retrieve_IDs", clear_on_submit=True):
    email_address = st.text_input("**Enter your Email ID**", placeholder="Type your email address here...", key="email_ID", max_chars=50)
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        retrieved = st.form_submit_button("Retrieve Meeting IDs")
    with columns[1]:
        reseted = st.form_submit_button('Reset')
if retrieved:
    if(len(email_address) == 0):
        st.warning("Oops!! you forgot to enter a valid email address.", icon="⚠️")
    else:
        if len(fetch_meeting_ids(email_address)):
            st.success("Notes found, we have sent the meeting details to "+email_address, icon="✅")
        else:
            st.warning("Oops!! we don't have any meeting notes with this email address. We appreciate if you have one.", icon="⚠️")
elif reseted:
    st.toast('Your input was cleared!', icon="🧹")