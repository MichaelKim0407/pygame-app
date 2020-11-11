from setuptools import setup, find_packages

from pygame_app import __version__

setup(
    name='pygame-app',
    version=__version__,
    # description='',

    # url='',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    packages=find_packages(),

    # python_requires='>=3.6',

    install_requires=[
        'pygame==2.*',
    ],

    classifiers=[
        'Intended Audience :: Developers',

        'Development Status :: 1 - Planning',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: pygame',
    ],
)
