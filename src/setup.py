from setuptools import setup, find_packages

setup(
    name="apisix-client",
    version="0.1.0",
    description="Python sdk for apisix admin api",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Dominik Tkacik, Jan Tkacik",
    author_email="tkacik38@gmail.com, jan.tkacik@gmail.com, info@neuronum.sk",
    maintainer="Dominik Tkacik, Jan Tkacik",
    maintainer_email="tkacik38@gmail.com, jan.tkacik@gmail.com",
    license="MIT",
    license_files=["LICENSE"],
    keywords=["apisix", "sdk", "neuronum"],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires=">=3.9",
    install_requires=[
        "httpx >= 0.27, <1.0",
        "pyhumps >= 3.8, <4.0",
        "attrs >= 24.3, <25.0",
        "cattrs >= 24.1, <25.0",
    ],
    extras_require={
        "dev": [
            "black >= 25.0",
            "ruff >= 0.12",
            "isort >= 6.0"
        ]
    },
    packages=find_packages(),
    url="https://github.com/NeuronumOfficial/apisix-client",
    project_urls={
        "Homepage": "https://github.com/NeuronumOfficial/apisix-client",
        "Documentation": "https://github.com/NeuronumOfficial/apisix-client",
        "Repository": "https://github.com/NeuronumOfficial/apisix-client",
        "Bug Tracker": "https://github.com/NeuronumOfficial/apisix-client/issues",
    },
)
