import streamlit as st
from model import Abstractive_Summarization_Model


# initialize model object
# @st.cache
def load_model():
    return Abstractive_Summarization_Model()

# Main app engine
if __name__ == "__main__":
    # display title and description
    st.title("AI Text Summarizer")
    st.header("Get AI generated paraphrased summaries of text!")
    st.write("You might need to wait a couple of seconds for the model to load because i'm using a tiny cpu 🥲")
    st.write("email me at darveenvijayan.27@gmail.com")

    #load model
    ASM = load_model()

    # display topic input slot
    text = st.text_input("Paste a paragraph of text in the text box below and hit ENTER!", "")

    # display article paragraph
    article_paragraph = st.empty()

    if text:
        # load wikipedia summary of topic

        summary = ASM.summarize(text)

        # display article summary in paragraph
        article_paragraph.markdown(summary)
