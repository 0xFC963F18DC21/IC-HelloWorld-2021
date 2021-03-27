from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def Callback(request):
    # Save code to current user object
    return JsonResponse(request.GET.get('code', ''),safe=False)