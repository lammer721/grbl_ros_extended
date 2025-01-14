from glob import glob
import os

import setuptools

package_name = 'grbl_ros'

setuptools.setup(
    name=package_name,
    version='0.0.16',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=[
        'pyserial',
    ],
    zip_safe=True,
    maintainer='Cody Lammer',
    maintainer_email='lammer.cody@gmail.com',
    description='ROS2 package to interface with a GRBL serial device',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'grbl_node = grbl_ros.device:main',
            'grbl_service = grbl_ros.service:main',
            'grbl_manager = grbl_ros.manager:main'
        ],
    },
)
