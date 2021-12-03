from .controller import *
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
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
            api_key = request.session["api_key"]
            usr = get_object_or_404(User, pk=api_key)
            ser = UserSerializer(usr)
            return JsonResponse(ser.data, status=200, safe=False)
        except:
            data = json.loads(request.body)
            ser = LoginSerializer(data=data)
            if ser.is_valid():
                usr = get_object_or_404(
                    User, api_key=ser.validated_data["api_key"])

                if usr.api_secret == ser.validated_data["api_secret"]:
                    request.session["api_key"] = usr.api_key
                    ser = UserSerializer(usr)
                    return JsonResponse(ser.data, status=200, safe=False)
                else:
                    return HttpResponse(status=403)
            else:
                return HttpResponse(status=400)


class LogoutView(View):
    def post(self, request):
        try:
            del request.session["api_key"]
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)


# to register the user
class RegisterView(View):

    def post(self, request):
        data = json.loads(request.body)
        ser = UserSerializer(data=data)
        if ser.is_valid():
            newUser = User(api_key=ser.validated_data["api_key"],
                           last_name=ser.validated_data["last_name"],
                           first_name=ser.validated_data["first_name"],
                           api_secret=ser.validated_data["api_secret"]
                           )
            newUser.save()
            request.session["api_key"] = newUser.api_key

            ser = UserSerializer(newUser)
            return JsonResponse(ser.data, status=200, safe=False)
        else:
            return HttpResponse(status=400)


# ///////////////////////////////////////////////////////

class GetAssetsBalance(View):
    def post(self, request):
        data = json.loads(request.body)
        ser = LoginSerializer(data=data)
        if ser.is_valid():
            api_key = ser.validated_data["api_key"]
            api_secret = ser.validated_data["api_secret"]
            balances_dict = get_balances_for_assets(api_key, api_secret)
            return JsonResponse(json.dumps(balances_dict), status=200, safe=False)
        else:
            return JsonResponse(status=400, safe=False)


class StartBot(View):
    def post(self, request):
        data = json.loads(request.body)
        ser = BotSerializer(data=data)
        if ser.is_valid():
            api_key = ser.validated_data["api_key"]
            api_secret = ser.validated_data["api_secret"]
            quantity = ser.validated_data["quantity"]
            pair = tuple(ser.validated_data["pair"])
            start(api_key, api_secret, quantity, pair)
            return JsonResponse(status=200, safe=False)
        else:
            return JsonResponse(status=400, safe=False)


class UpdateBot(View):
    def post(self, request):
        data = json.loads(request.body)
        ser = LoginSerializer(data=data)
        if ser.is_valid():
            api_key = ser.validated_data["api_key"]
            update_quantity(api_key, data.quantity)
            return JsonResponse(status=200, safe=False)
        else:
            return JsonResponse(status=400, safe=False)


class StopBot(View):
    def post(self, request):
        data = json.loads(request.body)
        ser = LoginSerializer(data=data)
        if ser.is_valid():
            api_key = ser.validated_data["api_key"]
            stop(api_key)
            return JsonResponse(status=200, safe=False)
        else:
            return JsonResponse(status=400, safe=False)
