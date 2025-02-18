from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    social_links = models.JSONField()
    resume_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class About(models.Model):
    profile_img_link = models.CharField(max_length=255)
    desc = models.TextField()
    study_year = models.CharField(max_length=50)
    total_projects = models.IntegerField()
    total_problems_solved = models.IntegerField()
    total_certifications = models.IntegerField()

    def __str__(self):
        return f"About - {self.study_year}"

class Resume(models.Model):
    degree_details = models.JSONField()
    work_experience = models.JSONField()

    def __str__(self):
        return f"Resume {self.id}"

class Skills(models.Model):
    tech_field = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.tech_field

class Projects(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img_link = models.CharField(max_length=255)
    live_link = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    tech_stack = models.JSONField()

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"