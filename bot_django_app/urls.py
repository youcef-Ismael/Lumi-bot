from django.urls import path
from bot_django_app.views import *
from django.views.decorators.csrf import csrf_exempt

"""


For Indra : (this will help you to make the front)
the User Object is :
{"api_key": xxx,
"api_secret": xxx,
"first_name": xxx,
"last_name": xxx,
}

 
1/ http://127.0.0.1:8000/login  (HTTP POST request) 
Input: the request body should contain (request.body : {"api_key": xxx, "api_secret": xxxxx})
Output: User Object
response status : 200 (successful login) , 403 (user exists but wrong api_secret),404( user don't exists), 400 (invalid data)


the request body should contain (request.body : {"api_key": xxx, "api_secret": xxxxx})

2/ http://127.0.0.1:8000/logout  (HTTP POST request) 
Input: the request body should contain (request.body : {"api_key": xxx, "api_secret": xxxxx})
Output: None
response status : 200 (successful logout) , 400 (error)


http://127.0.0.1:8000/start (HTTP POST request) - return the bot object as json
Input: the request body should contain (request.body : {api_key:xxx, api_secret:xxx, quantity: float, pair: array_of string[2]})
Output: None
response status : 200 (successful start) 


http://127.0.0.1:8000/stop (HTTP POST request) 
Input: the request body should contain (request.body :  {"api_key": xxx, "api_secret": xxxxx})
Output: None
response status : 200 (successful stop) 400 (error)


http://127.0.0.1:8000/update (HTTP POST request) 
Input: the request body should contain (request.body :  {"api_key": xxx, "api_secret": xxxxx, quantity: float})
Output: None
response status : 200 (successful update) 400 (error)


http://127.0.0.1:8000/balances (HTTP POST request)
Input: the request body should contain (request.body : {api_key:xxx, api_secret:xxx})
Output: dict of pairs {asset: value, ...}
response status : 200 (successful)


http://127.0.0.1:8000/register (HTTP POST request) - return the user object (informations about the user)
Input: the request body should contain (request.body : User Object)
Output: User Object
response status : 200 (successful registration) , 400 (invalid data)

i have set up sessions you have to think about sessions for the login and logout.

happy coding, 
Youcef 

"""

urlpatterns = [
    path('', csrf_exempt(MainView.as_view())),
    path('login/', csrf_exempt(LoginView.as_view())),
    path('logout/', csrf_exempt(LogoutView.as_view())),
    path('register/', csrf_exempt(RegisterView.as_view())),
    path('start/', csrf_exempt(StartBot.as_view())),
    path('stop/', csrf_exempt(StopBot.as_view())),
    path('update/', csrf_exempt(UpdateBot.as_view())),
    path('balances/', csrf_exempt(GetAssetsBalance.as_view())),
]


"""lumi-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
