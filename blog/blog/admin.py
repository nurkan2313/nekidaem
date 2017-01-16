from django.contrib import admin
from blog.models import Post, Blog
# Register your models here.


class AdminBlog(admin.ModelAdmin):
    filter_horizontal = ['subscriber']

admin.site.register(Post)
admin.site.register(Blog, AdminBlog)
