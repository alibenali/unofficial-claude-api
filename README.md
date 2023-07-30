Here is the README.md with the updated UUID and author info added to the top:

# Claude Flask API

**Author**: Ali Benali

This is an unofficial Flask API wrapper for the Claude AI assistant. It provides endpoints for creating chats, sending messages, and retrieving chat history.

## Endpoints

### Create New Chat

```
POST /api/chats/new_chat  
```

Creates a new chat with Claude and returns the chat UUID.

Request body:

```json
{
  "name": "My Chat" 
}
```

Response: 

```json
{
  "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b"
}
```

### Get All Chats

```
GET /api/chats/
```

Returns a list of all chats.

Response:

```json
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
```

### Get Single Chat

``` 
GET /api/chats/82e76459-1e8d-4618-afb4-b9c1d0ef242b
```

Returns a single chat by UUID. 

Response:

```json
{
  "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b",
  "name": "My Chat",
  "messages": [
    {"from": "user", "text": "Hi Claude!"},
    {"from": "claude", "text": "Hello!"}
  ]
}
```

### Append Message to Chat  

```
POST /api/chats/send_message
```

Sends a new message to a chat.

Request body:

```json
{
  "message": "Hello Claude, how are you?", 
  "chat_uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b"  
}
```

Response: 

```json
{
  "success": true
}
```

Error response if chat UUID is invalid:

```json 
{
  "error": 404
}
```
