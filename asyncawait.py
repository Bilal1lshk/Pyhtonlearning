import asyncio

async def hello():
   await  asyncio.gather(asyncio.sleep(1), print("Hello"))

asyncio.run(hello())