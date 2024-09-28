# DuoChat Codelab Part 4: Integrating AI APIs[¶](https://google.github.io/mesop/codelab/4/#duochat-codelab-part-4-integrating-ai-apis)

In this section, we'll set up connections to Gemini and Claude, implement model-specific chat functions, and create a unified interface for interacting with multiple models simultaneously.

### Setting Up AI Model Connections[¶](https://google.github.io/mesop/codelab/4/#setting-up-ai-model-connections)

First, let's create separate files for our Gemini and Claude integrations.

Create a new file called `gemini.py`:

**gemini.py**

```
import google.generativeai as genai
from typing import Iterable

from data_model import ChatMessage, State
import mesop as me

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

def configure_gemini():
    state = me.state(State)
    genai.configure(api_key=state.gemini_api_key)

def send_prompt_pro(prompt: str, history: list[ChatMessage]) -> Iterable[str]:
    configure_gemini()
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
    )
    chat_session = model.start_chat(
        history=[
            {"role": message.role, "parts": [message.content]} for message in history
        ]
    )
    for chunk in chat_session.send_message(prompt, stream=True):
        yield chunk.text

def send_prompt_flash(prompt: str, history: list[ChatMessage]) -> Iterable[str]:
    configure_gemini()
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        generation_config=generation_config,
    )
    chat_session = model.start_chat(
        history=[
            {"role": message.role, "parts": [message.content]} for message in history
        ]
    )
    for chunk in chat_session.send_message(prompt, stream=True):
        yield chunk.text
```

Now, create a new file called `claude.py`:

**claude.py**

```
import anthropic
from typing import Iterable

from data_model import ChatMessage, State
import mesop as me

def call_claude_sonnet(input: str, history: list[ChatMessage]) -> Iterable[str]:
    state = me.state(State)
    client = anthropic.Anthropic(api_key=state.claude_api_key)
    messages = [
        {
            "role": "assistant" if message.role == "model" else message.role,
            "content": message.content,
        }
        for message in history
    ] + [{"role": "user", "content": input}]

    with client.messages.stream(
        max_tokens=1024,
        messages=messages,
        model="claude-3-sonnet-20240229",
    ) as stream:
        for text in stream.text_stream:
            yield text
```

### Updating the Main Application[¶](https://google.github.io/mesop/codelab/4/#updating-the-main-application)

Now, let's update our `main.py` file to integrate these AI models. We'll update the `page` function, add the `display_conversations` and `display_message` functions and modify the `send_prompt` function to handle multiple models and display their responses:

**main.py**

```
import mesop as me
from data_model import State, Models, ModelDialogState, Conversation, ChatMessage
from dialog import dialog, dialog_actions
import claude
import gemini

# ... (keep the existing imports and styles)

# Replace page() with this:
@me.page(
    path="/",
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
    ],
)
def page():
    model_picker_dialog()
    with me.box(style=ROOT_BOX_STYLE):
        header()
        with me.box(
            style=me.Style(
                width="min(680px, 100%)",
                margin=me.Margin.symmetric(horizontal="auto", vertical=36),
            )
        ):
            me.text(
                "Chat with multiple models at once",
                style=me.Style(font_size=20, margin=me.Margin(bottom=24)),
            )
            chat_input()
            display_conversations()

# Add display_conversations and display_message:
def display_conversations():
    state = me.state(State)
    for conversation in state.conversations:
        with me.box(style=me.Style(margin=me.Margin(bottom=24))):
            me.text(f"Model: {conversation.model}", style=me.Style(font_weight=500))
            for message in conversation.messages:
                display_message(message)

def display_message(message: ChatMessage):
    style = me.Style(
        padding=me.Padding.all(12),
        border_radius=8,
        margin=me.Margin(bottom=8),
    )
    if message.role == "user":
        style.background = "#e7f2ff"
    else:
        style.background = "#ffffff"

    with me.box(style=style):
        me.markdown(message.content)
        if message.in_progress:
            me.progress_spinner()

# Update send_prompt:
def send_prompt(e: me.ClickEvent):
    state = me.state(State)
    if not state.conversations:
        for model in state.models:
            state.conversations.append(Conversation(model=model, messages=[]))
    input = state.input
    state.input = ""

    for conversation in state.conversations:
        model = conversation.model
        messages = conversation.messages
        history = messages[:]
        messages.append(ChatMessage(role="user", content=input))
        messages.append(ChatMessage(role="model", in_progress=True))
        yield

        if model == Models.GEMINI_1_5_FLASH.value:
            llm_response = gemini.send_prompt_flash(input, history)
        elif model == Models.GEMINI_1_5_PRO.value:
            llm_response = gemini.send_prompt_pro(input, history)
        elif model == Models.CLAUDE_3_5_SONNET.value:
            llm_response = claude.call_claude_sonnet(input, history)
        else:
            raise Exception("Unhandled model", model)

        for chunk in llm_response:
            messages[-1].content += chunk
            yield
        messages[-1].in_progress = False
        yield
```

This updated code adds the following features:

1. A `display_conversations` function that shows the chat history for each selected model.
2. A `display_message` function that renders individual messages with appropriate styling.
3. An updated `send_prompt` function that sends the user's input to all selected models and displays their responses in real-time.

### Handling Streaming Responses[¶](https://google.github.io/mesop/codelab/4/#handling-streaming-responses)

The `send_prompt` function now uses Python generators to handle streaming responses from the AI models. This allows us to update the UI in real-time as the models generate their responses.

### Running the Updated Application[¶](https://google.github.io/mesop/codelab/4/#running-the-updated-application)

Run the application again with `mesop main.py` and navigate to `http://localhost:32123`. You should now be able to:

1. Select multiple AI models using the model picker dialog.
2. Enter API keys for Gemini and Claude.
3. Send prompts to the selected models.
4. See the responses from multiple models displayed simultaneously.

### Troubleshooting[¶](https://google.github.io/mesop/codelab/4/#troubleshooting)

If you're having trouble, compare your code to the [solution](https://github.com/wwwillchen/mesop-duo-chat/tree/4_completed).