from setuptools import find_packages, setup

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    # Basic package information
    name="flag-coverage-filtering",
    version="0.1.0",
    author="Suejung Shin",
    author_email="",
    description="A package for flag coverage filtering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/flag-coverage-filtering",
    # Package discovery and dependencies
    packages=find_packages(exclude=["tests*", "docs"]),
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
    ],
    # Development dependencies
    extras_require={
        "dev": [
            "black>=23.7.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.5.1",
        ],
        "test": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
    # Entry points (CLI commands)
    entry_points={
        "console_scripts": [
            "flag-filter=flag_coverage_filtering.cli:main",
        ],
    },
    # Package metadata
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # Additional package data
    package_data={
        "flag_coverage_filtering": ["py.typed", "*.json"],
    },
    # Project URLs
    project_urls={
        "Bug Reports": "https://github.com/yourusername/flag-coverage-filtering/issues",
        "Source": "https://github.com/yourusername/flag-coverage-filtering",
    },
)
