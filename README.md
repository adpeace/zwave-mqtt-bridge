# Z-Wave to MQTT bridge

This utility publishes to MQTT topics when sensor reports are published
from multilevel-sensor devices on a Z-Wave network.  So far it has been
tested with the Aeotec Z-Stick and MultiSensor 6 devices.

It uses a configuration file, `/etc/sensors/config`, to determine the
MQTT host and username/password as well as topic prefix to use when
publishing sensor updates.

When a sensor sends a reading update, that update is published to the
topic `topic_prefix + "/ZWaveNode<n>"`, where `<n>` is the node ID of
the node that published the update.  The message will contain a JSON
object containing a key whose name is the type of value updated
(currently 'temperature', 'humidity', 'luminance', and 'ultraviolet' are
supported) and the value that was provided.

# Installation

You can install the Python package using `pip`, e.g. `pip install .`.

You will need to a create a configuration file, `/etc/sensors/config`
similar to the following:

```
[mqtt]
user=username
password=password
host=host running mosquitto

[emonhub]
basetopic=emon_sensors
```

Messages will be published to a topic under the `basetopic` specified,
according to the originating node on the network.

To run at startup you can use the provided example `systemd` file, which
needs to be installed in the `/etc/systemd/system` directory.  Note that
the provided example assumes that there is a user called `zwave` that
will have access to the appropriate serial device for the Z-Stick
(usually `/dev/ttyACM0`), and will create working files in that user's
home directory.  You can create this user using, for example, the
`adduser` command:

```
sudo adduser --system --no-create-home --ingroup dialout zwave
```
