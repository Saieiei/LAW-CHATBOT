import streamlit as st
from backend import comp_process

# Assign your OpenAI API key here
api_key = "sk-"

def frontend():
    # Streamlit UI
    st.set_page_config(page_title="Chat with LAWGPT 🤖")
    st.title("Chat with :green[LAWGPT] using Multiple :red[PDF Files] 🤖!")
    question = st.text_input("Ask Your Legal Below: ")

    with st.sidebar:
        st.image("law.jpeg")
        st.subheader("Upload PDFs Here")
        pdfs=st.file_uploader("Upload PDF File", type=["pdf"], accept_multiple_files=True)
        st.button('Process')
        st.write('Made with ❤️ by [Sairudra More](https://www.linkedin.com/in/sairudra-more/)')
        
    if pdfs and api_key is not None:  
        if question:                     
            ans=comp_process(apikey=api_key, pdfs=pdfs, question=question)
            st.write(ans)



if __name__ == "__main__":
    frontend()
