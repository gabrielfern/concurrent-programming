# Com base em http://curio.readthedocs.org/en/latest/tutorial.html
import asyncio
from random import randint


@asyncio.coroutine
def countdown(name, time):
    while time > 0:
        print(name, '==>', time)
        yield from asyncio.sleep(1)
        time -= 1


loop = asyncio.get_event_loop()

tasks = [  
    asyncio.ensure_future(countdown('A', randint(2, 6))),
    asyncio.ensure_future(countdown('B', randint(2, 6)))
]

loop.run_until_complete(asyncio.wait(tasks))  
loop.close() 
