import base64
import json
import os
import asyncio

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel

class Balances(BaseModel):
    login_status: str
    credit_card_number: str
    credit_card_amount_due: str
    ppf_account_interest_rate: str
    ppf_account_balance: str

bwController = Controller(output_model=Balances)

def save_screenshot(base64_string, output_filename="screenshot.png"):
    """Decodes a base64 string and saves it as an image file."""
    img_data = base64.b64decode(base64_string)
    with open(output_filename, "wb") as f:
        f.write(img_data)
    return output_filename

async def sitevalidation() :
    os.environ['GOOGLE_API_KEY'] = ''

    task = (
        'Important : I am UI Automation Tester validating the tasks'
        'Open website url - https://preview--smooth-service-solution.lovable.app/login'
        'login with username - keerthi and password - Test@1234'
        'Validate if the login is successful and dashboard is loaded'
        'Navigate to website url - https://preview--smooth-service-solution.lovable.app/cards-loans/credit-cards'
        'Click on Pay Bill link'
        'Select the primary credit card and pay the total amount due'
        'Navigate to website url - https://preview--smooth-service-solution.lovable.app/bank-accounts/ppf-account'
        'Make sure Intrest rate is greater than 5%'
        'Make sure the balance is greater than 10000'
        'Close the browser'
    )
    googleApiKey = SecretStr(os.environ['GOOGLE_API_KEY'])
    googleLlmModel = 'gemini-2.0-flash-exp'

    llm = ChatGoogleGenerativeAI(model=googleLlmModel,api_key=googleApiKey)
    agent = Agent(task=task, llm=llm, controller=bwController, use_vision=True)
    history = await agent.run()
    print("Test is completed without assertion")
    print("Test has executed for " + str(history.total_duration_seconds()) + " seconds")
    history.save_to_file(filepath='./test_history.json')
    result = history.final_result()

    print("Test Results:")
    print("#############")
    print("result: " + str(result))

    try:
        jsonResult = json.loads(result)
        bwResult=Balances(**jsonResult)
        print("Login Status :" + str(bwResult.login_status))
        print("Credit Card Amount Due :" + str(bwResult.credit_card_amount_due))
        print("Credit Card Number :" + str(bwResult.credit_card_number))
        print("PPF Account Interest Rate :" + str(bwResult.ppf_account_interest_rate))
        print("PPF Account Balance :" + str(bwResult.ppf_account_balance))
    except json.JSONDecodeError as e:
        print("Error decoding JSON: ", e)

    # Print the errors
    errors = history.errors()
    if errors:
        print("Errors:")
        for error in errors:
            print(error)
    else:
        print("No errors found.")

    # Save the screenshots
    screenshots = history.screenshots()
    counter=1
    for screenshot in screenshots:
        # Storing screenshots after decoding
        # TODO:- Get from the history object, so we can stick url
        # to the screenshot
        save_screenshot(screenshot, output_filename=f"screenshot_{counter}.png")
        counter+=1

asyncio.run(sitevalidation())