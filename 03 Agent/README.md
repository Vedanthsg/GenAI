# 🤖 Simple Groq Agent

This folder contains a minimal example of an LLM-powered agent that can plan steps and call tools. It uses Groq's API with a Llama model to reason about a user query and decide which function to execute.

## Features

- Plans step by step before executing tools
- Built-in tools:
  - `get_weather(city)` – fetches current weather via `wttr.in`
  - `run_command(cmd)` – executes a shell command
- Waits for the observation from each tool before producing the final answer

## Requirements

- Python 3.8+
- `groq` and other dependencies from `requirements.txt`
- Environment variable `GROQ_API_KEY` in a `.env` file

## Usage

```bash
python agent.py
```

Type a question or command at the prompt. The agent will plan, call the appropriate tool and return the result.
