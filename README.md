# AI Resume Analyser

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_API-green)

An LLM-powered tool that compares your resume against a job description and gives you a match score, missing skills, improvement suggestions, and formatting/ATS issues — all in a clean web interface.

🌐 **Live Demo:** https://airesumeradar.streamlit.app/

Built as a hands-on project to bridge Python fundamentals with real-world AI application development: PDF parsing, prompt design, structured LLM output, error handling, and a working UI — no fluff, just working code.

## How it works

1. Upload your resume (PDF)
2. Paste in a job description
3. Get back:
   - Match score (0–100)
   - Matching skills
   - Missing skills
   - Improvement suggestions
   - ATS & formatting issues

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- pdfplumber

## Live Demo

👉 https://airesumeradar.streamlit.app/

## Status

✅ Live — core pipeline complete (PDF extraction → LLM analysis → UI)

## Why this exists

Resumes often get filtered by Applicant Tracking Systems (ATS) before a recruiter ever sees them. This project helps identify skill gaps, improve resume quality, and catch formatting issues that can reduce interview chances.
