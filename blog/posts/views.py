from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Post


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
    pass
