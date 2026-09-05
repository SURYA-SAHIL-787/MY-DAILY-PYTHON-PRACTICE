class Email:
    def __init__(self, sender, subject, message):
        self.sender = sender
        self.subject = subject
        self.message = message

    def display(self):
        print("\nSender:", self.sender)
        print("Subject:", self.subject)
        print("Message:", self.message)


def classify_email(email):
    subject = email.subject.lower()

    if "invoice" in subject or "payment" in subject:
        return "Finance"

    if "meeting" in subject or "schedule" in subject:
        return "Work"

    if "offer" in subject or "sale" in subject:
        return "Marketing"

    return "General"


emails = [
    Email("abc@company.com", "Invoice for September", "Please check the attached invoice."),
    Email("manager@company.com", "Team Meeting", "Meeting at 10 AM."),
    Email("store@email.com", "Special Sale Offer", "50% discount today!")
]

try:
    for email in emails:
        email.display()
        category = classify_email(email)
        print("AI Category:", category)

except Exception as e:
    print("Automation Error:", e)
