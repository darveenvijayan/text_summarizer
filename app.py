"""

import streamlit as st
from model import Abstractive_Summarization_Model


# initialize model object
# @st.cache
def load_model():
    return Abstractive_Summarization_Model()

# Main app engine
if __name__ == "__main__":
    # display title and description
    st.title("Text Summarizer")
    st.write("Get summaries of your text - please wait 5-8 minutes as the model loads.")

    #load model
    ASM = load_model()

    # display topic input slot
    text = st.text_input("Input Text", "")

    # display article paragraph
    article_paragraph = st.empty()

    if text:
        # load wikipedia summary of topic

        summary = ASM.summarize(text)

        # display article summary in paragraph
        article_paragraph.markdown(summary)
"""

#=====================================


import streamlit as st
from transformers import pipeline


# initialize model object
# @st.cache
def load_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer




# Main app engine
if __name__ == "__main__":
    # display title and description
    st.title("Text Summarizer")

    st.write("Get AI generated paraphrased summaries of text! - please wait a couple of seconds for the model to load.")
    st.write("email me at darveenvijayan.27@gmail.com")

    #load model
    summarizer = load_model()

    # display topic input slot
    text = st.text_input("Paste a paragraph of text in the text box below", "")

    # display article paragraph
    article_paragraph = st.empty()

    if text:
        # summarize
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

        # display article summary in paragraph
        article_paragraph.markdown(summary[0]['summary_text'])
