import websockets
import asyncio
import picar_4wd as fc
import time


speed = 20
distance = 0
fc.start_speed_thread()

async def handler(websocket):
    global speed,distance
    async for message in (websocket):
        if message == "forward":
            fc.stop()
            fc.forward(speed)
        elif message == "backward":
            fc.stop()
            fc.backward(speed)
        elif message == "left":
            fc.stop()
            fc.turn_left(speed)
        elif message == "right":
            fc.stop()
            fc.turn_right(speed)
        elif message == "stop":
            fc.stop()
        elif message.startswith("#"):
            print("Text recieved from client : ",message[1:])
        elif message == "query":
            b = round(fc.utils.power_read(),2)
            t = round(fc.utils.cpu_temperature(),2)
            s = round(fc.speed_val(),2)
            distance+= round(s*0.1,2)
            #print(b,t,s,distance)
            await websocket.send(str(s)+","+str(distance)+","+str(t)+","+str(b))

async def main():
    async with websockets.serve(handler,"172.16.109.23",8564):
        await asyncio.Future()

asyncio.run(main())
