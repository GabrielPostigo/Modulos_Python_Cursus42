import sys
import os


def py_version() -> str:
    '''Return the Python version as "python3.X" (e.g. "python3.11").'''
    return f"python{sys.version_info.major}.{sys.version_info.minor}"


def site_packages(prefix: str) -> str:
    '''Return the site-packages folder inside the given Python prefix.'''
    if os.name == "nt":
        return os.path.join(prefix, "Lib", "site-packages")
    return os.path.join(prefix, "lib", py_version(), "site-packages")


def in_venv() -> None:
    '''
    Compare the current prefix with the base prefix.
    If they differ, we are inside a virtual environment.
    '''
    bo: bool = sys.prefix != sys.base_prefix
    global_path: str = site_packages(sys.base_prefix)

    if not bo:
        print("MATRIX STATUS: You're still plugged in",
              "",
              f"Current Python: {sys.executable}",
              "Virtual Environment: None detected",
              "",
              "WARNING: You're in the global environment!",
              "The machines can see everything you install",
              "",
              "Global package location:",
              global_path,
              "",
              "To enter the construct, run:",
              "python -m venv matrix_env",
              "source matrix_env/bin/activate   # On Unix",
              "matrix_env\\Scripts\\activate      # On Windows",
              "",
              "Then run this program again.",
              sep="\n")
    else:
        venv_path: str = site_packages(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct",
              "",
              f"Current Python: {sys.executable}",
              f"Virtual Environment: {os.path.basename(sys.prefix)}",
              f"Environment Path: {sys.prefix}",
              "",
              "SUCCESS: You're in an isolated environment!",
              "Safe to install packages without affecting",
              "the global system.",
              "",
              "Package installation path (venv):",
              venv_path,
              "Global package location (untouched):",
              global_path,
              sep="\n")


def display_info(bo: bool) -> None:
    print("Displays information about the current Python environment")
    if not bo:
        print("How to create a venv:",
              "python -m venv <name_project>",
              "",
              "How to activate a venv:",
              "source <name_project>/bin/activate", sep="\n")


if __name__ == "__main__":
    in_venv()
