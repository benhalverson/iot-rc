from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosed
import uvicorn


import asyncio
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print('WebSocket connected')


    try:
        # send "Connection established" message to client
        await websocket.send_text("Connection established!")
        
        # await for messages and send messages
        while True:
            msg = await websocket.receive_text()
            if msg.lower() == "close":
                await websocket.close()
                break
            else:
                print(f'CLIENT says - {msg}')
                await websocket.send_text(f"Your message was: {msg}")
                
    except (WebSocketDisconnect, ConnectionClosed):
        print("Client disconnected")
    # try:
    #     while True:
    #         data = await websocket.receive_json()
    #         print('Data received:', data)

    #         right_trigger = data.get('right_trigger', 0.0)
    #         left_axis = data.get('left_axis', 0.0)

    #         print(f'Right Trigger: {right_trigger}, Left Axis: {left_axis}')

    #         await websocket.receive_text({"message": "Data received", "right_trigger": right_trigger, "left_axis": left_axis})

    # except WebSocketDisconnect as e:
    #     print(f'WebSocket disconnected: {e.code}')
    #     await asyncio.sleep(0.5)
    # except Exception as e:
    #     print(f'WebSocket disconnected: {e.code} - Reason: {getattr(e, "reason", "Unknown")}')
    #     await asyncio.sleep(0.5)

    # finally:
    #     print('Cleaning up WebSocket connection...')
    #     await asyncio.sleep(0.5)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0" , port=8000, log_level="debug")