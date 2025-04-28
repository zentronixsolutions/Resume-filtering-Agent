from groq import Groq


job_description = input("Enter the Job Description: ")
cv_text = "artifact\\Resume.pdf"

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
    {
      "role": "user",
      "content": f"""
      You are an expert HR recruiter and AI document verifier.

Given a Job Description and a Candidate's CV Document, you must:

Step 1: Validate the Document Type
Check if the given document is a valid CV or Resume.

If it IS a valid CV, proceed to Step 2.

Step 2: Extract Candidate Information
Extract (if available):

      Candidate Name

      Candidate Email

      Candidate Phone Number

Step 3: Match the CV with Job Description
Compare the candidate's:

      Skills

      Experiences

      Qualifications (Degrees, Certifications)

      Projects (Academic or Professional)

Experience Handling Rule:

      If Job Description specifically mentions experience (e.g., "2 years required"), check and score accordingly.

      If Experience is NOT mentioned or Entry Level job, then do not deduct marks for missing experience.

Qualification Rule:

      If the candidate has strong educational qualifications (relevant degree, certifications), give higher score.

      If qualification is weak or unrelated, reduce score.

Projects Rule:

      If relevant projects are listed (academic or professional), increase score.

      If no projects are listed, decrease score slightly.

Step 4: Provide a Final Evaluation
Output the result in CSV format with the following fields:

      Candidate Name: [Extracted Name or "Not Found"]

      Candidate Email: [Extracted Email or "Not Found"]

      Candidate Phone: [Extracted Phone or "Not Found"]

      Match Score: X/10

      Reason: [Brief explanation]

Example CSV Output:

      Candidate Name, Candidate Email, Candidate Phone, Match Score, Reason
      John Doe, john.doe@gmail.com, +1-234-567-8901, 8/10, Candidate has strong skills in Python but limited experience in cloud deployment.

show only the important output not the process 


Job Description: {job_description}
Candidate CV: {cv_text}
""" 
    }
  ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,

)

print(completion.choices[0].message.content)