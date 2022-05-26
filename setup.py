#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Maxim Sugrobov",
    author_email='ml.sugrobov@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Telebot for article storage in DB",
    entry_points={
        'console_scripts': [
            'telegraph_history_bot=telegraph_history_bot.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='telegraph_history_bot',
    name='telegraph_history_bot',
    packages=find_packages(include=['telegraph_history_bot', 'telegraph_history_bot.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/MaximSugrobov/telegraph_history_bot',
    version='0.1.0',
    zip_safe=False,
)
