from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import InstagramPost


class InstagramPostViewTests(TestCase):
    def create_post(self, slug, posted_at=None, is_published=True):
        return InstagramPost.objects.create(
            instagram_url=f"https://www.instagram.com/p/{slug}/",
            posted_at=posted_at or timezone.now(),
            is_published=is_published,
        )

    def test_home_shows_three_latest_published_posts(self):
        now = timezone.now()
        for index in range(4):
            self.create_post(f"published-{index}", now + timedelta(minutes=index))
        self.create_post("draft", now + timedelta(days=1), is_published=False)

        response = self.client.get(reverse("home"))

        self.assertContains(response, "published-3")
        self.assertContains(response, "published-2")
        self.assertContains(response, "published-1")
        self.assertNotContains(response, "published-0")
        self.assertNotContains(response, "draft")

    def test_blog_embeds_published_posts_and_hides_drafts(self):
        now = timezone.now()
        self.create_post("public-post", now)
        self.create_post("private-post", now, is_published=False)

        response = self.client.get(reverse("blog"))

        self.assertContains(response, 'data-instgrm-permalink="https://www.instagram.com/p/public-post/"')
        self.assertContains(response, "instagram.com/embed.js")
        self.assertNotContains(response, "private-post")

    def test_instagram_post_rejects_non_instagram_urls(self):
        post = InstagramPost(instagram_url="https://example.com/post")

        with self.assertRaises(ValidationError):
            post.full_clean()