from setuptools import setup


setup(
    name='tangled.session',
    version='0.1a2.dev0',
    description='Tangled session integration',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=[
        'tangled',
        'tangled.session',
        'tangled.session.tests',
    ],
    install_requires=[
        'tangled>=0.1.dev0',
        'Beaker>=1.6.4',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
