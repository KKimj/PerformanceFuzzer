import setuptools

install_requires = [
    'numpy',
]


try:
    # $ pip install pypandoc
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setuptools.setup (
    name = 'PerformanceFuzzer',
    version = '0.0.3',
    license = 'GPL-3.0 License',

    description = 'PerformanceFuzzer',
    long_description = long_description,
    long_description_content_type='text/markdown',

    author = 'KKimj',
    author_email = 'kkimj@hanyang.ac.kr',
    url = 'https://github.com/KKimj/PerformanceFuzzer',

    install_requires=install_requires,

    py_modules=["performancefuzzer"],
    package_dir={"": "performancefuzzer"},
    packages=setuptools.find_packages(where="performancefuzzer"),
    classifiers = [
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
    ],
    python_requires='>=3',
)