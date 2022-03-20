from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def index(request):
    posts = Post.objects.select_related('category').all()
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'posts/index.html',
        {'page': page, 'paginator': paginator}
    )


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'posts/category.html',
        {'category': category, 'page': page, 'paginator': paginator}
    )


def post_detail(request, slug, post_id):
    pass
