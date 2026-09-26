from django.contrib import admin
from .models import ContactMessage, InstagramPost, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "featured", "available", "created_at")
    list_filter = ("category", "featured", "available")
    search_fields = ("name", "description", "short_description")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "replied", "created_at")
    list_filter = ("replied", "created_at")
    search_fields = ("first_name", "last_name", "email", "message")


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ("instagram_url", "posted_at", "is_published")
    list_filter = ("is_published", "posted_at")
    search_fields = ("instagram_url", "caption")
    readonly_fields = ("created_at",)
    fields = ("instagram_url", "is_published")
