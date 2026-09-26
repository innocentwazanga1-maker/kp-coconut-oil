from urllib.parse import urlsplit

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


def validate_instagram_post_url(value):
    hostname = urlsplit(value).hostname
    if hostname not in {"instagram.com", "www.instagram.com", "m.instagram.com"}:
        raise ValidationError("Enter a link to a public Instagram post, Reel, or video.")


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("coconut-oil", "Coconut Oil"),
        ("pilipili", "Pilipili ya Nazi"),
        ("soap", "Coconut Soap"),
        ("unga", "Unga wa Lishe"),
        ("mkaa", "Mkaa"),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} — {self.email}"


class InstagramPost(models.Model):
    caption = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="instagram_posts/", blank=True, null=True)
    instagram_url = models.URLField(
        validators=[validate_instagram_post_url],
        help_text="Paste the URL of a public Instagram post, Reel, or video.",
    )
    posted_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_at", "-created_at"]
        verbose_name = "Instagram post"
        verbose_name_plural = "Instagram posts"

    def __str__(self):
        return self.instagram_url
