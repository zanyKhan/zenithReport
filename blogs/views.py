from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q
# Create your views here.

def blogs_by_category(request, category_id):
    blogs = Blog.objects.filter(category_id = category_id, status = 'Published').order_by('-updated_at')
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    # category = get_object_or_404(Category, pk= category_id)

    context = {
        'blogs' : blogs,
        'category' : category
    }

    return render(request, 'blog_by_category.html', context)


# def custom_page_not_found(request, exception=None):
#     return render(request, '404.html', status=404)


# def custom_server_error(request):
#     return render(request, '404.html', status=500)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog = single_blog)
    comment_count = comments.count()
    context={
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')
    context = {
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(request, 'search.html', context)