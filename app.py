import streamlit as st
import pandas as pd
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Function to generate question paper PDF
def generate_question_paper(selected_questions, filename="question_paper.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []
    
    story.append(Paragraph("<b>Rosary Academy - Question Paper</b>", styles['Title']))
    story.append(Spacer(1, 20))
    
    for idx, row in enumerate(selected_questions, 1):
        story.append(Paragraph(f"{idx}. {row['Question']} ({row['Marks']} Marks)", styles['Normal']))
        story.append(Spacer(1, 12))
    
    doc.build(story)
    return filename

# Streamlit UI
st.title("📘 Automatic Question Paper Generator")

uploaded_file = st.file_uploader("Upload Question Bank (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📂 Question Bank Preview")
    st.write(df.head())

    if "Question" not in df.columns or "Marks" not in df.columns:
        st.error("❌ File must contain 'Question' and 'Marks' columns.")
    else:
        total_marks = st.number_input("Enter total marks for paper:", min_value=10, step=10, value=50)

        if st.button("Generate Paper"):
            selected_questions = []
            current_marks = 0

            shuffled = df.sample(frac=1).to_dict("records")  # Shuffle

            for q in shuffled:
                if current_marks + q["Marks"] <= total_marks:
                    selected_questions.append(q)
                    current_marks += q["Marks"]

            if not selected_questions:
                st.error("⚠️ Couldn't generate paper. Try different marks distribution.")
            else:
                filename = generate_question_paper(selected_questions)
                st.success("✅ Question Paper Generated!")
                with open(filename, "rb") as f:
                    st.download_button("📥 Download Paper", f, file_name=filename)
