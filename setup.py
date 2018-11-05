from setuptools import setup

setup(
    name='py_co_commit',
    version='0.1',
    description='An easy way to create a commit with multiple authors',
    url='https://github.com/vincentdnl/py-co-commit.git',
    author='Vincent Déniel',
    author_email='vincentdnl@users.noreply.github.com',
    license='apache-2.0',
    packages=['py_co_commit'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['py_co_commit=py_co_commit:main'],
    }
)
