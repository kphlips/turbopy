"""Removes extra directories after testing is completed"""
from pathlib import Path
import shutil


def test_should_remove_files():
    """Finds the parent directory (turbopy) and removes the specified files"""
    parent = Path(__file__).parents[1]
    if Path(f"{parent}/tmp").is_dir():
        shutil.rmtree(Path(f"{parent}/tmp").resolve())
    if Path(f"{parent}/default_output").is_dir():
        shutil.rmtree(Path(f"{parent}/default_output").resolve())
