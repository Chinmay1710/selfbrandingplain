"""
Database models for Chinmay's portfolio website.
"""

from django.db import models


class Profile(models.Model):
    """Singleton model for personal information."""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_pdf = models.FileField(upload_to='resume/', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name


class Education(models.Model):
    """Education timeline entries."""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_year']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} – {self.institution}"


class Skill(models.Model):
    """Skills with categories and proficiency."""
    CATEGORY_CHOICES = [
        ('lang', 'Programming Languages'),
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('db', 'Database'),
        ('tools', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(default=80, help_text='0–100 percent')
    icon_class = models.CharField(max_length=100, blank=True, help_text='Bootstrap icon class e.g. bi-code-slash')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    """Portfolio projects."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text='Comma-separated technologies')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    # UPDATED LINE BELOW: Added null=True and blank=True to allow loaddata to work
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Internship(models.Model):
    """Work experience / internship entries."""
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True, help_text='Comma-separated')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Internship / Experience'
        verbose_name_plural = 'Internships / Experience'

    def __str__(self):
        return f"{self.role} at {self.company}"

    def get_duration(self):
        start = self.start_date.strftime('%B %Y')
        end = 'Present' if self.is_current else (self.end_date.strftime('%B %Y') if self.end_date else '')
        return f"{start} – {end}"

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Certification(models.Model):
    """Certifications and courses."""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_issued = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date_issued']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return f"{self.title} – {self.issuer}"


class ContactMessage(models.Model):
    """Messages submitted through the contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} – {self.email} ({self.created_at.strftime('%d %b %Y')})"