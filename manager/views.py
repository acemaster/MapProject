from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from manager.models import Task
from manager.serializers import TaskSerializer
from django.contrib.auth import authenticate, login, logout
from .models import UserDetails, Road
import sys, traceback

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def task_list(request):
    """
    List all code Tasks, or create a new Task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)

@api_view(['POST', 'GET'])
def Login(request):
    if request.user.is_authenticated():
        return Response({"message":'User already logged in', 'status': status.HTTP_406_NOT_ACCEPTABLE })
    if request.method == "POST":
        email = request.data['email']
        password = request.data['password']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message':'Invalid username or password' , 'status':status.HTTP_406_NOT_ACCEPTABLE})
        user=None
        if u:
            user = authenticate(username=u, password=password)
        else:
            return Response({'message': 'User not registered', 'status': status.HTTP_406_NOT_ACCEPTABLE})
        
        if user is not None:
            login(request, user)
            token = Token.objects.get_or_create(user=user)
            print(token[0].key)
            firstname = u.first_name
            return Response({'message':'user logged in', 'token':token[0].key, 'email':email, 'firstname':firstname,'tzid':u.reguserprofile.tzid,'status' : status.HTTP_200_OK})
        else:
            response['message']='User is not registered'
    return Response({'message': 'User not registered', 'status': status.HTTP_406_NOT_ACCEPTABLE})

@api_view(['GET', 'POST', ])
def Register(request):
    print(request.data)
    if request.method == "POST":
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        email = request.data['email']
        password = request.data['password']
        user = User()
        user.username = email
        user.email = email
        user.first_name = firstname
        user.last_name = lastname
        user.set_password(password)
        try:
            user.save()
            message= "User successfully registered"
            print(message)
        except:
            message = "Email already present/You are already registered"
            return Response({'message': message, 'status':status.HTTP_406_NOT_ACCEPTABLE})

        reguser = None
        try:
            reguser = RegUserProfile.objects.get(user=request.user)
        except:
            print("New User")
        print("Registering user")
        if not reguser:
            reguser = RegUserProfile()
            reguser.user = user
            reguser.contact = request.data['contact']
            reguser.save()
            return Response({'message': 'User registered successfully', 'status': status.HTTP_200_OK})

    return Response({'message':'Cant Register User', 'status': status.HTTP_403_FORBIDDEN})

@api_view(['GET','POST'])
def getAllRoads(request):
    
    road_list = Road.objects.all()
    response_data = {}
    response = []
    i = 0
    for road in road_list:
        response_data['id']=road.id
        response_data['name'] = road.name
        response_data['start_lat'] = road.start_lat
        response_data['start_long'] = road.start_long
        response_data['middle_lat'] = road.middle_lat
        response_data['middle_long'] = road.middle_long
        response_data['end_lat'] = road.end_lat
        response_data['end_long'] = road.end_long
        response_data['path'] = road.path
        response_data['status'] = road.status
        response_data['remarks'] = road.remarks
        response.append(response_data)
        response_data = {}
    return Response({'data':response, 'status':status.HTTP_200_OK})

@api_view(['GET', 'POST'])
def getRoad(request):

    if request.method == 'POST':
        road_id = request.data['id']
        try:
            road = Road.objects.get(pk = road_id)
        except Road.DoesNotExist:
            return Response({'message': 'Road not found', 'status': status.HTTP_404_NOT_FOUND})

        return Response({'message': 'Success', 'name':road.name, 'start_lat': road.start_lat, 'start_long': road.start_long,
            'middle_lat':road.middle_lat, 'middle_long': road.middle_long, 'end_lat': road.end_lat, 'end_long': road.end_long,
            'path': road.path, 'road_status': road.status, 'status':status.HTTP_200_OK})
    return Response({'message': 'Forbidden', 'status': status.HTTP_403_FORBIDDEN})

@api_view(['GET', 'POST'])
def addRoad(request):
    if request.method == 'POST':
        road = Road()
        road.name = request.data['name']
        road.start_lat = request.data['start_lat']
        road.start_long = request.data['start_long']
        road.middle_lat = request.data['middle_lat']
        road.middle_long = request.data['middle_long']
        road.end_lat = request.data['end_lat']
        road.end_long = request.data['end_long']
        road.path = request.data['path']
        road.status = request.data['status']
        road.remarks=request.data['remarks']
        try:
            road.save()
        except:
            traceback.print_exc(file=sys.stdout)
            return Response({'message': 'Error', 'status': status.HTTP_406_NOT_ACCEPTABLE})
        return Response({'message': 'Road added successfully', 'status': status.HTTP_200_OK})
    return Response({'message': 'Forbidden', 'status': status.HTTP_403_FORBIDDEN})

@api_view(['GET', 'POST'])
def updateStatus(request):
    if request.method == 'POST':
        road_id = request.data['id']
        try:
            road = Road.objects.get(pk = road_id)
        except Road.DoesNotExist:
            return Response({'message': 'Road not found', 'status': status.HTTP_404_NOT_FOUND})

        road.status = request.data['status']
        road.save()
        return Response({'message': 'Road status Updated', 'status': status.HTTP_200_OK})

    return Response({'message': 'Forbidden', 'status': status.HTTP_403_FORBIDDEN})
