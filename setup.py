from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-hidefield',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    version='0.2.0',
    description='hide fields in django admin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Joerg Breitbart',
    author_email='j.breitbart@netzkolchose.de',
    url='https://github.com/jerch/django-hidefield',
    download_url='https://github.com/jerch/django-hidefield/archive/0.2.0.tar.gz',
    keywords=['django', 'widget', 'admin', 'field', 'hide'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
