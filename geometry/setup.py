from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='ULGforBox',
  version='0.0.1',
  author='SHkipperX',
  author_email='concover712@gmail.com',
  description='This is the simplest module for get area geometry figure.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/SHkipperX/ULG.git',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/SHkipperX/ULG.git'
  },
  python_requires='>=3.6'
)

