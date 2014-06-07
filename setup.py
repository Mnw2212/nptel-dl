from distutils.core import setup

setup(
  name='Nptel-dl',
  version="0.1",
  author="Mayuresh Waykole",
  author_email="mayuresh2212@gmail.com",
  license='LICENSE',
  description="Useful to download NPTEL videos",
  long_description=open('README.md').read(),
  install_requires=[
    "BeautifulSoup >= 4.00",
  ],
)
