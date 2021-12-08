import setuptools

with open("readme.md","r",encoding="utf-8")as fh:
	long_decs=fh.read()

setuptools.setup(
    name="xcrypt",
    version="1.2.0",
    author="kgsensei",
    author_email="ceojeremy@rainydais.com",
    description="A Python encryption library.",
    long_description=long_decs,
    long_description_content_type="text/markdown",
    url="https://github.com/kgsensei/XCrypt",
    project_urls={
        "Bug Tracker":"https://github.com/kgsensei/XCrypt/issues",
    },classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"Natural Language :: English",
		"Topic :: Security :: Cryptography"
    ],package_dir={"":"xcrypt"},
	py_modules=["xcrypt"],
    python_requires=">=3.6",
)
