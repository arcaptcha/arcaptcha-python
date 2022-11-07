from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Python package for Arcaptcha'
LONG_DESCRIPTION = 'Validate and display captcha for Arcaptcha'

# Setting up
setup(
  # the name must match the folder name 'verysimplemodule'
  name="arcaptcha-python",
  version=VERSION,
  author="ARCaptcha",
  author_email="info@arcaptcha.ir",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  packages=find_packages(),
  install_requires=["requests"],
  keywords=['captcha', 'api', 'arcaptcha'],
)
