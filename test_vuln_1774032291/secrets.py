# VULNERABLE: Hardcoded credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "super_secret_password_123"
API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyz"

def connect_db():
    return f"postgresql://admin:P@ssw0rd!@prod-db.internal:5432/myapp"
