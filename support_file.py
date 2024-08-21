import streamlit as st
import secrets
from jinja2 import Template
import streamlit.components.v1 as components
from datetime import datetime
import time
import psycopg2

streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

### User-defined functions for Streamlit ###

def page_configuration(title_parameter, icon_parameter):
    st.set_page_config(page_title=title_parameter, page_icon=icon_parameter)
    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{title_parameter}</h1>", unsafe_allow_html=True)
    
def stream_data_content(subheader_parameter, content_parameter):
    st.subheader(subheader_parameter)
    for word in content_parameter.split(" "):
        yield word + " "
        time.sleep(0.03)
        
def display_meeting_notes(result_parameter):
    with open("template.html", "r") as template_file:
        template_content = template_file.read()
        jinja_template = Template(template_content)
        rendered_html = jinja_template.render(fetched_content = result_parameter)
        components.html(rendered_html, height=1000, scrolling=True)

@st.experimental_dialog("Update Meeting Notes.", width="large")        
def edit_meeting_notes(ID_parameter, result_parameter):
    st.subheader("***We have the below details about your meeting notes.***")
    with st.form(key='update_form', clear_on_submit=True):
        new_author_name = st.text_input("Author's Name:", value=result_parameter[2])
        new_author_email = st.text_input("Author's Email:", value=result_parameter[3])
        new_meeting_date = st.date_input("Date of the Meeting:", value=datetime.strptime(result_parameter[4], '%Y-%m-%d'))  
        new_meeting_agenda = st.text_input("Meeting Agenda:", value=result_parameter[5])
        new_meeting_notes = st.text_area("Meeting Notes:", value=result_parameter[6])
        clicked = st.form_submit_button("Update the meeting notes")
        if clicked:
            update_meeting_notes(
                ID_parameter,
                new_author_name,
                new_author_email,
                new_meeting_date.strftime('%Y-%m-%d'),
                new_meeting_agenda,
                new_meeting_notes
            )
            st.rerun()
            
def form_success_notification():
    st.toast('Submitted successfully!', icon="✅")
    st.balloons()
    st.toast('You will receive an email shortly!', icon="✉️")
    
### User-defined functions for DataBase ###

def initialize_db():
    conn = psycopg2.connect(st.secrets["DB_URL"])
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
    id INT DEFAULT nextval('notes_sequence'),
    unique_code STRING PRIMARY KEY NOT NULL,
    author_name STRING NOT NULL,
    author_email STRING NOT NULL,
    meeting_date STRING NOT NULL,
    meeting_agenda STRING NOT NULL,
    meeting_notes STRING NOT NULL );
    ''')
    conn.commit()
    cur.close()
    conn.close()

def generate_unique_code():
    return secrets.token_hex(8)  # 8 bytes = 16 characters in hexadecimal

def save_meeting_notes(author_name, author_email, meeting_date, meeting_agenda, meeting_notes):
    unique_code = generate_unique_code()
    conn = psycopg2.connect(st.secrets["DB_URL"])
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes) VALUES (%s, %s, %s, %s, %s, %s)",
        (unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes)
    )
    conn.commit()
    cur.close()
    conn.close()

def fetch_meeting_notes(unique_code):
    conn = psycopg2.connect(st.secrets["DB_URL"])
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE unique_code = %s", (unique_code,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def fetch_meeting_ids(email_id):
    conn = psycopg2.connect(st.secrets["DB_URL"])
    cur = conn.cursor()
    cur.execute("SELECT meeting_date, meeting_agenda, unique_code FROM notes WHERE author_email = %s", (email_id,))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def update_meeting_notes(unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes):
    conn = psycopg2.connect(st.secrets["DB_URL"])
    cur = conn.cursor()
    cur.execute(
        "UPDATE notes SET author_name=%s, author_email=%s, meeting_date=%s, meeting_agenda=%s, meeting_notes=%s WHERE unique_code=%s",
        (author_name, author_email, meeting_date, meeting_agenda, meeting_notes, unique_code)
    )
    conn.commit()
    cur.close()
    conn.close()