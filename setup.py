from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open("requirements.txt") as f:
    lines = f.read().splitlines()
    requirements = list(filter(str.isalnum, map(lambda l: l.split(None, 1)[0], lines)))

optional_requirements = {
    'lint': [ 'pylint>=2.0.0' ],
    'test': [ 'pytest>=3.0.0' ]
}

setup(
    name='auscultor',
    version='0.0.1',
    description='Toy NLP module to extract topic from English text',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Daniel Arato',
    author_email='nil.the.human@gmail.com',
    url='https://github.com/nilthehuman/auscultor',
    license=license,
    packages=find_packages(exclude=('tests')),
    python_requires='>=3.6',
    extras_require=optional_requirements,
    install_requires=requirements
)
