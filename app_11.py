import streamlit as st
from modules.rag import ask_question

st.set_page_config(
    page_title="AI Sales Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Sales Assistant")
st.markdown("Upload documents and ask questions using Llama 3 + RAG")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "RAG Chat",
        "Meeting Prep",
        "Competitor Analysis",
        "Objection Handler"
    ]
)

# -------------------
# RAG CHAT
# -------------------

if page == "RAG Chat":

    st.header("📄 Document Question Answering")

    question = st.text_input(
        "Ask a question about uploaded documents"
    )

    if st.button("Generate Answer"):

        if question:

            with st.spinner("Thinking..."):

                answer = ask_question(question)

                st.success("Answer Generated")

                st.write(answer)

# -------------------
# MEETING PREP
# -------------------

elif page == "Meeting Prep":

    st.header("📋 Meeting Preparation")

    company = st.text_input("Company Name")

    industry = st.text_input("Industry")

    if st.button("Prepare Meeting Brief"):

        prompt = f"""
        Prepare a sales meeting brief.

        Company: {company}
        Industry: {industry}

        Include:
        - Company Overview
        - Industry Challenges
        - Pain Points
        - Sales Opportunities
        - Questions To Ask
        """

        answer = ask_question(prompt)

        st.write(answer)

# -------------------
# COMPETITOR ANALYSIS
# -------------------

elif page == "Competitor Analysis":

    st.header("⚔ Competitor Intelligence")

    product = st.text_input("Our Product")

    competitor = st.text_input("Competitor")

    if st.button("Analyze Competitor"):

        prompt = f"""
        Compare:

        Product: {product}

        Competitor: {competitor}

        Provide:
        - Strengths
        - Weaknesses
        - Competitive Positioning
        """

        answer = ask_question(prompt)

        st.write(answer)

# -------------------
# OBJECTION HANDLER
# -------------------

elif page == "Objection Handler":

    st.header("💬 Customer Objection Handler")

    objection = st.text_area(
        "Customer Objection"
    )

    if st.button("Generate Response"):

        prompt = f"""
        Customer objection:

        {objection}

        Generate:

        1. Empathetic response
        2. Business justification
        3. Follow-up question
        """

        answer = ask_question(prompt)

        st.write(answer)
