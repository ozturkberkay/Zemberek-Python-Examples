#!/usr/bin/env python
import setuptools


setuptools.setup(
  name="turkishnlptool",
  version="0.0.1",
  packages=setuptools.find_packages(),
  install_requires=[
    "JPype1",
    "numpy",
    "overrides",
  ],
  package_data={'': ['zemberek-full.jar','turkish_stopwords.txt']},
    include_package_data=True,
  classifiers=[
    "Programming Language :: Python :: 3.6",
    "Topic :: Text Processing"
  ],
)
