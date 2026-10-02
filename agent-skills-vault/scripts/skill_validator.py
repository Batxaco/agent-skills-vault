#!/usr/bin/env python3
"""
Skill Validator Script
Validates the structure and YAML frontmatter of agent skills within the repository.
"""

import os
import sys
import yaml

SKILL_FILE_NAME = "SKILL.md"


def validate_skill_directory(skill_path: str) -> bool:
    """Validate that a skill directory contains a properly formatted SKILL.md file."""
    skill_file = os.path.join(skill_path, SKILL_FILE_NAME)
    if not os.path.exists(skill_file):
        print(f"[ERROR] Missing {SKILL_FILE_NAME} in {skill_path}")
        return False

    with open(skill_file, "r", encoding="utf-8") as file:
        content = file.read()

    if not content.startswith("---"):
        print(f"[ERROR] Invalid frontmatter in {skill_file}: Must start with YAML delimiters.")
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"[ERROR] Malformed frontmatter structure in {skill_file}.")
        return False

    try:
        frontmatter = yaml.safe_load(parts[1])
        if "name" not in frontmatter or "description" not in frontmatter:
            print(f"[ERROR] Frontmatter in {skill_file} missing mandatory 'name' or 'description' fields.")
            return False
    except yaml.YAMLError as exc:
        print(f"[ERROR] YAML parsing error in {skill_file}: {exc}")
        return False

    print(f"[SUCCESS] Validated skill: {frontmatter.get('name')}")
    return True


def main():
    """Scan root directories for skill packages and validate them."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    valid = True

    ignore_dirs = {".git", ".github", "scripts", "assets"}
    for entry in os.listdir(base_dir):
        entry_path = os.path.join(base_dir, entry)
        if os.path.isdir(entry_path) and entry not in ignore_dirs:
            for sub_entry in os.listdir(entry_path):
                sub_path = os.path.join(entry_path, sub_entry)
                if os.path.isdir(sub_path):
                    if not validate_skill_directory(sub_path):
                        valid = False

    if not valid:
        sys.exit(1)
    print("[INFO] All repository skills validated successfully.")


if __name__ == "__main__":
    main()