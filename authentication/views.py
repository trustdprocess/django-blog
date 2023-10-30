from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from . models import Post,Comment
from . forms import PostForm,CommentForm

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already Exists.")
        else:
            # Username doesn't exist, create the user
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username
            )
            user.set_password(password)  # Set the password
            user.save()  # Save the user to the database

            messages.success(request, "User Created Successfully.")

    return render(request, "register.html")



def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Incorrect Username")
            return redirect('loginpage')  # Correct the view name
     
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid User")
            return redirect('loginpage')  # Correct the view name
        else:
            login(request,user)  # Move the login function inside the 'else' block
            return redirect('homepage')  # Correct the view name
    
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("loginpage")


@login_required(login_url="loginpage")
def homepage(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }
    return render(request,"homepage.html",context)

@login_required(login_url="loginpage")
def addpost(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect("homepage")
    else:
        form=PostForm()
    context={
        "forms":form
    }
    return render(request,"addpost.html",context)   

@login_required(login_url="loginpage")
def addcomment(request):
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            form.save()
    else:
        form=CommentForm()
    
    context={
        "forms":form
    }
     
    return render(request,"commentform.html",context)


@login_required(login_url="loginpage")
def detailposts(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)  # Get comments associated with the post

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("detailpage", id=id)  # Redirect back to the same detail page

    else:
        form = CommentForm()

    context = {
        "posts": post,
        "comments": comments,
        "forms": form
    }

    return render(request, "detailpage.html", context)

        
    


    
             


    
            

    
    



    
    

    



        
        
