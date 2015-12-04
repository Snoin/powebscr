from setuptools import find_packages, setup

install_requires = {}

tests_require = {
    'pytest >= 2.8.2',
    'flake8 >= 2.5.0',
    'import-order >= 0.0.6',
}

extras_require = {
    'tests': tests_require,
}

setup(
    name='powebscr',
    version='0.0.0',
    description='Powerful Web Screenshoter',
    url='http://github.com/Snoin/powebscr',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'powebscr=powebscr.cli:main',
        ],
    }
)
