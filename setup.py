
from setuptools import setup, find_packages

setup(
    name='jl-serverless',
    version='0.1.0',
    author='Arunkumar',
    author_email='arun19ict@gmail.com',
    description='A simple CLI tool to run scripts remotely in JarvisLabs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arunkumar-Dhanraj/JL-Serverless.git',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'click',
        'requests',
        'fastapi',
        'uvicorn'
    ],
    entry_points={
        'console_scripts': [
            'jl-cli=jl_serverless.cli:send_script'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Organization :: Python :: 3.11',
    ],
)
