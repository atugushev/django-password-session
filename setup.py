import os
import re
from setuptools import setup

VERSION = re.search(
    r"VERSION\s*=\s*['\"](.*)['\"]",
    open(os.path.join(os.path.dirname(__file__), 'password_session', '__init__.py')).read()
).group(1)

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-password-session',
    version=VERSION,
    packages=['password_session'],
    install_requires=['Django>=1.3'],
    include_package_data=True,
    license='MIT License',
    description='A reusable Django app that will invalidate all active sessions after change password.',
    long_description=README,
    url='https://github.com/atugushev/django-password-session',
    author='Albert Tugushev',
    author_email='albert@tugushev.ru',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
