from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Public_Channel, Public_Posts, Post_Comments
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username= username, password=password)

        if user is not None:
            auth.login(request,user)
            
            return redirect('/channels')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect( '/')
    
    else:
        return render(request, 'main/index.html')


def signup(request):
    if request.method== 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already Used')           
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup') 
            elif first_name=="" or last_name=="":
                messages.info(request, 'Please fill in your first name and last name')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password= password, first_name= first_name, last_name= last_name )
                user.save(); 
                return redirect('index')
        else:
            messages.info(request, 'Password confirmation failed')
            return redirect('signup')
    else:
        return render(request, 'main/signup.html')
def channels_page(request):
    current_user= request.user
    public_channel_list = Public_Channel.objects.all()
    context ={ 
        'user': current_user,
        'public_channels': public_channel_list,

    }
    return render(request, 'main/channels.html', context)


    #current_user = request.user
def public_channel_form(request):
    if request.method == 'POST':
        pub_channel_name = request.POST['pub_channel_name']
        channel_subject = request.POST['channel_subject']
        channel_creator = request.user.username
        channel_members = request.user
        channel_date_created = datetime.datetime.now()

        channel = Public_Channel.objects.create(
            pub_channel_name= pub_channel_name,
            channel_subject = channel_subject,
            channel_creator =channel_creator,
            channel_members = channel_members,
            channel_date_created = channel_date_created
        )
        channel.save();
        return redirect('channels')

############## channel pe click karne se channel members+= request.user ho jaega
        
    return render(request, 'main/public_channel_form.html')

def channel_posts(request, pub_channel_name):
    channel = Public_Channel.objects.get(pub_channel_name= pub_channel_name)
    channel_subject = channel.channel_subject
    channel_posts = Public_Posts.objects.filter(channel=channel)
    if request.method=='GET':
        post = Public_Posts.objects.get(id=id)
        print(post)

    context ={
        'channel_name': pub_channel_name,
        'channel_subject':channel_subject,
        'channel_creator': channel.channel_creator,
        'channel_posts': channel_posts,
    }

    
    return render(request, 'main/public_channel_posts.html', context)



def pub_add_post(request, pub_channel_name):
    channel = Public_Channel.objects.get(pub_channel_name= pub_channel_name)
    channel_subject = channel.channel_subject

    
    if request.method=='POST':
        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        author = request.user
        post_date_created = datetime.datetime.now()

        public_post = Public_Posts.objects.create(
            post_title = post_title,
            post_content = post_content,
            author = author,
            post_date_created = post_date_created,
            channel = channel
        )
        public_post.save();
        return redirect('channel_posts' ,pub_channel_name)
        

    context ={
        'channel_name': pub_channel_name,
        'channel_subject':channel_subject,
        'channel_creator': channel.channel_creator,
    }    
    
    return render(request, 'main/pub_add_post.html', context)

