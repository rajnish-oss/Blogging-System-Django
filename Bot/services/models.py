import time
from ollama import Client
import os
import dotenv
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

dotenv.load_dotenv()



async def agentic_bot(page_content, context,user_input,past_quetion):
    from Bot.consumers import MyConsumer

    client = client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": "Bearer " + os.environ.get("OLLAMA_KEY", "")
            },
        )
    socket = MyConsumer()

    print(user_input)

    prompt = f"""
        You are a helper chatbot of article website.

        This is the page content: {page_content}

        This is the past chat context: {context}

        These are past question user asked (giving this to you for better memmory): {past_quetion}
        """

    messages = [
    {
        "role": "system",
        "name": "planner",
        "content": str(prompt),
    },
    {
        "role": "user",
        "content": user_input,
    },
    ]
    

    try:
        response = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            stream=False,
        )
    except Exception as e:
        print("Error:", e)

    print(response)

    return response

    res = response.get("message")
    return res.get("content")

    interaction_id = None
    last_event_id = None
    

    channel_layer = get_channel_layer()

    # Send message to the group "bot_updates"
    await channel_layer.group_send(
        "bot_updates", 
        {
            "type": "bot.message", # This matches the method name 'bot_message'
            "message": res.content,
        }
    )

        # if chunk.event_type == "interaction.start":
        #     interaction_id = chunk.interaction.id
        #     print(f"Interaction started: {interaction_id}")

        # if chunk.event_id:
        #     last_event_id = chunk.event_id

        # if chunk.event_type == "content.delta":
        #     if chunk.delta.type == "text":
        #         print(chunk.delta.text, end="", flush=True)
        #     elif chunk.delta.type == "thought_summary":
        #         print(f"Thought: {chunk.delta.content.text}", flush=True)

        # elif chunk.event_type == "interaction.complete":
        #     print("\nResearch Complete")