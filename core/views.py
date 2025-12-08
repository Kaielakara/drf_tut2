from django.forms import model_to_dict
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json

from .models import Product
from .serializers import ProductSerializers

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

def api_model(request, *args, **kwargs):
    p_one = Product.objects.all().order_by('?').first()

    data ={}

    # this basically creates a dictionary using the values of the model fields (this is the manual way)
    # if p_one:
    #     data['title'] = p_one.title
    #     data['description'] = p_one.description
    #     data['price'] = p_one.price

    # or you could use a library

    data = model_to_dict(p_one, fields=['id', 'title', 'price'])

    
    return JsonResponse(data)

# this is using the djangorest framework
@api_view(['GET', 'POST'])
def drf_model(request, *args, **kwargs):

    # This is for 
    if request.method == 'POST':
        
        # for this next line avoid using positional arguements but rather keyword arguements
        serializer = ProductSerializers(data=request.data) 
        if serializer.is_valid(raise_exception=True): #This will show us the error
            serializer.save() # this will help save the new instance into the database
            return Response(serializer.data)

    else:
        instance = Product.objects.all().order_by("?").first()
        data = {}
        
        if instance:
            data = ProductSerializers(instance).data

        return Response(data)
