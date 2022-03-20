from django.contrib.auth import get_user_model
from django.db import models

from martor.models import MartorField


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = MartorField()

    def __str__(self) -> str:
        return f"{self.title}, slug - {self.slug}"


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    text = MartorField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Выбери категорию для поста"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        default=1
    )
    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"
