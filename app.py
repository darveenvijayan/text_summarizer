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

    st.write("Get AI generated summaries of text! - please wait a couple of seconds for the model to load.")
    st.write("Meanwhile checkout my github page -> https://github.com/darveenvijayan")

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
