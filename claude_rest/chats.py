import requests, uuid
import config.development as config

class claudeREST():
    def __init__(self):
        self.base_url = config.CLAUDE_URL
        self.claude_api = config.CLAUDE_API
        self.session = requests.Session()
        self.headers = {"cookie": f"sessionKey={config.SESSION_KEY};",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

    def create_chat(self, name):
        url = f'{self.base_url}/chat_conversations'
        data = {
            "uuid": str(uuid.uuid4()),
            "name": name,
        }
        try:
            response = self.session.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return str(e)
    
    def get_chats(self):
        url = f'{self.base_url}/chat_conversations'
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Raise exception for 4xx or 5xx errors
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return str(e)
        
    def get_chat(self,chat_uuid):
        url = f'{self.base_url}/chat_conversations/{chat_uuid}'
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Raise exception for 4xx or 5xx errors
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return str(e)
        
    def append_message(self, message, chat_uuid):
        url = f"{self.claude_api}/append_message"
        data = {
            "completion": {
                "prompt": message,
                "timezone": "Africa/Lagos",
                "model": "claude-2",
                "incremental": True
            },
            "organization_uuid": config.ORGANIZATION_UID,
            "conversation_uuid": chat_uuid,
            "text": message,
            "attachments": []
        }
        try:
            response = self.session.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            return str(e)