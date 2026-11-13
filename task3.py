
import re

def analyze_email(email):
    risk_score = 0
    warnings = []

    urgent_words = [
        "urgent", "immediately", "act now",
        "account suspended", "verify now",
        "limited time", "login immediately"
    ]

    for word in urgent_words:
        if word in email.lower():
            risk_score += 1
            warnings.append(f"Urgent language detected: {word}")

    urls = re.findall(r'https?://\S+|www\.\S+', email)

    if urls:
        risk_score += 2
        warnings.append("Email contains links. Verify their destination.")

    sensitive_words = [
        "password", "otp", "bank details",
        "credit card", "pin", "social security"
    ]

    for word in sensitive_words:
        if word in email.lower():
            risk_score += 2
            warnings.append(f"Sensitive information requested or mentioned: {word}")

    print("\n----- EMAIL RISK REPORT -----")

    if risk_score >= 4:
        print("Risk Level: HIGH")
    elif risk_score >= 2:
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: LOW")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("No obvious suspicious patterns detected.")

    print("\nTotal Risk Score:", risk_score)

email_content = input("Enter email content:\n")
analyze_email(email_content)
