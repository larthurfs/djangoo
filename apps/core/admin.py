from django.contrib import admin

from apps.core.models import Ferramentas


class FerramentasModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativa')
    search_fields = ('nome', 'ativa')
    list_filter = ('nome','ativa')



admin.site.register(Ferramentas, FerramentasModelAdmin)

