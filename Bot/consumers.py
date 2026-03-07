# Bot/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from Bot.services.models import agentic_bot
from Bot.services.vector_db import create_vector_db, get_context,vector_db
# from Bot.services.scraping import current_page_content



class MyConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
        # self.group_name = "bot_updates"  # Or a dynamic ID from URL
        # await self.channel_layer.group_add(self.group_name, self.channel_name)
    #     data =await self.accept()
    #     print(data)

    #     await agentic_bot("", "", data)


    # # This method is called when the bot sends a message to the group
    # async def bot_message(self, event):
    #     message = event['message']
    #     await self.send(text_data=json.dumps({'message': message}))

    async def receive(self, text_data):
        # 1. Parse the JSON sent from your frontend
        data = json.loads(text_data)
        user_message = data.get('message')
        current_page = data.get('page_data')

        print(current_page)

        print(f"Frontend sent: {user_message}")
        context = get_context(user_message)
        print("context",context)

        past_quetion = []

        if(len(past_quetion) > 10):
            past_quetion.pop(0)
            past_quetion.append(user_message)
        else:
            past_quetion.append(user_message)

        # 2. Process with your bot logic
        # You can now pass the actual user message to your bot!
        bot_response = await agentic_bot(current_page, context, user_message, past_quetion)
        bot_mess = bot_response.get("message")

        # Correct (Replace 'field1', 'field2', 'field3' with the actual field names from your vector_db model)
        create_vector_db(vector_db(
            id=bot_response.get("created_at"),
            content=bot_mess.get("content"),
            source=user_message
        ))

        # 3. Send a response back to the frontend immediately
        await self.send(text_data=json.dumps({
            'message': bot_mess.get("content")
        }))
