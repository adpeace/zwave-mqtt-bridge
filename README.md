# Z-Wave to MQTT bridge

This utility publishes to MQTT topics when sensor reports are published
from multilevel-sensor devices on a Z-Wave network, and set values when
messages are received on relevant topics.  So far it has been tested
with the Aeotec Z-Stick, MultiSensor 6, and SmartSwitch 6 devices.

The repository also includes a helper that republishes Z-Wave messages
on MQTT to topics that are compatible with JSON-format OpenEnergyMonitor
messages.

## Usage

The bridge is started by running the `zwave_mqtt_bridge` executable.
This takes a number of options, which are described in the help for the
tool:

```
usage: zwave_mqtt_bridge [-h] [-U MQTT_USER] [-p MQTT_PASS] [-d DEVICE]
                         [-u USER_PATH] [--basetopic BASETOPIC]
                         mqtt_host

MQTT interface to Z-Wave sensors.

positional arguments:
  mqtt_host             MQTT host

optional arguments:
  -h, --help            show this help message and exit
  -U MQTT_USER          MQTT username
  -p MQTT_PASS          MQTT password
  -d DEVICE, --device DEVICE
                        Path to Z-Stick device
  -u USER_PATH          Path to write user files (e.g. current Z-Wave
                        configursation
  --basetopic BASETOPIC
                        Base topic to publish/subscribe to
```

`DEVICE` is often `/dev/ttyACM0` (and this is the default value.
`BASETOPIC` defaults to `zwave`.

Once running, the tool publishes updates to
`<basetopic>/updates/<node_id>` as JSON objects, where each key is the
value that was updated, and the value is the new value it was set to.
For example, `{"Temperature": 20.5}`.

It also subscribes to `<basetopic/refresh/#>`.  The user can publish
messages to subtopics named by node ID (e.g. zwave/refresh/5) with a
list of values that they wish to refresh (e.g. `["Power"]`) (the labels
are those used by OpenZWave).  This should cause a message to the
corresponding `update` topic shortly after with the current value.

Finally, it subscribes to `<basetopic/set/#>`.  The user can publish
messages to subtopics named by node ID (e.g. zwave/set/5) with a JSON
object identifying values to be updated (e.g. `{"Switch": true}`).
These will then be set: typically they will be reflected in the
`updates` topic.

## ZWave to Emon republisher

https://github.com/adpeace/emonhub/tree/emon-pi contains a script
(`emon_mqtt_logger.py`) that subscribes to  messages published by
emonhub (a tool for capturing measurements published by
OpenEnergyMonitor devices and posting them to MQTT, amongst others) and
posts them to EmonCMS (a data storage/graphing site).

The MQTT bridge here uses a different topic structure to allow for
bi-directional communication, and the types of updates from Z-Wave
devices is much more varied that needs to be posted to EmonCMS, so I
wrote a utility (`zwave_emon_republisher`) that captures just the
relevant messages from the Z-Wave network, reformats, and reposts them
to be captured by `emon_mqtt_logger.py`.

The usage is similar to `zwave_mqtt_bridge`: simply provide MQTT host
details, and the base topics you are using for Z-Wave messages and emon
messages and it takes care of the rest.

# Installation

Install using `pip`, e.g. `pip install zwave-mqtt-bridge`.

To run at startup you can use the provided example `systemd` files,
which needs to be installed in the `/etc/systemd/system` directory.
Note that the provided example assumes that there is a user called
`zwave` that will have access to the appropriate serial device for the
Z-Stick (usually `/dev/ttyACM0`), and will create working files in that
user's home directory.  You can create this user using, for example, the
`adduser` command:

```
sudo adduser --system --no-create-home --ingroup dialout zwave
```
