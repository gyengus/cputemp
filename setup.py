import setuptools
import os

if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cputemp",
    version=version,
    author="Gyengus",
    author_email="gyengus@gmail.com",
    description="Show Raspberry Pi's or Orange Pi's CPU temperature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gyengus/cputemp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        'console_scripts': [
            'cputemp = cputemp.cputemp:main'
        ]
    },
)
