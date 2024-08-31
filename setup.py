from setuptools import find_packages, setup

setup(
    name="financebot",
    version="0.0.1",
    author="sunny",
    author_email="sunny.savita@ineuron.ai",
    packages =find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)