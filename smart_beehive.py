from abc import ABC, abstractmethod


class HiveSensor(ABC):
    def __init__(self, sensor_id, reading):
        self.sensor_id = sensor_id
        self.reading = reading

    @abstractmethod
    def check_status(self):
        pass


class TemperatureSensor(HiveSensor):
    def check_status(self):
        if 32 <= self.reading <= 36:
            return "Normal hive temperature"
        return "Temperature warning"


class HumiditySensor(HiveSensor):
    def check_status(self):
        if 50 <= self.reading <= 65:
            return "Normal humidity"
        return "Humidity warning"


class SoundSensor(HiveSensor):
    def check_status(self):
        if self.reading < 80:
            return "Normal bee activity"
        return "Possible hive disturbance"


sensors = [
    TemperatureSensor("TEMP-01", 35),
    HumiditySensor("HUM-02", 72),
    SoundSensor("SOUND-03", 91)
]

for sensor in sensors:
    print(
        f"{sensor.sensor_id}: "
        f"{sensor.check_status()}"
    )
