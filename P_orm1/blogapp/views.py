from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from .models import post
# Create your views here.

def add_blog(request:HttpRequest):
    if request.method =="POST":
        new_blog=post(title=request.POST["title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_data=request.POST["publish_data"])
        new_blog.save
    return render(request,"blog/addpost.html")

#def raed_blog(request:HttpRequest):
    #post_list = post.objects.all()
    
    #return render(request,"blog/raedpost.html" ,{"raedblog": post_list})
def raed_blog(request : HttpRequest):
    post_list = post.objects.all()

    return render(request, "blog/raedpost.html", {"Posts": post_list})
    