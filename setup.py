import subprocess
import sys
from setuptools import setup

if sys.hexversion >= 0x3000000:
    dispatch_dependency = "pydispatch"
else:
    dispatch_dependency = "Louie-latest"

# Try to create an rst long_description from README.md:
try:
    args = 'pandoc', '--to', 'rst', 'README.md'
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    print("WARNING: Couldn't generate long_description - is pandoc installed?")
    long_description = None

setup(name="zwave_mqtt_bridge",
      version="0.0.3",
      description="Bridge Z-Wave to MQTT",
      url="https://github.com/adpeace/zwave-mqtt-bridge.git",
      author="Andy Peace",
      author_email="andrew.peace@gmail.com",
      license="MIT",
      long_description=long_description,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          ],
      scripts=['zwave_mqtt_bridge', 'zwave_emon_republisher'],
      install_requires=[dispatch_dependency, 'python-openzwave', 'paho-mqtt', 'watchdog'],
      zip_safe=False,
      )

