# practice-5 user role access checker

role = input("enter your role: ")
if role == "admin":
    print("full access granted.")
elif role == "dev":
    print("deployment access granted.")
elif role == "tester":
    print("testing access granted.")
else:
    print("access denied.")
