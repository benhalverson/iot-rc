from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosed
import uvicorn
import json


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
            data = json.loads(msg)

            left_axis = data.get('left_axis', 2)
            right_trigger = data.get('right_trigger', 2)
            if msg.lower() == "close":
                await websocket.close()
                break
            else:
                print(f'CLIENT says - {msg}')
                left_axis_rounded = round(left_axis, 2)
                right_trigger_rounded = round(right_trigger, 2)
                await websocket.send_json({"message": "Data received", "right_trigger": right_trigger_rounded, "left_axis": left_axis_rounded})
                
    except (WebSocketDisconnect, ConnectionClosed):
        print("Client disconnected")
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0" , port=8000, log_level="info")