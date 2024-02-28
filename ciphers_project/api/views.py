from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import caeser_encode

# Create your views here.
def greetings(request):
    result = {"message" : "Welcome to ciphers service"}
    return JsonResponse(result)


def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caeser_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})