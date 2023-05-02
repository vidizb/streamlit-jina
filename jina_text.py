import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Text Search",)

endpoint = "https://vidizb-streamlit-jina-jina-text-e5vbu7.streamlit.app/api/search"

st.title("Jina Text Search")
st.markdown("You can run our [Wikipedia search example](https://github.com/jina-ai/examples/tree/master/wikipedia-sentences) to test out this search")

jina.text_search(endpoint=endpoint)
