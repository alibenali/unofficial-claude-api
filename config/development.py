import os
from dotenv import load_dotenv

load_dotenv()

# Development configuration
DEBUG = True
ORGANIZATION_UID = "0e3fb36e-b00f-40c2-98dd-6488fc8f9968"
CLAUDE_URL = f"https://claude.ai/api/organizations/{ORGANIZATION_UID}"
CLAUDE_API = f"https://claude.ai/api"
SESSION_KEY = os.environ['SESSION_KEY']
