from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, Category
from .forms import BlogForm

#render =>  response객체를 해당 url로 보내줌
def base(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    return render(request, 'base.html', {'blogs': blogs, 'categories': categories})

def home(request):
    category_id = request.GET.get('category')
    if category_id:
        blogs = Blog.objects.filter(category__id=category_id)
    else:
        blogs = Blog.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{'blogs':blogs, 'categories': categories})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    categories = Category.objects.all() # 카테고리 정보를 가져옴
    return render(request,'new.html', {'categories': categories})
    
#def create(request):
#    new_blog = Blog()
#    new_blog.title = request.POST['title'] #post->딕셔너리 값으로 바꿔줌
#    new_blog.content = request.POST['content']
#    new_blog.save()
#    return redirect('detail', new_blog.id)
#    #return render(request, 'detail.html', {'blog':new_blog}) <-새로고침하면 계속 post를 요청


def create(request):
    form = BlogForm(request.POST, request.FILES)#post로 넘어온 입력값
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', new_blog.id)
    return render(request, "new.html")



def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    categories = Category.objects.all()
    return render(request, 'edit.html', {'edit_blog':edit_blog, 'categories': categories})


#def update(request, blog_id):
#    old_blog = get_object_or_404(Blog, pk=blog_id)
#    old_blog.title = request.POST['title']
#    old_blog.content = request.POST['content']
#    old_blog.save()
#    return redirect('detail', old_blog.id)

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
