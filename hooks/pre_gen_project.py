import re
import sys

REGEX_PATTERN = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_name = "{{ cookiecutter.project_name }}"

if not re.match(REGEX_PATTERN, project_name):
    print(f"ERROR: {project_name} is not a valid project name !")
    sys.exit(1)
