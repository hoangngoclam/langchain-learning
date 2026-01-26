## How to run

First, you should install the uv first, follow this install link: https://docs.astral.sh/uv/getting-started/installation/

setup the environment
```sh
cp .env.example .env
```
add the openapi, tavily, langsmith keys to the .env file

To run the example script with uv:

```sh
uv venv
source .venv/bin/activate
uv sync
uv run search-agent.py
```
