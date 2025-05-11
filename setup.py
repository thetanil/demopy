from setuptools import setup, find_packages

setup(
    name="demopy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest", "pytest-cov", "black", "mypy"],
    },
    entry_points={
        "console_scripts": [
            "demopy=demopy.cli:main",
        ]
    },
)