from setuptools import setup
setup(
    name='currency',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'currency=currency:run'
        ]
    }
)