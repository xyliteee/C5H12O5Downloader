from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize



setup(
    name='Source_Get',
    ext_modules=cythonize([
        Extension("Source_Get", ["Source_Get.pyx"]),
    ]),
)
