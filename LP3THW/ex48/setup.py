try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = { 
    'description': 'My Project',
    'author': 'Major Hoffman',
    'url': 'majorhoffman.com',
    'download_url': 'Where to download it.',
    'author_email': 'me@majorhoffman.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)