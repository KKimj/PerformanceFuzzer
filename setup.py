import setuptools


install_requires = [
    'numpy',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name = 'PerformanceFuzzer',
    version = '0.0.1',
    license = 'MIT',
    description = 'PerformanceFuzzer',
    author = 'KKimj',
    author_email = 'kkimj@hanyang.ac.kr',
    url = 'https://github.com/KKimj/PerformanceFuzzer',

    install_requires=install_requires,

    py_modules=["performancefuzzer"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers = [
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
    ],
    python_requires='>=3',
)