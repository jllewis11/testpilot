from testpilot.key import *
import os
from dotenv import load_dotenv

load_dotenv()


def test_setkey():
    example_key = "12345678901234567890"
    setkey("openai", example_key)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    assert openai_api_key == example_key


# def test_viewkey()

# def test_removekey()
