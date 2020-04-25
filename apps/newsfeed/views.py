from django.shortcuts import render,redirect

from django.contrib import messages

from ..first_app.models import User

from . models import Post

# Create your views here.
def success(request):
    if 'user_id' in request.session:
        context = {
            'user' : User.objects.get(id = request.session['user_id']),
            'posts': Post.objects.all().order_by(
                '-created_at')
        }
    
        return render(request,"newsfeed/newsfeed.html",context)

    return redirect('loginreg:index')


def addPost(request):
    response_from_models = Post.objects.validate_post(request.POST,request.session['user_id'])

    if response_from_models == False:
        messages.error(request,"Your post must be 180 characters")
        
    return redirect('newsfeed:success')


def addLike(request,id):
    post_id = id 

    Post.objects.validate_like(request.session['user_id'], post_id)

    return redirect("newsfeed:success")


def deletePost(request,id):
    Post.objects.get(id = id).delete()  

    return redirect("newsfeed:success")

def editPost(request,id):
    post = Post.objects.get(id = id)
    context = {
        'post': post
    }

    return render(request,"newsfeed/editpost.html",context)


def updatePost(request,id):
    if request.method == 'POST':
        post = Post.objects.get(id = id)

        post.post = request.POST['post']

        post.save()

        return redirect('newsfeed:success')

    route = str(id) + "/edit_post"

    return redirect("newsfeed:editPost")