import sys
import os


def in_venv() -> None:
    '''
    Compare the the current interpreter,
    if it is the same, you are not in a venv
    '''
    bo: bool = sys.prefix != sys.base_prefix

    if not bo:
        print("MATRIX STATUS: You're still plugged in",
              "",
              f"Current Python: {sys.executable}",
              "Virtual Environment: None detected",
              "",
              "WARNING: You're in the global environment!",
              "The machines can see everything you install",
              "",
              "To enter the construct, run:",
              "python -m venv matrix_env",
              "source matrix_env/bin/activate   # On Unix",
              "matrix_env/Scripts/activate      # On Windows",
              "",
              "Then run this program again.",
              sep="\n")
    else:
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
              "Package installation path:",
              f"{sys.prefix}/lib/python3.10/site-packages",
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


'''
    how to create a venv:
    python -m venv <name_project>

    how to activate it:
    source <name_project>/bin/activate

    how to install any package in it:
    pip install <name_package>

    how to desactivate the venv:
    desactivate

    how to Remove the venv:
    rm -rf <name_project>
'''
