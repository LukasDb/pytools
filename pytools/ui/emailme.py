def emailme(*args):
    """This function sends an email to yourself (only gmail supported atm). It reads an application password from the environment variable GMAIL_API_KEY and the email from GMAIL_EMAIL."""
    from smtplib import SMTP
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import os

    hostname = os.uname()[1]
    try:
        mail_address = os.environ["GMAIL_EMAIL"]
    except KeyError:
        raise KeyError("Please set the environment variable GMAIL_EMAIL")

    try:
        passwd = os.environ["GMAIL_API_KEY"]
    except KeyError:
        raise KeyError("Please set the environment variable GMAIL_API_KEY")

    # build message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Notification from {hostname}"
    msg["From"] = mail_address
    msg["To"] = mail_address
    html = f"""\
    <html>
    <head></head>
    <body>
        <p>
        {"<br>".join(args)}
        </p>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    # send message
    with SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(mail_address, passwd)
        smtp.sendmail(
            mail_address,
            mail_address,
            msg.as_string(),
        )


if __name__ == "__main__":
    emailme("Hello World!")
