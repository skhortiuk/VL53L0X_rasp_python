from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext, _build_ext


class ExtensionBuilder(build_ext):
    def get_ext_filename(self, ext_name):
        name = _build_ext.get_ext_filename(self, ext_name)
        if name.endswith(".so"):
            return f"{name.split('.')[0]}.so"

        return super().get_ext_filename(ext_name)


extension = Extension(
    'vl53l0x_api',
    define_macros=[],
    include_dirs=['.', 'Api/core/inc', 'platform/inc'],
    libraries=[],
    library_dirs=[],
    sources=['Api/core/src/vl53l0x_api_calibration.c',
             'Api/core/src/vl53l0x_api_core.c',
             'Api/core/src/vl53l0x_api_ranging.c',
             'Api/core/src/vl53l0x_api_strings.c',
             'Api/core/src/vl53l0x_api.c',
             'platform/src/vl53l0x_platform.c',
             'python_lib/vl53l0x_python.c']
)

setup(
    name='vl53l0x',
    version='1.0.0',
    description='VL53L0X sensor for raspberry PI',
    author='Serhii Khortiuk',
    author_email='khortiukserhii@ukr.net',
    url='https://github.com/skhortiuk/vl53l0x',
    long_description='''
VL53L0X sensor for raspberry PI.
''',
    ext_modules=[extension],
    package_dir={'': 'python'},
    py_modules=['vl53l0x'],
    requires=['smbus2'],
    cmdclass={'build_ext': ExtensionBuilder}
)
