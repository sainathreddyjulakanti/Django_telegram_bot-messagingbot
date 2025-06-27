from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TelegramUserSerializer
from rest_framework import serializers
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

class TelegramUserView(APIView):
    def post(self, request):
        username = request.data.get('username', 'Anonymous')
        serializer = TelegramUserSerializer(data={'username': username})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
# Function to handle the /start command


API_URL = 'https://rnlyw-115-97-181-25.a.free.pinggy.link/telegram/api/userdetails/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username or "Anonymous"
    data = {'username': username}

    
    try:
        response = requests.post(API_URL, data=data)
        if response.status_code == 201:
            await update.message.reply_text(f"Hello, {username}! You've been registered.")
        else:
            await update.message.reply_text("Something went wrong during registration. Try again later.")
    except Exception as e:
        await update.message.reply_text("Unable to connect to the server.")
        print(f"Error sending data: {e}")


def main():
   
    bot_token = "7670872262:AAHV2jz-nRM4NxvUePji5otGbfiLR3_WlQM"
    
    app = ApplicationBuilder().token(bot_token).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()