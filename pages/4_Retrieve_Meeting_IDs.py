from support_file import *

page_configuration("Retrieve Meeting IDs", "📨")

with st.form("Retrieve_IDs", clear_on_submit=True):
    email_address = st.text_input("**Enter your Email ID**", placeholder="Type your email address here...", key="email_ID", max_chars=50)
    columns = st.columns([12, 1.5], gap="small")
    with columns[0]:
        retrieved = st.form_submit_button("Retrieve associated Meeting IDs")
    with columns[1]:
        reseted = st.form_submit_button('Reset')