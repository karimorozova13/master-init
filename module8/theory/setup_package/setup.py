from setuptools import setup,find_namespace_packages

setup(name='setup_package',
      version='1',
      description='Very useful code',
    #   url='http://github.com/dummy_user/useful',
      author='Kari Mo',
      author_email='karimorozova13@gmail.com',
      license='MIT',
    #   packages=['setup_package'],
      packages=find_namespace_packages(),
    #   install_requires=['markdown'],
      entry_points={'console_scripts': ['helloworld = setup_package.some:hello_world']})
