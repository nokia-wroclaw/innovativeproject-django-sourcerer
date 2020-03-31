import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='django_sourcerer',
    version='1.0',
    author="nokia",
    author_email="cmarslan06@gmail.com",
    description="Django app that import and correlating data from external sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer",
    packages=setuptools.find_packages(),
    install_requires=[
        'django',
        'djangorestframework',
        'requests',
        'pyyaml',
        'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)