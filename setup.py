from setuptools import setup, find_packages

version = '1.1.dev0'

setup(name='por.karma',
      version=version,
      description="Karma integration in Penelope",
      long_description=open("README.rst").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='penelope karma trac',
      author='RedTurtle',
      author_email='svilplone@redturtle.it',
      url='http://www.redturtle.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['por'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'distribute',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
