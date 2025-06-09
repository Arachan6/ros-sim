from setuptools import setup
import os
from glob import glob

setup(
    name='brazo_robotico',
    version='0.0.0',
    packages=['brazo_robotico'],
    data_files=[
        ('share/brazo_robotico/urdf', glob('urdf/*.xacro')),
        ('share/brazo_robotico/world', glob('world/*.sdf')),
        ('share/brazo_robotico/launch', glob('launch/*.py')),
        ('share/brazo_robotico', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_nombre',
    maintainer_email='tu_email@ejemplo',
    description='Simulación brazo en Ignition Gazebo',
    license='Apache-2.0',
)

