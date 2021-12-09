import setuptools
from discord_interaction import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord-interaction",
    version=__version__,
    author="HazemMeqdad",
    author_email="hazemmeqdad@gmail.com",
    description="a simple manger to discord interaction flask app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HazemMeqdad/discord-interaction",
    project_urls={
        "Bug Tracker": "https://github.com/HazemMeqdad/discord-interaction/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["discord_interaction"],
    python_requires=">=3.6",
)
