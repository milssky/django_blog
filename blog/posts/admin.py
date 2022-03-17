from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget

from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Post, PostModelAdmin)
