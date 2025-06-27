# Django_telegram_bot-messagingbot
Django Internship Assignment

# SET-UP INSTRUCTIONS:
django-admin 5.2.3<br>
Python 3.13.1 <br>
celery 5.3.6 <br>
Redis server 5.0.14.1 <br>
djangorestframework 3.16.0 <br>
djangorestframework_simplejwt  5.5.0 <br>

# Telegram Bot
goto->telegram app->search->BotFather <br>
message:/start->create new bot and name it and get token <br>

#Used the JWT AUTHENTICATION
one for login whcih is public and home page as private used is permission_classess <br>

# NOTE
1)Used Celery and Redis for sending the registration success message to the mail in console. <br>
2)Redis is an broker and Celery is an queue task sheduling system which distribites task and can have many worker. <br>
3)Used Telegram and got the token and used inbuilt python-telegram-bot library for handling messages <br>
4)created two public and one private API's<br>
5)created an manager for tackling the createsuperuser Errors <br>



