import socket
import threading
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Prompt user for language code (e.g., en, hi, fr, es)
print("Welcome to Simple Chat Translator!")
print("Type the language code you want messages translated to (e.g., 'en' for English, 'fr' for French, 'hi' for Hindi):")
target_language = input("Enter language code: ").strip().lower()

# Function to receive messages
def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            translated = translator.translate(data, dest=target_language).text
            print(f"\n[Translated]: {translated}")
        except:
            print("❌ Connection closed by server.")
            break

# Create socket connection to server
host = '127.0.0.1'  # Replace with actual IP if needed
port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Start the thread to receive messages
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Loop to send messages
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        client_socket.close()
        break
    client_socket.send(message.encode())

