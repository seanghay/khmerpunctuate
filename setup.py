import setuptools

with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
  name="khmerpunctuate",
  version="0.2.0",
  description="Punctuation Restoration for Khmer language",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/seanghay/khmerpunctuate",
  author="Seanghay Yath",
  author_email="seanghay.dev@gmail.com",
  license="MIT",
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Natural Language :: English",
  ],
  python_requires=">3.5",
  packages=setuptools.find_packages(exclude=["bin"]),
  package_dir={"khmerpunctuate": "khmerpunctuate"},
  package_data={"khmerpunctuate": ["tokenizer.json"]},
  include_package_data=True,
  install_requires=[
    "tokenizers",
    "tqdm",
    "onnxruntime",
    "numpy",
    "requests",
    "appdirs",
  ],
)
