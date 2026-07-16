import os
import extract 
import json
from google import genai
from dotenv import load_dotenv
load_dotenv('.env')
key = os.getenv("GOOGLE_API_KEY") 
client = genai.Client(api_key=key)
job_description = """Job Title: Junior Software Tester (Internship)
Location: Remote / Hybrid

About the role:
We are looking for a motivated Junior Software Tester to join our QA team. 
You will support manual and automated testing of web applications, help 
identify and document defects, and work closely with developers to improve 
software quality.

Responsibilities:
- Execute manual test cases and report bugs clearly using a defect tracking tool
- Assist in writing and maintaining automated test scripts (Python preferred)
- Perform regression testing before releases
- Collaborate with developers to reproduce and verify bug fixes
- Document test results and maintain test case repositories
- Participate in agile ceremonies (standups, sprint planning)

Requirements:
- Currently pursuing or recently completed a degree in Computer Science or related field
- Basic understanding of software testing concepts (unit testing, test cases, defect lifecycle)
- Familiarity with Python or another programming language
- Strong attention to detail and analytical thinking
- Good written communication skills
- Experience with version control (Git) is a plus
- Exposure to test automation frameworks (Selenium, PyTest) is a plus but not required"""
final_output = extract.extract_text_frm_pdf("sample_data/sample_data_1.pdf")
def call_model(prompt):
    output = client.models.generate_content(model="gemini-3.5-flash", contents= prompt)
    return output.text
prompt = f"""You are a resume analysis assistant. Compare the following resume against 
the job description and return your analysis.

RESUME:
{final_output}

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
raw_result = call_model(prompt)
result = json.loads(raw_result)
print(result["match_score"])