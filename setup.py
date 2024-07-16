from setuptools import setup, find_packages

setup(
    name='SQLiteDataCreator',
    version='1.0.0',
    author='Errahum',
    description='',
    long_description=open('README.md').read(),  # Assurez-vous d'avoir un fichier README.md
    long_description_content_type='text/markdown',
    url='https://github.com/Errahum/SQLite-data-creator',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'pandas',
        'pyarrow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'SQLiteDataCreator=main_sql_lite:main_sql',  # Assurez-vous que la fonction principale de main.py est appelée 'main'
        ],
    },
    include_package_data=True,  # Pour inclure des fichiers supplémentaires comme des fichiers de données
    license='MIT',
)
