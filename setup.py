from setuptools import find_packages, setup

setup(
    name="saf_patterns",
    author="SberDevices",
    author_email="developer@sberdevices.ru",
    description="SAF Patterns — это плагин для SmartApp Framework, "
                "который позволяет использовать паттерны на пользовательский ввод."
                "Механизм матчинга паттернов реализован на C#, плагин требует Mono/.NET",
    long_description_content_type="text/markdown",
    license="sberpl-2",
    packages=find_packages(exclude=[]),
    package_data={
        "saf_patterns": ["lib/*.dll"]
    },
    include_package_data=True,
    install_requires=[
        'pythonnet',
        'smart_app_framework',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
