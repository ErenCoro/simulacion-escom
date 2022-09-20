import setuptools 


setuptools.setup(
     name='mpb22p1',  
     version='0.0.1',
     author="erendira",
     author_email="ecoronab1994@gmail.com",
     description="dataframe",
     url="#",
     package_dir={"": "src"},
     packages=setuptools.find_packages(where="src"),
     install_requires=['pandas', 'numpy', 'matplotlib']
)