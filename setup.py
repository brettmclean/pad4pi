from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name="pad4pi",
    version="1.1.5",
    description="Interrupt-based matrix keypad library for Raspberry Pi",
    long_description=readme(),
    url="https://github.com/brettmclean/pad4pi",
    keywords="raspberry pi matrix keypad",
    author="Brett McLean",
    author_email="brettrmclean@gmail.com",
    license="LGPLv3",
    packages=["pad4pi"],
    install_requires=[
        "RPi.GPIO"
    ],
    classifiers = [
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
