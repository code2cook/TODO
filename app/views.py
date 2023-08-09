from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from app.forms import PictureUploadForm
from django.contrib.auth.decorators import login_required
import boto3

from .models import foodCard4 as foodCards, Comment

from django.conf import settings
from django.http import JsonResponse

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        foodCard = foodCards.objects.all()
        comments = Comment.objects.all()
        return render(request , 'index.html' , context={'foodCard': foodCard, 'comments':comments})

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )


def signup(request):
    

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)



# @login_required(login_url='login')
# def add_todo(request):
#     if request.user.is_authenticated:
#         user = request.user
#         print(user)
#         form = TODOForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             todo = form.save(commit=False)
#             todo.user = user
#             todo.save()
#             print(todo)
#             return redirect("home")
#         else: 
#             return render(request , 'index.html' , context={'form' : form})
        
        
@login_required(login_url='login')
def add_todo(request):
    
    
    if request.user.is_authenticated and request.method == 'POST':
        user = request.user
        print(user)
        form = PictureUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            
         
            s3 = boto3.client('s3',region_name='us-east-1', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
            file_obj = request.FILES['picture']
            s3.upload_fileobj(file_obj, 'django-media-s3-myblog', file_obj.name)
            
            # Save the S3 URL and other attributes in the database
            picture_url = f'https://django-media-s3-myblog.s3.amazonaws.com/{file_obj.name}'
            foodName = form.cleaned_data['foodName']
            comments= form.cleaned_data['comment']
            # need to create model to save in db
            food = foodCards.objects.create(foodName=foodName, author = user, image_url=picture_url)
            Comment.objects.create(food_card=food,text=comments)
            return redirect('home')
    else:
        
        form = PictureUploadForm()
    return render(request, 'upload_picture.html', {'form': form})



def signout(request):
    logout(request)
    return redirect('login')


def resume(request):
    print("this is my resume ")
    return render(request, 'resume.html')

def foodPage(request):
    return render(request, 'foodPage.html')



@login_required(login_url='login')
def like_food(request, card_id):
    card = foodCards.objects.get(pk=card_id)
    card.like_count += 1
    card.save()
    return JsonResponse({'likes': card.like_count})


@login_required(login_url='login')
def dislike_food(request, card_id):
    card = foodCards.objects.get(pk=card_id)
    card.dislike_count += 1
    card.save()
    return JsonResponse({'dislikes': card.dislike_count})

def add_comment(request, card_id):
    
    if request.method == 'POST' and request.is_ajax():
        card = foodCards.objects.get(id=card_id)
        text = request.POST.get('comment_text')
        Comment.objects.create(food_card=card,text=text)
        Comments = Comment.objects.filter(food_card = card)
        # Comment.objects.create(food_card=card,text=text)
        # comment_list = list(Comments.values())
        response = JsonResponse({'comments': text})
        response['X-Requested-With'] = 'XMLHttpRequest'
        return response
    return redirect('home')