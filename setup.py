import os

from setuptools import setup, find_packages

version = '1.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'gevent-socketio',
    'waitress',
    'tweepy',
    'gevent',
    ]

setup(name='wheres_the_beer',
      version=version,
      description='wheres_the_beer',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="wheres_the_beer",
      entry_points="""\
      [paste.app_factory]
      main = wheres_the_beer:main
      """,
      )
