import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("Email Notification App")

# Email configuration
email_sender = st.text_input("Enter your email address (sender):", "")
email_password = st.text_input("Enter your email password:", type="password")
email_receiver = st.text_input("Enter recipient email address:", "")
body = st.text_input("Enter the message you want to send:", "")

if st.button("Start Sending Notifications"):
    if email_sender and email_password and email_receiver:
        try:
            while True:
                # Create message
                msg = MIMEMultipart()
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = "Hi!"
                
                msg.attach(MIMEText(body, 'plain'))

                # Create server connection
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_sender, email_password)
                
                # Send email
                text = msg.as_string()
                server.sendmail(email_sender, email_receiver, text)
                server.quit()
                
                st.success(f"Email sent to {email_receiver}")
                time.sleep(60)  # Wait for 1 minute
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in all email fields!")

st.sidebar.header("About")
st.sidebar.write("This app sends an email notification every minute!")
st.sidebar.warning("Note: For Gmail, you need to use an App Password instead of your regular password.")
