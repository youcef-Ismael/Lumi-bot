from django.urls import path
from bot_django_app.views import *


"""
Hello guys

what i have made so far:
    - created a model for the User
    - created the views for (Login, Registration, Logout)
    - installed the rest_framework
    - created different Serialisers to communicate with the front ( UserSerializer, LoginSerializer)
    - linked the views 
    - provided indra with detailed informations about the links to interact with
    - created requirement.txt file, i have copied in that file all the external packages we used so far,
    from now on any other package you use in the app you have to put its name in the requirements.txt 
    - created how_to_lunch_the_server.txt, it contains the set of instructions to lunch the django server

tommorow: 
    - Indra told me that he will show at least the main interface to the mentor
    - for my part i will show him what i have done so far 

And we have to set up a meeting in the few next days, to discuss about the remainings parts.


For Indra : (this will help you to make the front)
the User Object is :
{"username": xxx,
"last_name": xxx,
"first_name": xxx,
"password": xxx,
"tel_number": xxx,
"email": xxx, }

 
1/ http://127.0.0.1:8000/login  (HTTP POST request) 
Input: the request body should contain (request.body : {"username": xxx, "password": xxxxx})
Output: User Object
response status : 200 (successful login) , 403 (user exists but wrong password),404( user don't exists), 400 (invalid data)


the request body should contain (request.body : {"username": xxx, "password": xxxxx})

2/ http://127.0.0.1:8000/logout  (HTTP POST request) 
Input: the request body should contain (request.body : {"username": xxx, "password": xxxxx})
Output: None
response status : 200 (successful logout) , 400 (error)


http://127.0.0.1:8000/register (HTTP POST request) - return the user object (informations about the user)
Input: the request body should contain (request.body : User Object)
Output: User Object
response status : 200 (successful registration) , 400 (invalid data)

i have set up sessions you have to think about sessions for the login and logout.
(You can find this comment under "bot_django_app/urls.py" as well)

happy coding, 
Youcef 

"""

urlpatterns = [
    path('', MainView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view())
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
