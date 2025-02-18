from django.contrib import admin
from .models import Hero, About, Resume, Skills, Projects, Message
from django_json_widget.widgets import JSONEditorWidget
from django.db import models

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'resume_link')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('study_year', 'total_projects', 'total_problems_solved', 'total_certifications')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id',)
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('tech_field', 'desc')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_link', 'github_link')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
