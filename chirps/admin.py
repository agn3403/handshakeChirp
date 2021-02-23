from django.contrib import admin

# Register your models here.
from .models import Chirp


class ChirpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
        ('ID Info', {'fields': ['id']}),
        ('Votes Number', {'votes': ['votes']}),
    ]


admin.site.register(Chirp)
