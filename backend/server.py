import streamlit as st 
from api import auth, docs, drive, slides, config
from llm import keys, summarize


st.header("Generate Cheat Sheet")

pres_form = st.form(key="Presentations")


# set the document name
pres_form.header("Document Name")

doc_name = 'cheat-sheet'
doc_name = pres_form.text_input("Name the document", 'cheat-sheet')

pres_form.header("Information")

# get the list of presentations
auth.authenticate_create_token()
presentations_full = drive.get_presentations()

# assign each presentation with a name as the key and an id as the value, useful for later
presentations = {presentation['name']: presentation['id'] for presentation in presentations_full}

selections = pres_form.multiselect("Select the presentations to extract information from", presentations)

list_of_ids = []
for thing in selections:
    list_of_ids.append(presentations[thing])

topics = []

pres_form.header("Topics")

@st.cache_data
def Topics():
    return []

topic_text = pres_form.text_input("Input topics separated by commas", "example 1, example 2")

topics = [x for x in topic_text.split(',')]

if pres_form.form_submit_button("Submit"):

    presentation_text = slides.get_mult_pres_text(list_of_ids)

    summary = summarize.create_summary(presentation_text, topics)

    docs.create_document(doc_name, summary.content)

