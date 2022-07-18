from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Profile, University, Notifications

admin.site.register(University)
admin.site.register(Profile)
admin.site.register(Notifications)
