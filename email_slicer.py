print("✉️ Email Slicer\n")

email = input("Enter your email address: ").strip()

if "@" in email and "." in email:
    username, domain_part = email.split("@", 1)

    if "." in domain_part:
        domain, extension = domain_part.rsplit(".", 1)

        print("\n📊 Email Details")
        print(f"Username  : {username}")
        print(f"Domain    : {domain}")
        print(f"Extension : {extension}")
    else:
        print("❌ Invalid email format")
else:
    print("❌ Invalid email format")
