from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return JsonResponse({
        'message': 'Hello from Django Backend!',
        'status': 'success'
    })

@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'message': 'GET request successful',
            'data': ['item1', 'item2', 'item3']
        })
    elif request.method == 'POST':
        return JsonResponse({
            'message': 'POST request successful',
            'received': request.data
        })
