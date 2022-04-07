from setuptools import setup

setup(
 name="fakhrilak",
 version="0.0.1",
 description="Simple Package(Example) for packaging Tvb to Debian",
 author="fakhrilak",
 author_email="fakhrilak@zilog.tech",
 license="GNU",
 url="https://github.com/fakhrilak/fakhrilak",
 packages=["fakhrilak"],
 entry_points={
 "console_scripts": [
 "fakhrilak=fakhrilak:main",
 ]
 },
)