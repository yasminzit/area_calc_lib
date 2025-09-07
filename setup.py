from setuptools import setup, find_packages

setup(
    name="geometry-calculator",
    version="0.2.0",
    packages=find_packages(),
    author="Your Name",
    author_email="your.email@example.com",
    description="Простая библиотека для вычисления площадей геометрических фигур",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geometry-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": ["pytest"],
    },
)
