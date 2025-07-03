# Groq + Gradio Chat Example

[Gradio](https://gradio.app) is a powerful library for creating web interfaces for your applications that enables you to quickly build interactive demos for your fast Groq apps with features such as:

- **Interface Builder:** Create polished UIs with just a few lines of code, supporting text, images, audio, and more
- **Interactive Demos:** Build demos that showcase your LLM applications with multiple input/output components
- **Shareable Apps:** Deploy and share your Groq-powered applications with a single click

This repository is a lightweight example demonstrating how to build a chatbot interface using Gradio with Groq's API for fast AI inference.

## Overview

This is a simple chat application that shows how to integrate Groq's API with Gradio to create a web-based AI chatbot. The example uses the Llama 3.3 70B model and provides a clean interface for chatting with the AI.

**Features:**
- Simple web chat interface powered by Gradio
- Integration with Groq API for AI responses
- Pre-configured example prompts
- Easy to customize and extend
- Fast response times with Groq's inference

## Architecture

**Tech Stack:**
- **Frontend:** Gradio web interface
- **AI API:** Groq with Llama 3.3 70B Versatile
- **Backend:** Python with groq-gradio integration
- **Package Management:** UV

## Quick Start

### Prerequisites
- Python 3.12+
- UV package manager ([Install UV](https://docs.astral.sh/uv/getting-started/installation/))
- Groq API key ([Get one here](https://console.groq.com/keys))

### Setup

1. **Clone the repository**
   ```bash
   gh repo clone janzheng/groq-gradio-template
   cd groq-gradio-template
   ```

2. **Install dependencies**
   ```bash
   uv sync  # Creates .venv and installs dependencies
   ```

3. **Create a `.env` file** with your API key:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   ```

4. **Run the application**
   ```bash
   uv run main.py
   ```

5. **Open your browser** to the URL shown in the terminal (usually `http://127.0.0.1:7860`)

## Usage

- Click the example prompts to try them out
- Type your own questions in the chat input
- The AI will respond using Groq's API

## Customization

### Change the Model
Update the model name in `main.py`:
```python
gr.load(
    name="llama-3.1-8b-instant",  # Different model
    src=groq_gradio.registry,
    # ... rest of config
)
```

### Update the Interface
Modify the title, description, and examples:
```python
gr.load(
    name="llama-3.3-70b-versatile",
    src=groq_gradio.registry,
    title="My Custom Chatbot",
    description="A simple AI assistant.",
    examples=[
        "What's the weather like?",
        "Tell me a joke",
    ],
).launch()
```

## Available Models

Common Groq models you can use:
- `llama-3.1-8b-instant`
- `llama-3.3-70b-versatile`
- `meta-llama/llama-4-scout-17b-16e-instruct`
- `meta-llama/llama-4-maverick-17b-128e-instruct`
- Full list of [Groq models here](https://console.groq.com/docs/models) 

## Environment Setup

Make sure your `.env` file contains:
```env
GROQ_API_KEY=your-actual-api-key
```

## Deployment

This example can be deployed to:
- Local development (default)
- Hugging Face Spaces
- Any Python hosting service
- Docker containers

## Troubleshooting

**Common issues:**
- Missing API key: Check your `.env` file
- Module not found: Run `uv pip install groq-gradio`
- Port in use: Add `server_port=7861` to the `.launch()` call

## Next Steps

- Get your Groq API key at [console.groq.com](https://console.groq.com)
- Check out [Gradio docs](https://gradio.app/docs/) for UI customization
- Explore other Groq models and capabilities
- Join the [Groq community](https://community.groq.com) for support

## License

MIT License - see LICENSE file for details.

## Credits

Built with Groq API and Gradio.