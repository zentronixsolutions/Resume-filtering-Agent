import pandas as pd
import smtplib
from email.message import EmailMessage

def send_resume_data(hr_email, csv_file_path, sender_email, sender_password):
    candidates = pd.read_csv(csv_file_path)
    candidate_html = candidates.to_html(index=False)

    msg = EmailMessage()
    msg['Subject'] = 'List of Selected Candidates'
    msg['From'] = sender_email
    msg['To'] = hr_email
    msg.set_content('This is a plain text version in case HTML is not supported.')
    msg.add_alternative(f"""
    <html>
        <body>
            <h2>Selected Candidates</h2>
            {candidate_html}
        </body>
    </html>
    """, subtype='html')

    with open(csv_file_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
send_resume_data(hr_email, csv_file_path, sender_email, sender_password)
print("Email Sent sucessfully")