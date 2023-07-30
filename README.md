Claude Flask API
This is an unofficial Flask API wrapper for the Claude AI assistant. It provides endpoints for creating chats, sending messages, and retrieving chat history.

Author
This Flask API was created by Ali Benali.

Endpoints
Create New Chat
Copy code

POST /api/chats/new_chat
Creates a new chat with Claude and returns the chat UUID.

Request body:

json

Copy code

{
  "name": "My Chat"
}
Response:

json

Copy code

{
  "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b"  
}
Get All Chats
Copy code

GET /api/chats/
Returns a list of all chats.

Response:

json

Copy code

[
  {
    "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b",
    "name": "My First Chat"
  },
  {
    "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b", 
    "name": "My Second Chat"
  } 
]
Get Single Chat
Copy code

GET /api/chats/82e76459-1e8d-4618-afb4-b9c1d0ef242b
Returns a single chat by UUID.

Response:

json

Copy code

{
  "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b",
  "name": "My Chat",
  "messages": [
    {"from": "user", "text": "Hi Claude!"},
    {"from": "claude", "text": "Hello!"}
  ]
}
Append Message to Chat
Copy code

POST /api/chats/send_message
Sends a new message to a chat.

Request body:

json

Copy code

{
  "message": "Hello Claude, how are you?",
  "chat_uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b"
}
Response:

json

Copy code

{
  "success": true
}
Error response if chat UUID is invalid:

json

Copy code

{
  "error": 404
}
