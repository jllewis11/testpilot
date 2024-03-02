
## Pre-requisites

- Python 3 
- Poetry (https://python-poetry.org/docs/)

### LLM Service (Either one of the following)

- Openai
- Togetherai


## Setup

1. ```poetry install```
2. ```poetry shell```


- `exit` to exit the virtual environment.

## Avaliable Commands

- ```testpilot version```: View the current version of the CLI.


### Key Management
- ```testpilot setkey [service] [key]```: Set the API key for the given service.
- ```testpilot viewkey```: View the current API keys and if they are set.
- ```testpilot removekey [service]```: Remove the API key for the given service.

## Testing

- ```pytest```: Run all tests.
- ```pytest --cov=testpilot tests```: Pytest with coverage and parallel execution.

