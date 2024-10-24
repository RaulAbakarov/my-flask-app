from setuptools import setup

setup(
    install_requires=[
        'Flask==2.1.2',
        'gunicorn==20.1.0',
        'attrs==23.2.0',
        'Werkzeug==2.0.3',
        'requests==2.28.1',
        'psycopg2-binary==2.9.5',
    ],
)
