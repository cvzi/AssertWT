import setuptools
import io


with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

version = None
with io.open("assertwt.py", encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("__version__"):
            version = line.split("=")[1].strip()
            version = version.replace('"', "").replace("'", "")
            break

setuptools.setup(
    name="AssertWT",
    version=version,
    license="Unlicense",
    author="cuzi",
    author_email="cuzi@openmail.cc",
    description="Run a Python script in Windows Terminal wt.exe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cvzi/AssertWT",
    py_modules=["assertwt"],
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
    ]
)
