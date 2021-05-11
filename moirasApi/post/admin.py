from django.contrib import admin

# Register your models here.
from .models import Post,ImagePost,UrlPost,Comment

admin.site.register(Post)
admin.site.register(ImagePost)
admin.site.register(UrlPost)
admin.site.register(Comment)
