from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from bot_django_app.models import User


class UserView(ListView):
    model = User

    def get(self, request):
        user = self.get_queryset(username=request.username)

        return JsonResponse(user)


"""
FOR MY COLAB
django is a python coding django is just a stucture, don't be offended by the names
"A view is a callable which takes a request and returns a response"

so guys below i have created 4 views for you, you can add more if you feel the need to.
you can either chose to implement the get or the post request as you need.
ofc you have to change the name of the views with a significant name.

don't worry i will take care of connection the view with the rest of the app. 

the idea behind views is that you a view should always return a JSON response  
you can get the input data from the request variable (request is of type JSON object)

a view can do one task for exemple (getting profile information for a specific user, creating a user ) 
and so on, you got the idea.

if you need any interaction with the database you can find query making instuction by following this link 
(it only takes you 5 min) 
https://docs.djangoproject.com/en/3.2/topics/db/queries/

and if you need any help, let me know ;)

Happy coding 

"""


class MyView1(View):
    def get(self, request):
        # <view logic>
        return JsonResponse()

    def post(self, request):
        # <view logic>
        return JsonResponse()


class MyView2(View):
    def get(self, request):
        # <view logic>
        return JsonResponse()


class MyView3(View):
    def get(self, request):
        # <view logic>
        return JsonResponse()


class MyView4(View):
    def get(self, request):
        # <view logic>
        return JsonResponse()
