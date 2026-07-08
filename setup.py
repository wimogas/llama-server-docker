from setuptools import setup, find_packages

setup(
    name="lsd",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["server"],
    entry_points={
        'console_scripts': [
            'lsd=server:main',
        ],
    },

    python_requires='>=3.6',
)