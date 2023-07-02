
from django.contrib import admin
from.models import Post , Comment 
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(Post , SomeModelAdmin)

admin.site.register(Comment)
