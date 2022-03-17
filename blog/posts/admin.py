from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget

from posts.models import Category, Post


class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class CategoryModelAdmin(PostModelAdmin):
    pass


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
