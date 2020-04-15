from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Notice)
admin.site.register(models.Feedback)
admin.site.register(models.Student)
admin.site.register(models.Account)
admin.site.register(models.Admin)
