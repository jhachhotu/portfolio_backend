from django.contrib import admin
from .models import Hero, About, Resume, Skills, Projects, Message

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'resume_link')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('study_year', 'total_projects', 'total_problems_solved', 'total_certifications')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('tech_field', 'desc')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_link', 'github_link')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
