from isend import ISend

client = ISend("API_KEY")

email_response = client.send_email(
    "WelcomeTemplate",
    "user@example.com",
    {"name": "John"}
)
print("Email Response:", email_response)

event_response = client.send_event(
    "Signup",
    "user@example.com",
    {"plan": "Free"}
)
print("Event Response:", event_response)
