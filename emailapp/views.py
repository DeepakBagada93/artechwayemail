from django.shortcuts import render
from validate_email_address import validate_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, sender_email):
    # Set your Gmail SMTP server and credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'deeepakbagada25@gmail.com'
    smtp_password = 'kmqcufpfyjcuchrx'  # Use an App Password for security

    # Set sender and recipient emails
    sender_name = 'Your Name'

    # Create the MIME object with HTML content
    message = MIMEMultipart()
    message['From'] = f'{sender_name} <{sender_email}>'
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the HTML content to the email
    message.attach(MIMEText(body, 'html'))

    # Connect to the Gmail SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account using an App Password
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

def index(request):
    email_list = None

    if request.method == 'POST':
        email_addresses = [email.strip() for email in request.POST.get('email_addresses').split(',')]

        email_subject = 'Unlock Digital Success with Artechway: Exclusive Packages Inside!'
        email_body = """<div style="font-size: 16px; text-align: center; background-color: #f4f4f4; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
            <p><strong>Hi,</strong></p>
            <p>I hope this email finds you well. I'm reaching out from Artechway, a leading digital marketing agency, with a golden opportunity to elevate your brand's online presence.</p>
            <!-- Rest of the email content -->
             <p><strong>Why Artechway?</strong></p>
            <p>At Artechway, we blend innovation and strategy to craft digital success stories. Our team is committed to transforming your brand into a digital marvel, ensuring you stand out in the crowded online landscape.</p>
            <img src="https://artechway.com/wp-content/uploads/2023/11/2.png" alt="Artechway Image" style="max-width: 100%; height: auto;">
            <p><strong>Take the First Step: Receive Our Brochure!</strong></p>
            <p>To discover more about how Artechway can revolutionize your digital presence, I've attached our company brochure. [Company Brochure Attachment]</p>
            <p><strong>Let's Discuss Your Digital Journey:</strong></p>
            <p>Are you available for a brief call this week? We would love the opportunity to learn more about your goals and share insights on how Artechway can propel your brand to new heights.</p>
            <p>Thank you for considering Artechway. We look forward to the possibility of partnering with you on your digital success journey.</p>
            <p><strong>Best regards,</strong></p>
            <p>Deepak Bagada, CEO (Artechway: Crafting Digital Marvels)</p>
            <p><a href="http://www.artechway.com">www.artechway.com</a></p>
            <a href="https://artechway.com/" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; margin-right: 10px; border-radius: 5px;">Learn More</a>
            <a href="https://wa.me/7016179234" style="background-color: #25D366; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; border-radius: 5px;">WhatsApp</a>
        </div>"""

        # Concatenate subject and HTML body
        full_email_body = f"\n{email_body}"

        # Create a list of dictionaries containing email addresses for display on the index page
        email_list = [{'email': email, 'status': 'Sent' if validate_email(email) else 'Invalid'} for email in email_addresses]

        # Remove any empty email addresses
        email_addresses = [email for email in email_addresses if email]

        # Add each email to the table body
        table_body = "<table border='1'><tr><th>Email Address</th></tr>"
        for recipient_email in email_addresses:
            table_body += f"<tr><td>{recipient_email}</td></tr>"
        table_body += "</table>"

        # Send the email list to the sender's email
        send_email('Recipient List', table_body, sender_email='deeepakbagada25@gmail.com', to_email='deeepakbagada25@gmail.com')

        # Send the HTML template to each recipient
        for recipient_email in email_addresses:
            print(f"Sending email to: {recipient_email}")
            if validate_email(recipient_email):
                send_email(email_subject, full_email_body, recipient_email, sender_email='deeepakbagada25@gmail.com')
            else:
                print(f"Invalid email address: {recipient_email}")

    return render(request, 'emailapp/index.html', {'email_list': email_list})
