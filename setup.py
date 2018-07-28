import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CrawlerFriend",
    version="1.0.1",
    author="Sreejoy Halder",
    author_email="sreejoy4242@gmail.com",
    description="A light weight crawler which gives search results in HTML form or in Dictionary form,"
                " given urls and keywords.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sreejoy/CrawlerFriend",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)