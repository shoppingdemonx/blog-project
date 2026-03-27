from django.contrib import admin
from .models import Profile,Post,PostImages


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','status']
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(PostImages)