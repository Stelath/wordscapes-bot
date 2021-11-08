from setuptools import setup, find_packages
print(find_packages(include=['wordscapesbot', 'wordscapesbot.*']))
setup(
    name='wordscapesbot',
    version='1.0.0',
    packages=find_packages(include=['wordscapesbot', 'wordscapesbot.*']),
    url='https://github.com/Stelath/wordscapes-bot',
    license='GNU GPLv3',
    author='Stelath',
    author_email='',
    description='A Python Script That Solves Wordscapes Levels',
    install_requires=[
        'numpy>=1.21.3',
        'opencv-python>=4.5.4.58',
        'Pillow>=8.4.0',
        'pytesseract>=0.3.8',
        'pynput>=1.7.4'
    ],
    keywords=['wordscapes', 'bot', 'videogame', 'tesseract'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)
