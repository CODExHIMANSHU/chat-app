import asyncio
import websockets
import json
import os

connected_users = set()
MESSAGE_FILE = "server/database/messages.json"  # Fixed typo: databse → database

def load_messages():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            return json.load(f)
    return []  # Fixed: this was indented inside the if block before — now it always returns []

def save_message(sender, text):
    messages = load_messages()
    messages.append({"sender": sender, "text": text})
    with open(MESSAGE_FILE, "w") as f:
        json.dump(messages, f)

async def handle_message(websocket):
    connected_users.add(websocket)

    # Phase 6: First message from client = username
    username = await websocket.recv()
    print(f"[+] {username} connected! Total: {len(connected_users)}")

    try:
        async for message in websocket:
            print(f"Message from {username}: {message}")

            # Save to file
            save_message(username, message)

            # Attach username and broadcast to everyone else
            full_message = f"{username}: {message}"
            for user in connected_users:
                if user != websocket:
                    await user.send(full_message)

    finally:
        connected_users.remove(websocket)
        print(f"[-] {username} disconnected! Total: {len(connected_users)}")

async def main():
    server = await websockets.serve(handle_message, "localhost", 8765)
    print("Server started on port 8765!")
    await server.wait_closed()

asyncio.run(main())