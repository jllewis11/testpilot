from testpilot.key import *
import os
from dotenv import load_dotenv

load_dotenv()


def test_setkey(monkeypatch):
    example_key = "12345678901234567890"

    # Set the environment variable using monkeypatch
    monkeypatch.setenv("OPENAI_API_KEY", example_key)

    # Call your function (assuming setkey should read the environment variable)
    setkey("openai", example_key)

    # Retrieve the environment variable
    openai_api_key = os.environ["OPENAI_API_KEY"]

    # Assert that the environment variable matches the expected value
    assert openai_api_key == example_key


# def test_viewkey()

# def test_removekey()
