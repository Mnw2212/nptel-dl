from distutils.core import setup

setup(
  name='Nptel-dl',
  version="0.1",
  author="Mayuresh Waykole",
  author_email="mayuresh2212@gmail.com",
  license='LICENSE',
  description="Command Line downloader for Course content published at nptel.ac.in",
  long_description=open('README.md').read(),
  install_requires=[
    "BeautifulSoup >= 4.00",
  ],
)
