from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
# from django.views.generic import ListView
from django.views import View
from .serializers import *
import json

from bot_django_app.models import User


class MainView(View):
    def get(self, request):
        return HttpResponse("welcome to our website")


# to login
class LoginView(View):
    # model = User

    def post(self, request):

        try:
            username = request.session["username"]
            usr = get_object_or_404(User, pk=username)
            ser = UserSerializer(usr)
            return JsonResponse(ser.data, status=200, safe=False)
        except:
            data = json.loads(request.body)
            ser = LoginSerializer(data=data)
            if ser.is_valid():
                usr = get_object_or_404(
                    User, username=ser.validated_data["username"])

                if usr.password == ser.validated_data["password"]:
                    request.session["username"] = usr.username
                    ser = UserSerializer(usr)
                    return JsonResponse(ser.data, status=200, safe=False)
                else:
                    return HttpResponse(status=403)
            else:
                return HttpResponse(status=400)


class LogoutView(View):
    def post(self, request):
        try:
            del request.session["username"]
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)


# to register the user
class RegisterView(View):

    def post(self, request):
        data = json.loads(request.body)
        ser = UserSerializer(data=data)
        if ser.is_valid():
            newUser = User(username=ser.validated_data["username"],
                           last_name=ser.validated_data["last_name"],
                           first_name=ser.validated_data["first_name"],
                           password=ser.validated_data["password"],
                           tel_number=ser.validated_data["tel_number"],
                           email=ser.validated_data["email"])
            newUser.save()
            request.session["username"] = newUser.username

            ser = UserSerializer(newUser)
            return JsonResponse(ser.data, status=200, safe=False)
        else:
            return HttpResponse(status=400)


# class MyView2(View):
#     def get(self, request):
#         # <view logic>
#         return JsonResponse()


# class MyView3(View):
#     def get(self, request):
#         # <view logic>
#         return JsonResponse()


# class MyView4(View):
#     def get(self, request):
#         # <view logic>
#         return JsonResponse()
