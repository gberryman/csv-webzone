import setuptools

with open("README.md", "r") as fh:
	long_description=fh.read()

setuptools.setup(
	name="csv-webzone",
	version="0.0.8",
	author="Geoffrey Berryman",
	author_email="geoffrey.berryman@gmail.com",
	description="A tiny webapp that will load CSV files and display them.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/geoffrey.berryman/csv-webzone",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	],
	python_requires='>=3.8',
	include_package_data=True,
	install_requires=['flask', 'matplotlib'])