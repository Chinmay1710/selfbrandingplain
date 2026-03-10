"""Views for portfolio_app."""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Education, Skill, Project, Internship, Certification
from .forms import ContactForm


def _get_profile():
    """Helper to fetch singleton Profile or return None."""
    return Profile.objects.first()


def _skill_groups(skills_qs):
    """Return skills grouped by category label."""
    groups = {}
    for skill in skills_qs:
        label = skill.get_category_display()
        if label not in groups:
            groups[label] = []
        groups[label].append(skill)
    return groups


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def home(request):
    profile = _get_profile()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'page_title': 'Home',
    }
    return render(request, 'portfolio_app/home.html', context)


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def about(request):
    profile = _get_profile()
    education = Education.objects.all()
    context = {
        'profile': profile,
        'education': education,
        'page_title': 'About',
    }
    return render(request, 'portfolio_app/about.html', context)


# ---------------------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------------------
def skills(request):
    all_skills = Skill.objects.all()
    skill_groups = _skill_groups(all_skills)
    context = {
        'skill_groups': skill_groups,
        'page_title': 'Skills',
    }
    return render(request, 'portfolio_app/skills.html', context)


# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
        'page_title': 'Projects',
    }
    return render(request, 'portfolio_app/projects.html', context)


# ---------------------------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------------------------
def experience(request):
    internships = Internship.objects.all()
    context = {
        'internships': internships,
        'page_title': 'Experience',
    }
    return render(request, 'portfolio_app/experience.html', context)


# ---------------------------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------------------------
def certifications(request):
    certs = Certification.objects.all()
    context = {
        'certifications': certs,
        'page_title': 'Certifications',
    }
    return render(request, 'portfolio_app/certifications.html', context)


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def contact(request):
    profile = _get_profile()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon. 🚀")
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'profile': profile,
        'page_title': 'Contact',
    }
    return render(request, 'portfolio_app/contact.html', context)
