#Before excute install imaplib in your desktop
import imaplib
import email

inap_server = "inap.world4you.com"
email_address = "mailtest@vini.com"
password = "mailtest123"

inap = imapLib.IMAP4_SSL(inap_server)
inap.login(email_address, password)

inap.select("Inbox")
_, nsgnums = inap.search(None, "ALL")

for msgnum in nsgnums[0].split():
    _, data = inap.fetch(msgnum, "(RFC822)")

    message = email.message_from_binary_file(data[0][1])

    print(f"Message Number: {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")

    print("Content: ")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())

