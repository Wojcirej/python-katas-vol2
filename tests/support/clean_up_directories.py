import os
import shutil

def clean_up_directories():
    if os.path.isdir("./katas/test_kata") == True:
        shutil.rmtree("./katas/test_kata")
    if os.path.isfile("./tests/katas/test_test_kata.py") == True:
        os.remove("./tests/katas/test_test_kata.py")