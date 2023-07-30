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
    "created_at": "2023-07-26T17:13:56.627609+00:00",
    "name": "Simple Backtrader Python Script",
    "summary": "",
    "updated_at": "2023-07-26T21:44:33.799410+00:00",
    "uuid": "1060b564-b8ad-4f73-8450-cb2643102ed8"
  },
  {
    "created_at": "2023-07-19T15:05:25.384935+00:00",
    "name": "QR art generator in Python",
    "summary": "",
    "updated_at": "2023-07-19T15:14:12.086136+00:00",
    "uuid": "82e76459-1e8d-4618-afb4-b9c1d0ef242b"
  },
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
  "chat_messages": [
    {
      "attachments": [],
      "chat_feedback": null,
      "created_at": "2023-07-30T16:40:20.978118+00:00",
      "edited_at": null,
      "index": 0,
      "sender": "human",
      "text": "Hi",
      "updated_at": "2023-07-30T16:40:20.978118+00:00",
      "uuid": "84989bbc-8f78-4b85-b32b-98fb46f2c5d9"
    },
    {
      "attachments": [],
      "chat_feedback": null,
      "created_at": "2023-07-30T16:40:21.048643+00:00",
      "edited_at": null,
      "index": 1,
      "sender": "assistant",
      "text": "Hello! My name is Claude.",
      "updated_at": "2023-07-30T16:40:21.048643+00:00",
      "uuid": "2b8464c0-835d-484f-a09a-bb9963dea265"
    }
  ],
  "created_at": "2023-07-30T16:40:19.799679+00:00",
  "name": "\ud83d\udcac Hi",
  "summary": "",
  "updated_at": "2023-07-30T16:40:21.048643+00:00",
  "uuid": "4ad6155b-751c-44a4-a06e-390edc718b0b"
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

Error response:

```json 
{
  "error": "Error message."
}
```
