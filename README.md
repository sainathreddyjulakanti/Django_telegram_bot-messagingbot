# Django_telegram_bot-messagingbot
Django Internship Assignment

# SET-UP INSTRUCTIONS:
django-admin 5.2.3
Python 3.13.1
celery 5.3.6
Redis server 5.0.14.1
djangorestframework 3.16.0
djangorestframework_simplejwt  5.5.0

# Telegram Bot
goto->telegram app->search->BotFather 
message:/start->create new bot and name it and get token

#Use the JWT AUTHENTICATION


# NOTE
1)Used Celery and Redis for sending the registration success message to the mail in console.
2)Redis is an broker and Celery is an queue task sheduling system which distribites task and can have many worker.
3)Used Telegram and got the token and used inbuilt python-telegram-bot library for handling messages
4)created two public and one private API's
5)created an manager for tackling the createsuperuser Errors 



