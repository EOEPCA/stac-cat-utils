from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='stac_cat_utils',
    version='0.1.0',
    description='Package of utility functions facilitating generation of STAC files from existing files and folders.',
    url='https://github.com/SpaceApplications/stac-cat-utils',
    author='Space Applications Services',
    author_email='sys_eos@spaceapplications.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['stac_cat_utils', 'stac_cat_utils/slc'],
    keywords='STAC, pystac, STAC generation',
    python_requires='>=3.8',
    license='BSD',
    install_requires=[
        'stactools==0.4.5',
        'stactools-browse==0.1.7',
        'stactools-landsat==0.3.0',
        'stactools-sentinel1==0.5.3',
        'stactools-sentinel2==0.4.0',
        'pystac==1.7.2',
        'rio_stac==0.7.0',
        'lxml==4.9.2',
    ],
)
