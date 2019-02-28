from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from owners.models import Owner
from owners.serializers import OwnerSerializer
# Create your views here.


@csrf_exempt
def owner_list(request):
    """
    List all owners, or create a new one
    """
    if request.method == 'GET':
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def owner_detail(request, pk):
    """
    Retrieve, updated, or delete an owner
    """
    try:
        owner = Owner.objects.get(pk=pk)
    except Owner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OwnerSerializer(owner)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(owner, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        owner.delete()
        return HttpResponse(status=204)