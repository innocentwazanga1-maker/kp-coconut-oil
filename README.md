# KP Coconut Oil — Django Website

A complete Django starter website for KP Company Limited, designed around coconut-based products.

## Included pages
- Home
- Products
- Product detail pages
- About Us
- Contact Us
- Django Admin
- Contact form saved to the database
- Responsive navigation
- Product catalog managed from Django Admin
- Media uploads for product images
- Instagram post embeds managed from Django Admin
- Blog page with published Instagram posts

## Product categories
- Coconut Oil
- Pilipili ya Nazi
- Coconut Soap
- Unga wa Lishe
- Mkaa

## Quick start

1. Create and activate a virtual environment:
   Windows:
   `python -m venv venv`
   `venv\Scripts\activate`

   macOS/Linux:
   `python3 -m venv venv`
   `source venv/bin/activate`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Apply database migrations:
   `python manage.py migrate`

4. Create an admin user:
   `python manage.py createsuperuser`

5. Run:
   `python manage.py runserver`

6. Open:
   http://127.0.0.1:8000/
   Admin: http://127.0.0.1:8000/admin/

## Adding content
Log into `/admin/` to manage products, contact messages, and Instagram posts. To add a post, choose **Instagram posts**, paste a public Instagram post URL, and publish it. The site embeds the post and caption from Instagram. Private or non-embeddable posts may only show their direct link.

## Deploying a public test site
The included `render.yaml` configures a Django web service with static-file serving. The free test deployment uses SQLite, so database changes and uploads are temporary and may be lost when Render restarts the service. To deploy:

1. Push this project to GitHub.
2. In Render, choose **New > Blueprint** and connect the GitHub repository.
3. Apply the Blueprint and wait for the first deploy to finish.
4. Open the `onrender.com` URL shown for the web service.

Render's free web service sleeps after 15 minutes without traffic, so the first request may take about a minute. Do not use this SQLite setup for production or for data that must persist. Free service files are temporary, so uploaded media isn't persistent either.

The local `db.sqlite3`, uploaded `media/`, environment files, and Python environments are excluded from Git. Create a separate admin user for the deployed site; local accounts and data are not copied.

## Contact form
Submitted messages are stored in the `ContactMessage` model and visible in Django Admin.

## Notes
Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` through the deployment environment. Never commit passwords, secret keys, local databases, or customer messages.
