# AI-103 Section Code

Small Python examples for calling an Azure-hosted OpenAI-compatible model.

## Requirements

- Python 3.13 or later
- An Azure AI endpoint, a deployed model, and an API key

## Setup

Install the project dependencies:

```bash
python3 -m pip install openai python-dotenv
```

Create your local environment file from the template:

```bash
cp .env.example .env
```

Set these values in `.env`:

| Variable | Description |
| --- | --- |
| `AZURE_OPENAI_ENDPOINT` | Azure endpoint base URL, such as `https://<resource>.services.ai.azure.com/openai/v1` |
| `AZURE_OPENAI_DEPLOYMENT` | Name of the deployed model to call |
| `AZURE_OPENAI_API_KEY` | API key for the Azure endpoint |

`.env` is ignored by Git. Keep credentials there and never commit them. If a key has been exposed, revoke it and create a replacement.

## Run an example

Run a script from this directory, for example:

```bash
python3 01_first_api_call.py
```

The examples are:

- `01_first_api_call.py` - basic response
- `02_model_behaviour.py` - instructions and model behavior
- `03_reasoning.py` - reasoning effort
- `04_multi_modal.py` - image input; requires `Agent_types.png` in this directory
- `05_web_search.py` - web search
- `06_code_interpreter.py` - code interpreter
