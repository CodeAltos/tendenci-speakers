from setuptools import setup, find_packages

longdesc = \
'''
An addon for Tendenci for displaying speakers.
'''

setup(
    name='tendenci-speakers',
    author='Schipul',
    author_email='programmers@schipul.com',
    version='7.0.0',
    license='GPL3',
    description='Speakers addon for Tendenci',
    long_description=longdesc,
    url='https://github.com/tendenci/tendenci-speakers',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=['tendenci>=7.0.0,<8.0'],
)
