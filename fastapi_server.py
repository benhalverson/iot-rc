from fastapi import FastAPI, WebSocket
import asyncio
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print('websocket connected')

    try:
        while True:
            data = await websocket.receive_json()

            right_trigger = data.get('right_trigger', 0.0)
            left_axis = data.get('left_axis', 0.0)

            if right_trigger > 0.0:
                print(f'Right Trigger: {right_trigger}')
            if left_axis != 0.0:
                print(f'Left Axis: {left_axis}')

            return data
    except:
        await websocket.close()
        print('websocket disconnected')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

