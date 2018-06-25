from setuptools import setup 

exec(compile(open('zepid/version.py').read(),
                  'zepid/version.py', 'exec'))

setup(name='zepid',
    version=__version__,
    description='Tool package for epidemiologic analyses',
    keywords='epidemiology inverse probability weights risk ratio',
    license='MIT',
    author='Paul Zivich',
    author_email='zepidpy@gmail.com',
    url = 'https://github.com/pzivich/zepid',
    classifiers = ['Programming Language :: Python :: 3.5'],
    install_requires = ['pandas>=0.18',
                        'numpy',
                        'statsmodels>=0.7.0',
                        'matplotlib>=2.0',
                        'scipy',
                        'tabulate'],
    )
