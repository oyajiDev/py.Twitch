# -*- coding: utf-8 -*-
import os, glob, shutil
from setuptools import setup
from py.Twitch import __version__


__dirname = os.path.dirname(os.path.realpath(__file__))
lib_name = "py.Twitch"

with open(os.path.join(__dirname, "requirements.txt"), "r", encoding = "utf-8") as reqr:
    requires = reqr.read().strip().split("\n")

for cache_dir in glob(os.path.join(__dirname, "py", "**", "__pycache__"), recursive = True):
    shutil.rmtree(cache_dir)


setup(
    author = "oyajiDev", author_email = "this.dev.somehit@gmail.com", version = __version__,
    name = lib_name, description = "",
    long_description = open(os.path.join(__dirname, "README.md"), "r", encoding = "utf-8").read().strip(),
    url = f"https://github.com/oyajiDev/{lib_name}",
    # pip informations
    python_requires = ">=3.9",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    license = "MIT",
    # package informations
    install_requires = requires,
    setup_requires = requires,
    packages = [
        dir_path.replace(__dirname + os.path.sep, "")
        for dir_path in filter(lambda i: os.path.isdir(i) and not os.path.basename(i) == "__pycache__", glob.glob(os.path.join(__dirname, "py", "**"), recursive = True))
    ],
    package_data = {
        "": [
            "**/*.*",
            "**/**/*.*"
        ]
    },
    zip_safe = False
)
