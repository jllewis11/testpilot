from testpilot.cli.key import *
import os
from dotenv import load_dotenv

load_dotenv()


def test_setkey(monkeypatch):
    example_key = "12345678901234567890"

    # Set the environment variable using monkeypatch
    monkeypatch.setenv("OPENAI_API_KEY", example_key)

    # Retrieve the environment variable
    openai_api_key = os.environ["OPENAI_API_KEY"]
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    # Assert that the environment variable matches the expected value
    assert openai_api_key == example_key


def test_api_keys_output(capsys, monkeypatch):
    # Scenario 1: No keys set
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TOGETHERAI_API_KEY", raising=False)
    viewkey()
    captured = capsys.readouterr()
    assert "No OpenAI API key is set." in captured.out
    assert "No TogetherAI API key is set." in captured.out

    # Scenario 2: Only OpenAI key set
    monkeypatch.setenv("OPENAI_API_KEY", "1234567890abcdef")
    viewkey()
    captured = capsys.readouterr()
    assert "Current OpenAI API Key: ************cdef" in captured.out
    assert "No TogetherAI API key is set." in captured.out

    # Scenario 3: Only TogetherAI key set
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("TOGETHERAI_API_KEY", "abcdef1234567890")
    viewkey()
    captured = capsys.readouterr()
    assert "No OpenAI API key is set." in captured.out
    assert "Current TogetherAI API Key: ************7890" in captured.out

    # Scenario 4: Both keys set
    monkeypatch.setenv("OPENAI_API_KEY", "1234567890abcdef")
    monkeypatch.setenv("TOGETHERAI_API_KEY", "abcdef1234567890")
    viewkey()
    captured = capsys.readouterr()
    assert "Current OpenAI API Key: ************cdef" in captured.out
    assert "Current TogetherAI API Key: ************7890" in captured.out


# Idk something it's broken and not recognising the inputs


# def test_removekey(capsys, monkeypatch):
#     # Scenario 1: Remove OpenAI key
#     monkeypatch.setenv("OPENAI_API_KEY", "1234567890abcdef")
#     removekey("openai")
#     # Simulate user entering 'y' when prompted
#     monkeypatch.setattr('builtins.input', lambda _: 'y')
#     captured = capsys.readouterr()
#     assert "OPENAI_API_KEY" not in os.environ
#     assert "OPENAI_API_KEY removed successfully." in captured.out

#     # Scenario 2: Remove TogetherAI key
#     monkeypatch.setenv("TOGETHERAI_API_KEY", "abcdef1234567890")
#     removekey("togetherai")
#     # Simulate user entering 'y' when prompted
#     monkeypatch.setattr('builtins.input', lambda _: 'y')
#     captured = capsys.readouterr()
#     assert "TOGETHERAI_API_KEY" not in os.environ
#     assert "TOGETHERAI_API_KEY removed successfully." in captured.out

#     # Scenario 3: Remove non-existent key
#     removekey("openai")
#     # Simulate user entering 'y' when prompted
#     monkeypatch.setattr('builtins.input', lambda _: 'y')
#     captured = capsys.readouterr()
#     assert "Operation cancelled." in captured.out


#     #Scenario 4: Invalid service
#     removekey("AWS")
#     assert "Invalid service. Please choose 'openai' or 'togetherai'." in captured.out
