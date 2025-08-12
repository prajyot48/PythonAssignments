from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import UserDetails
import json

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Check if email already exists
            if UserDetails.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return render(request, 'signup.html')
            
            # Create new user
            user = UserDetails.objects.create(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f'Welcome {user.username}!')
            return render(request, 'success.html', {'user': user})
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password!')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

# CRUD Operations
@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        users = UserDetails.objects.all()
        users_data = []
        for user in users:
            users_data.append({
                'username': user.username,
                'email': user.email,
                'password': user.password
            })
        return JsonResponse({'users': users_data})

@csrf_exempt
def get_user_by_email(request, email):
    if request.method == 'GET':
        try:
            user = UserDetails.objects.get(email=email)
            user_data = {
                'username': user.username,
                'email': user.email,
                'password': user.password
            }
            return JsonResponse({'user': user_data})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def update_user(request, email):
    if request.method == 'PUT':
        try:
            user = UserDetails.objects.get(email=email)
            data = json.loads(request.body)
            
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.save()
            
            return JsonResponse({'message': 'User updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)