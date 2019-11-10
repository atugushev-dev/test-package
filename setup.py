from setuptools import setup

setup(name='atugushev-testpackage',
      version='0.1.12',
      description='The test Package',
      url='http://github.com/atugushev/test-package',
      install_requires=['six'],
      author='Albert Tugushev',
      author_email='albert@tugushev.ru',
      license='MIT',
      packages=['testpackage'],
      zip_safe=False)
