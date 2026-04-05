# DevSenseAI 🤖

An AI-powered coding assistant built with Streamlit and OpenRouter, designed to help developers with debugging, code generation, and concept explanations.

---

## Features

- **Smart prompt routing** — automatically detects whether you're asking about a bug, code, or a concept, and adjusts the system prompt accordingly
- **Streaming responses** — answers appear in real time as they're generated
- **Multi-chat support** — create and switch between multiple chat sessions in the sidebar
- **Clear chat** — reset any conversation with one click
- **Minimal UI** — clean interface with user/assistant avatars

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| LLM API | OpenRouter (`gpt-4o-mini`) |
| API Client | `openai` Python SDK |

---

## Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/devsenseai.git
   cd devsenseai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**

   Create a `.streamlit/secrets.toml` file:
   ```toml
   API_KEY = "your_openrouter_api_key_here"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## Deploying on Streamlit Cloud

1. Push your code to a public GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and create a new app
3. In **App settings → Secrets**, add:
   ```
   API_KEY = "your_openrouter_api_key_here"
   ```
4. Deploy — the app reads the key via `os.getenv("API_KEY")` automatically

> **Note:** Never commit your API key directly in `app.py` or `secrets.toml`. The secrets panel in Streamlit Cloud keeps it secure.

---

## Project Structure

```
devsenseai/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── .streamlit/
    └── secrets.toml    # API key (local only, do not commit)
```

---

## How Prompt Routing Works

The app inspects your input and selects a system prompt before sending to the model:

| Keyword detected | Behaviour |
|---|---|
| `error`, `bug`, `debug` | Activates debugging assistant persona |
| `code` | Activates coding assistant persona |
| `explain` | Activates teacher/explainer persona |
| *(anything else)* | General coding assistant |

---
