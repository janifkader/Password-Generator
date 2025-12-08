import importlib
import subprocess
import sys

required_packages = [
    "sv_ttk",
    "pandas",
    "numpy",
    "matplotlib",
    "openpyxl"
]

def install_if_missing(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"Module '{package_name}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def get_packages():
    for pkg in required_packages:
        install_if_missing(pkg)