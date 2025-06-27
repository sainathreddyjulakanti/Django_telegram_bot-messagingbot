from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TelegramUserSerializer
from rest_framework import serializers
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_URL = os.getenv("API_URL")


class TelegramUserView(APIView):
    def post(self, request):
        username = request.data.get('username', 'Anonymous')
        serializer = TelegramUserSerializer(data={'username': username})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
   
    bot_token = os.getenv("bot_token")
    
    app = ApplicationBuilder().token(bot_token).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()