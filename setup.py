import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_scrollable_textbox",
    version="0.0.2",
    author="Roberto Frias Nerio",
    author_email="robertofnerio@gmail.com",
    description="Scrollable textbox for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobertoFN/streamlit-scrollable-textbox",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
