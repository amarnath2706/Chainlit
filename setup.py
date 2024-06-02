from setuptools import find_packages, setup
setup(
    name="Zomato_Bot_Application",
    version="0.0.1",
    author="amarnath",
    author_email="amarnath.arjsd@gmail.com",
    packages=find_packages(),
    install_requires=["chainlit","notebook","ipywidgets","tqdm","python-dotenv","openai","langchain-google-genai"]

)