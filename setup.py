try:                                              
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex48',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts':[],
    'name': 'ex48'
}

setup(**config)


# Above is not a standard style of writing. The standard style is to call setup() function and pass parameters, for example：
# setup(
#	name='TowelStuff',
#	version='0.1.0',
#	author='J. Random Hacker',
#	author_email='jrh@example.com',
#	packages=['towelstuff', 'towelstuff.test'],
#	scripts=['bin/stowe-towels.py','bin/wash-towels.py'],       
#	url='http://pypi.python.org/pypi/TowelStuff/',
#	license='LICENSE.txt',
#	description='Useful towel-related stuff.',
#	long_description=open('README.txt').read(),
#	install_requires=[
#		"Django >= 1.1.1",
#		"caldav == 0.1.4",
#	],

