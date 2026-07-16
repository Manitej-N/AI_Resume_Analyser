import streamlit as st
import json
import extract 
import analyser

title = st.title("Resume Analyser")
uploaded_cv = st.file_uploader("Upload your resume here")
job_description = st.text_area("Enter job description here")

if st.button("Analyse"):
    if uploaded_cv is None:
        st.write("Upload your CV")
    elif job_description.strip() == "":
        st.write("Please enter a job description")
    else:
        pdf_data = extract.extract_text_frm_pdf(uploaded_cv)
        if pdf_data.strip() == "":
            st.write("Uploaded resume can't be read — it may be a scanned image with no selectable text.")
        else:
            prompt = f"""You are a resume analysis assistant. Compare the following resume against 
the job description and return your analysis.

RESUME:
{pdf_data}

JOB DESCRIPTION:
{job_description}

Return ONLY a valid JSON object with exactly this structure, no extra text, 
no markdown formatting, no explanation outside the JSON:

{{
  "match_score": <integer between 0 and 100>,
  "matching_skills": [<list of strings>],
  "missing_skills": [<list of strings>],
  "suggestions": [<list of strings>],
  "formatting_issues": [<list of strings>]
}}"""
            raw_result = analyser.call_model(prompt)
            result = json.loads(raw_result)
            if "match_score" in result:
                st.write("Match Score: ", result["match_score"])
                st.subheader("Matched Skills")
                for item in result["matching_skills"]:
                    st.markdown(f"- {item}")
                st.subheader("Missing Skills")
                for item in result["missing_skills"]:
                    st.markdown(f"- {item}")
                st.subheader("Suggestions")
                for item in result["suggestions"]:
                    st.markdown(f"- {item}")
                st.subheader("Formatting Issues")
                for item in result["formatting_issues"]:
                    st.markdown(f"- {item}")
            else:
                st.write(result["error"])