from setuptools import setup, find_packages


setup(
    name='mkdocs-markdown-filter',
    version='0.1.0',
    description='A MkDocs plugin to add a markdown filter to jinja templates.',
    long_description='',
    keywords='mkdocs jinja',
    url='https://github.com/byrnereese/mkdocs-markdown-filter',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'markdown-filter = mkdocs_markdown_filter.plugin:MarkdownFilterPlugin'
        ]
    }
)
