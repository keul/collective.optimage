from setuptools import setup, find_packages
import os

version = '0.1.1.dev0'

setup(name='collective.optimage',
      version=version,
      description="Optimize Plone content images for Web usage",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        ],
      keywords='plone image optimization web jpegoptim optipng',
      author='keul',
      author_email='luca@keul.it',
      url='http://plone.org/products/collective.optimage',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.blob',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
