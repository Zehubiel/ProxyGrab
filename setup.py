import setuptools


with open('requirements.txt', 'r') as f:
    dependencies = [l.strip() for l in f]

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ProxyGrab",
    license="MIT",
    version="0.1",
    packages=setuptools.find_packages(),
    author="Skuzzy xD",
    author_email="techdroidroot@gmail.com",
    description="A simple package made using Python and requests to get proxies from multiple sites!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="proxyscrape proxies proxygrab proxygrab-python proxylist",
    url="http://github.com/SkuzzyxD/ProxyGrab/",
    install_requires=dependencies,
    python_requires=">=3.5"

)