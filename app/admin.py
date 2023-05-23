from django.contrib import admin

from .models import Config , Info, Customized_Info

# Register your models here.
admin.site.register(Config)
admin.site.register(Info)
admin.site.register(Customized_Info)
