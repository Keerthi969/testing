import os
import asyncio

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr


async def siteValidation() :
    os.environ['GOOGLE_API_KEY'] = ''

    task = (
        'Important : I am UI Automation Tester validating the tasks'
        'Open website url - https://rahulshettyacademy.com/loginpagePractise'
        'Login with username and password. login details are available in the login page'
        'After login, select first 2 products and add them to cart'
        'Then checkout the products and store the total value you see in the screen'
        'Increase the quantity of the first product by 2 and check if the total value is updated accordingly'
        'Checkout, select country and agree to the terms and complete purchase'
        'verify the purchase is successful by checking the thankyou message'
    )
    googleApiKey = SecretStr(os.environ['GOOGLE_API_KEY'])
    googleLlmModel = 'gemini-2.0-flash-exp'

    llm = ChatGoogleGenerativeAI(model=googleLlmModel,api_key=googleApiKey)
    agent = Agent(task=task, llm=llm, use_vision=True)
    history = await agent.run()
    print("Test is completed without assertion")
    print(history.final_result())

asyncio.run(siteValidation())