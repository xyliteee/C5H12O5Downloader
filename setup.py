from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize



setup(
    name='Source_Get',
    ext_modules=cythonize([
        Extension("Source_Get", ["Source_Get.pyx"]),
    ]),
)

setup(
    name='Window_Def',
    ext_modules=cythonize([
        Extension("Window_Def", ["Window_Def.pyx"]),
    ]),
)

