from django.contrib import admin
from .models import AboutSection, AboutText
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.admin import SummernoteInlineModelAdmin

# Register your models here.


class AboutTextAdminInLine(admin.TabularInline):
    model = AboutText

class AboutSectionAdmin(admin.ModelAdmin):
    inlines = (AboutTextAdminInLine,)

    readonly_fields = ()

    fields = ('section', 'disp_seq', 'hide_display', 'section_title')

    list_display = ('section', 'disp_seq', 'hide_display', 'section_title')

    ordering = ('disp_seq',)

admin.site.register(AboutSection, AboutSectionAdmin, )