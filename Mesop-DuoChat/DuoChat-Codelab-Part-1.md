# Mesop DuoChat Codelab[¶](https://google.github.io/mesop/codelab/#mesop-duochat-codelab)

This tutorial walks you through building DuoChat, an interactive web application for chatting with multiple AI models simultaneously. You'll learn how to leverage Mesop's powerful features to create a responsive UI and integrate with AI APIs like Google Gemini and Anthropic Claude.

### What you will build[¶](https://google.github.io/mesop/codelab/#what-you-will-build)

By the end of this codelab, you will build [DuoChat (demo)](https://huggingface.co/spaces/wwwillchen/mesop-duo-chat) that will allow users to:

- Select multiple AI models to chat with
- Compare responses from different models side-by-side
- Provide their own API keys

If you want to dive straight into the code, you can look at the [DuoChat repo](https://github.com/wwwillchen/mesop-duo-chat) and each branch represents the completed code after each section.

### Setting Up the Development Environment[¶](https://google.github.io/mesop/codelab/#setting-up-the-development-environment)

Let's start by setting up our development environment:

1. Create a new directory for your project:

```
mkdir duochat
cd duochat
```

1. Follow the [Mesop command-line installation guide](https://google.github.io/mesop/getting-started/installing/#b-command-line) and create a [virtual environment](https://google.github.io/mesop/getting-started/installing/#create-a-venv-environment) and activate it.
2. Create a `requirements.txt` file with the following content:

```
mesop
gunicorn
anthropic
google-generativeai
```

1. Install the dependencies:

```
pip install -r requirements.txt
```

### Setting Up the Main Application[¶](https://google.github.io/mesop/codelab/#setting-up-the-main-application)

Let's start by creating a basic Mesop application. Create `main.py` and add the following code:

**main.py**

```
import mesop as me

@me.page(path="/")
def page():
    me.text("Welcome to DuoChat!")
```

This creates a simple Mesop application with a welcome message.

### Running the Application[¶](https://google.github.io/mesop/codelab/#running-the-application)

To run your Mesop application:

```
mesop main.py
```

Navigate to `http://localhost:32123` in your web browser. You should see the welcome message.

### Getting API keys[¶](https://google.github.io/mesop/codelab/#getting-api-keys)

Later on, you will need API keys to call the respective AI models:

- [Get a Google Gemini API Key](https://ai.google.dev/gemini-api/docs/api-key) and use the Gemini API [free tier](https://ai.google.dev/pricing).
- [Get an Anthropic API Key](https://docs.anthropic.com/en/docs/quickstart#prerequisites) and setup billing. Check their docs for pricing.

> TIP: You can get started with the Gemini API key, which has a free tier, first and create the Anthropic API key later.

### Troubleshooting[¶](https://google.github.io/mesop/codelab/#troubleshooting)

If you're having trouble, compare your code to the [solution](https://github.com/wwwillchen/mesop-duo-chat/tree/1_completed).