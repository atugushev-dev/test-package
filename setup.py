from setuptools import setup

setup(name='testpackage',
      version='0.1',
      description='The test Package',
      url='http://github.com/atugushev/test-package',
      install_requires=['azure-common', 'azure-mgmt-compute'],
      author='Albert Tugushev',
      author_email='albert@tugushev.ru',
      license='MIT',
      packages=['testpackage'],
      zip_safe=False)
