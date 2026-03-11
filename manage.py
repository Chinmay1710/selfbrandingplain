#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Ensure the settings module is correctly pointed to for both local and Render environments
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Optional: Log which settings are being used in the terminal (helpful for debugging Render builds)
    # print(f"Using Settings: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()