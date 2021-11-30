from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import FutureSerializer, TodoSerializer
from .models import Todo
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone

@swagger_auto_schema(methods=['POST'], request_body=TodoSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def todo(request):
    if request.method == 'GET':
        objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(objs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer =  TodoSerializer(data=request.data)
        if serializer.is_valid():
            
            if 'user' in serializer.validated_data.keys():
                serializer.validated_data.pop('user')
                
            object = Todo.objects.create(**serializer.validated_data, user=request.user)
            serializer = TodoSerializer(object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=TodoSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, todo_id):
   
    try:
        obj = Todo.objects.get(id = todo_id)
    
    except Todo.DoesNotExist:
        data = {
                'status'  : False,
                'message' : "Does not exist"
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)
    if obj.user != request.user:
        raise PermissionDenied(detail='You do not have permission to perform this action')
    
    
    if request.method == 'GET':
        serializer = TodoSerializer(obj)
        
        data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    #Update the profile of the TODO
    elif request.method == 'PUT':
        serializer = TodoSerializer(obj, data = request.data, partial=True) 

        if serializer.is_valid():
        
            serializer.save()

            data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

            return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : False,
                'message' : "Unsuccessful",
                'error' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)

    #delete the account
    elif request.method == 'DELETE':
        obj.delete()

        data = {
                'status'  : True,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)
    
    
    
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def mark_complete(request, todo_id):
   
    try:
        obj = Todo.objects.get(id = todo_id)
    
    except Todo.DoesNotExist:
        data = {
                'status'  : False,
                'message' : "Does not exist"
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)
    if obj.user != request.user:
        raise PermissionDenied(detail='You do not have permission to perform this action')
    
    
    if request.method == 'GET':
        if obj.completed == False:
            obj.completed=True
            obj.save()
                  
            data = {
                    'status'  : True,
                    'message' : "Successful"
                }

            return Response(data, status=status.HTTP_200_OK)
        else:
                  
            data = {
                    'status'  : False,
                    'message' : "Already marked complete"
                }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        

    
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def today_list(request):
    if request.method == 'GET':
        today_date = timezone.now().date()
        objects = Todo.objects.filter(date=today_date, user=request.user)
        
        serializer = TodoSerializer(objects, many=True)
        data = {
            'status'  : True,
            'message' : "Successful",
            'data' : serializer.data,
        }

        return Response(data, status = status.HTTP_200_OK)


@swagger_auto_schema(method='post', request_body=FutureSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def future_list(request):
    if request.method == 'POST':
        serializer = FutureSerializer(data=request.data)
        if serializer.is_valid():
            objects = Todo.objects.filter(date=serializer.validated_data['date'], user=request.user)
            
            serializer = TodoSerializer(objects, many=True)
            data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

            return Response(data, status = status.HTTP_200_OK)
        else:
            error = {
                'status'  : False,
                'message' : "failed",
                'error' : serializer.errors,
            }

            return Response(error, status = status.HTTP_200_OK)