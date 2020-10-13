
from rasa.core.agent import Agent
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import asyncio






app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.get('/')
async def load_agent():
    model_path = "C:/Users/Gopi/Desktop/rasa/rasa_2_version/models/20201010-155216.tar.gz"
    agent =  Agent.load(model_path)
    agent_reply = await agent.handle_text('hello')
    print(agent)
    print(agent_reply)
    return agent_reply




