# 🗣️ Simple Chat Translator

A Python-based multi-client chat system with **real-time translation** using Google Translate. Demonstrates socket programming, threading, and API integration.


## 🚀 Features

- 📡 **Client–Server chat** using Python’s `socket` module  
- 🌍 **Live translation** of messages via `googletrans`  
- 🧑‍🤝‍🧑 Supports **multiple clients** concurrently  
- 🧠 Solid introduction to **network programming**, **threading**, and **APIs**


## 🗂️ Project Structure
<pre> ```
chat-translator/
│
├── server.py # Central chat server
├── client.py # Chat client with language prompt & translation
├── requirements.txt # Dependency list
└── README.md 
``` </pre>

## Tech Stack
- Python 3
- socket (built-in networking module)
- threading for concurrent client handling
- googletrans (Google Translate unofficial API)

## How It Works
- The server listens for incoming connections.
- Each connected client can send messages.
- Messages are translated into a preferred language using Google Translate before being displayed.
- All clients see the translated message.


## Setup & Usage
   # Clone the repo
   git clone https://github.com/yourusername/chat-translator.git
   cd chat-translator
   # Install dependencies
   pip install googletrans==4.0.0-rc1

## Running the Server
python3 server.py

## Running a Clients (in a new terminal)
python3 client.py

## Language Support
- Uses Google Translate backend via googletrans
- Clients can choose target translation language (e.g., 'en', 'fr', 'hi', 'ar')
  
## Sample Interaction
- Client A starts, chooses fr
- Client B starts, chooses en
  A sends “Bonjour!” → B sees “[Translated]: Hello!”
  B sends “How are you?” → A sees “[Translated]: Comment ça va ?”
  
## Screenshots
![Server Screenshot](chat%20translator/images/server.png)

![Client 1 Screenshot](images/client1.png)
![Client 2 Screenshot](images/client2.png)

## Future Improvements
✔️ Add logging of chat history to a file
✔️ GUI client with Tkinter or PyQt
✔️ Auto-detect sender language before translating
✔️ Deploy as a web app with Flask + WebSockets

Varsha Shabolu 
Github profile: https://github.com/varshashabolu
