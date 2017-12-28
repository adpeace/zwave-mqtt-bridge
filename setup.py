from setuptools import setup

setup(name="zwave_mqtt_bridge",
      version="0.0.1",
      description="Bridge Z-Wave to MQTT",
      url="https://github.com/adpeace/zwave-mqtt-bridge.git",
      author="Andy Peace",
      author_email="andrew.peace@gmail.com",
      license="MIT",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          ],
      scripts=['zwave_mqtt_bridge'],
      # Requires python-openxwave, which isn't available on PyPI
      install_requires=['Louie', 'paho-mqtt', 'boilerio', 'watchdog'],
      zip_safe=False,
      )

