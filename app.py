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

