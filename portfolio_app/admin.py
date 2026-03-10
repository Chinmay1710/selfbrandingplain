"""Admin configuration for portfolio_app."""

from django.contrib import admin
from .models import Profile, Education, Skill, Project, Internship, Certification, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_year', 'end_year', 'is_current', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    list_editable = ('proficiency', 'order')
    ordering = ('category', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order', 'created_at')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description', 'tech_stack')


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('order',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_issued', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'issuer')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read',)
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Mark selected messages as read'
