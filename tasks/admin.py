from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=['title', 'completed', 'description']
    def image_preview(self,obj):
        if obj.image:
            return '<img src="{0}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url)
        else:
            return 'No Image'
            
        image_preview.allow_tags=True

admin.site.register(Task,TaskAdmin)