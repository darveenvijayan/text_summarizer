import streamlit as st
# from model import Abstractive_Summarization_Model
from transformers import pipeline


# initialize model object
# @st.cache
def load_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#     summarizer = Abstractive_Summarization_Model()

    return summarizer


# Main app engine
if __name__ == "__main__":
    # display title and description
    st.title("Text Summarizer")
    st.write("Get summaries of your text - please wait 5-8 minutes as the model loads.")

    #load model
    summarizer = load_model()

    # display topic input slot
    text = st.text_input("Input Text", "")

    # display article paragraph
    article_paragraph = st.empty()

    if text:
        # load wikipedia summary of topic

#         summary = summarizer.summarize(text)
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)['summary_text']

        # display article summary in paragraph
        article_paragraph.markdown(summary)

