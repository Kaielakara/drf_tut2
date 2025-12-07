from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import json

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def api_message(request, *args, **kwargs):

    data = {}
    try:
        data = json.loads(request.body)
        
    except:
        pass
    
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    return JsonResponse(data)