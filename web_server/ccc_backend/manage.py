#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

root_dir_name = "ccc_backend"
dir_path = os.path.abspath(sys.argv[0])
root_dir = dir_path[:dir_path.lower().find(root_dir_name) + len(root_dir_name)]
sys.path.insert(0, root_dir)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccc_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
