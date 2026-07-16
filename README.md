# 📄 AI Resume Analyser

An LLM-powered tool that compares your resume against a job description and gives you a match score, missing skills, improvement suggestions, and formatting/ATS issues — all in a clean web interface.

Built as a hands-on project to bridge Python fundamentals with real-world AI application development: PDF parsing, prompt design, structured LLM output, error handling, and a working UI — no fluff, just working code.

## How it works
1. Upload your resume (PDF)
2. Paste in a job description
3. Get back:
   - **Match score** (0–100)
   - **Matching skills** — what already aligns with the role
   - **Missing skills** — gaps worth addressing
   - **Suggestions** — concrete ways to improve the resume
   - **Formatting issues** — things that might trip up an ATS (broken links, typos, inconsistent formatting)

## Tech Stack
- Python
- Streamlit (UI)
- Google Gemini API (analysis engine)
- pdfplumber (PDF text extraction)

## Status
🚀 Live — core pipeline complete (PDF extraction → LLM analysis → UI)

## Why this exists
Resumes get filtered by algorithms before a human ever sees them. This tool tries to show you what that algorithm might be thinking — and catches the kind of small formatting mistakes that quietly hurt real applications.
