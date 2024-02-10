from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Image(models.Model):
    file = models.ImageField(upload_to='images')
    description = models.TextField(
        max_length=500,
        verbose_name="details"
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.description[:20]}..."

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo'




