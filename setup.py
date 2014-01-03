from setuptools import setup, find_packages


setup(
    name='tangled.session',
    version='0.1.dev0',
    description='Tangled session integration',
    packages=find_packages(),
    install_requires=(
        'tangled>=0.1.dev0',
        'Beaker>=1.6.4',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
