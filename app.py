import streamlit as st

st.set_page_config(
    page_title="PPT Agent Suite",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 PPT Agent Suite")
st.markdown("---")

st.markdown("""
Welcome! This app uses **AI agents powered by Groq LLMs** to convert your research papers
into polished PowerPoint presentations automatically.

Choose a tool from the sidebar, or click a card below to get started.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📄 PPT Agent
    Upload a **single `.tex` file** and let the agent:
    - Parse and summarize your LaTeX paper
    - Generate a structured slide outline
    - Build a themed PPTX file

    > Best for: Single-file LaTeX papers
    """)
    st.page_link("pages/1_PPT_Agent.py", label="Open PPT Agent →", icon="📄")

with col2:
    st.markdown("""
    ### 🖼️ PPT Agent with Images
    Upload a **`.zip` or `.tar.gz` archive** of your full LaTeX project and the agent will:
    - Locate `main.tex` automatically
    - Extract and embed figures from your project
    - Build a presentation with dedicated visual slides

    > Best for: Full LaTeX projects with figures
    """)
    st.page_link("pages/2_PPT_Agent_with_Images.py", label="Open PPT Agent with Images →", icon="🖼️")

st.markdown("---")
st.caption("Built with LangChain · Groq · python-pptx · Streamlit")
