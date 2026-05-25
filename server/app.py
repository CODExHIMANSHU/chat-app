import asyncio
import websockets

connected_users = set()

async def handle_message(websocket):
    connected_users.add(websocket)
    print("User connected! Total:", len(connected_users))
    try:
        async for message in websocket:
            print("Message received:", message)
            for user in connected_users:
                if user != websocket:
                    await user.send(message)
    finally:
        connected_users.remove(websocket)
        print("User disconnected! Total:", len(connected_users))

async def main():
    server = await websockets.serve(handle_message, "localhost", 8765)
    print("Server started on port 8765!")
    await server.wait_closed()

asyncio.run(main())