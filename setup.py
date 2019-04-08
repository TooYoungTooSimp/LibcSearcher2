import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LibcSearcher2",
    version="0.0.3",
    author="TooYoungTooSimp",
    author_email="6648049+TooYoungTooSimp@users.noreply.github.com",
    description="LibcSearcher2: Maybe a faster LibcSearcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TooYoungTooSimp/LibcSearcher2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Security",
    ],
)
