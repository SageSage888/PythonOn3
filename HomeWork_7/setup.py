from setuptools import _install_setup_requires, setup, version

setup(name='useful',
      version='1',
      description='Very useful code',
      url='http://github.com/dummy_user/useful',
      author='Sage',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['useful'],
      install_requires=['markdown'],
      entry_points={'console_scripts': [
          'clean_folder = useful.start:start']}
      )
