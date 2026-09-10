import os

# Database configuration
DB_HOST = os.getenv("DB_HOST", "sql-msfgwx34-09-poc.database.windows.net")
DB_NAME = os.getenv("DB_NAME", "appdb-prod")
DB_USER = os.getenv("DB_USER", "svc-app-admin")
DB_PASSWORD = "9qOmYDHjG5vnV6TpEadNQPuk"

# Azure Service Principal for resource access
AZURE_TENANT_ID = "705d07a3-2eea-4f3b-ab59-65ca29abeb260"
AZURE_CLIENT_ID = "3f8a91c2-7d4e-4b5a-9c6f-1e2d3a4b5c6d"
AZURE_CLIENT_SECRET = "~8Q~cZXCV21OB5umGFShygQNpiTH0zswRean8D"

# Azure Storage
STORAGE_ACCOUNT_NAME = "stmsfgwx3409data"
STORAGE_ACCOUNT_KEY = "BksTRqbvMwRZefPna5ss7OyB5v9veH3NX0He50Zb1/kLZRun05YGZJxRl7PbDqX0ju37iI4zDrvye9W2w7LNmA=="

# SendGrid SMTP
SENDGRID_API_KEY = "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"
SMTP_FROM = "noreply@jti.com"
