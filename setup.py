from setuptools import setup

setup(
    name='git-stats-all',
    version='0.0.1',
    description="Imports all your git projects using 'git-stats-importer'",
    author='Felipe Arruda Pontes',
    author_email='contato@arruda.blog.br',
    url='https://github.com/arruda/git-stats-all',
    py_modules=['git_stats_all'],
    install_requires=[
        'click>=3.3',
    ],
    license="MIT",
    keywords='git-stats, git-stats-importer, git-stats-all',
    entry_points="""
        [console_scripts]
        git_stats_all=git_stats_all:git_stats_all
    """,
    # test_suite='tests',
    # tests_require=test_requirements
)
