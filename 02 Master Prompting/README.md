# Prompting Techniques using LLMs

This project showcases different prompting techniques using LLM APIs like OpenAI's GPT and Google's Gemini. The core focus is to demonstrate how zero-shot, few-shot, and chain-of-thought prompting strategies can be implemented in Python.

## 📁 Project Structure

```
.
├── zero_shot_prompting.py
├── few_shot_prompting.py
├── chain_of_thoughts.py
└── gemini_chat.py
```

## 🧠 Prompting Techniques

### 1. `zero_shot_prompting.py`
- Uses OpenAI's GPT model with no prior examples.
- Sends a single query to the model (e.g., "What is the capital of Karnataka").
- Demonstrates how GPT responds without any specific context or samples.

### 2. `few_shot_prompting.py`
- Provides multiple examples to guide the model's behavior.
- Restricts the model to only answer questions related to **Indian geography and history**.
- Humorous and informative responses are encouraged for out-of-domain queries.

### 3. `chain_of_thoughts.py`
- Implements step-by-step reasoning by simulating multiple thinking stages:
  - **Analyse**, **Think**, **Output**, **Validate**, and **Result**.
- Expects a structured JSON response after each step.
- Demonstrates iterative, logical breakdown of a user query.

### 4. `gemini_chat.py`
- Uses **Google Gemini 2.0 Flash** model via API.
- Simple prompt: “What is Kolar famous for?”
- Demonstrates usage of Gemini for content generation.

## 🛠️ Requirements

- Python 3.7+
- `.env` file with API keys for OpenAI and Gemini:
  ```
  OPENAI_API_KEY=your_openai_key
  GEMINI_API_KEY=your_gemini_key
  ```

Install dependencies:
```bash
pip install openai python-dotenv google-generativeai
```

## 🚀 How to Run

```bash
python zero_shot_prompting.py
python few_shot_prompting.py
python chain_of_thoughts.py
python gemini_chat.py
```

Make sure you have valid API keys set up in the `.env` file before running the scripts.

## 📌 Notes

- `chain_of_thoughts.py` is interactive and expects user input via console.
- The outputs are printed directly to the terminal.
- All scripts use `gpt-4o-mini-2024-07-18` or `gemini-2.0-flash-001` models.

## 📃 License

This project is for educational and demonstration purposes.
