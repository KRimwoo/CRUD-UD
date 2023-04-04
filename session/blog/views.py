from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm

#render =>  response객체를 해당 url로 보내줌
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')
'''
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title'] #post->딕셔너리 값으로 바꿔줌
    new_blog.content = request.POST['content']
    new_blog.save()
    return redirect('detail', new_blog.id)
    #return render(request, 'detail.html', {'blog':new_blog}) <-새로고침하면 계속 post를 요청
'''

def create(request):
    form = BlogForm(request.POST)#post로 넘어온 입력값
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', new_blog.id)
    return render(request, "new.html")



def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})

'''
def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST['title']
    old_blog.content = request.POST['content']
    old_blog.save()
    return redirect('detail', old_blog.id)
'''
def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST, instance=old_blog)

    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)

    return render(request, "new.html")

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')
