import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="generic-python-template",
    version="0.0.1",
    description="A generic python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Giorgio Carta",

    package_dir={"": "./"},
    packages=[''],

    install_requires=[
        "python-dotenv==0.11.0"
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 1 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Typing :: Typed"
    ],
    entry_points={
        'console_scripts': [
            'myapp = app:main',
        ]
    }

)
