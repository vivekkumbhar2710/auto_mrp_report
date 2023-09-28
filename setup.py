from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mrp_report/__init__.py
from mrp_report import __version__ as version

setup(
	name="mrp_report",
	version=version,
	description="MRP report",
	author="vivek.kumbhar@erpdata.in",
	author_email="vivek.kumbhar@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
