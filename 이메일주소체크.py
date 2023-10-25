#이메일주소 체크.py

import re

def is_valid_email(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(pattern, email)

# Sample email addresses
sample_emails = [
    "user@example.com",
    "john.doe123@email.co.uk",
    "jane.doe@email.org",
    "contact@subdomain.domain.co",
    "my.email@123.net",
    "user@domain.io",
    "test.email@example.com",
    "invalid.email@.com",
    "noatsymbol.com",
    "missing@dotcom"
]

for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
