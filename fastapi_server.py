from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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
        while True:
            data = await websocket.receive_json()
            print('Data received:', data)

            right_trigger = data.get('right_trigger', 0.0)
            left_axis = data.get('left_axis', 0.0)

            print(f'Right Trigger: {right_trigger}, Left Axis: {left_axis}')

            # Send acknowledgment back to the client
            await websocket.send_json({"message": "Data received", "right_trigger": right_trigger, "left_axis": left_axis})

    except WebSocketDisconnect as e:
        print(f'WebSocket disconnected: {e.code}')
    except Exception as e:
        print(f'Unexpected WebSocket error: {e}')
    finally:
        print('Cleaning up WebSocket connection...')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0" , port=8000)