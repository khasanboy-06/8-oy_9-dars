from django.contrib import admin

from .models import Like, Comment, Blog

admin.site.register(Like)

admin.site.register(Comment)

admin.site.register(Blog)