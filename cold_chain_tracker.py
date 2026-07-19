class MedicineContainer:
    def __init__(self, medicine_name, min_temp, max_temp):
        self.medicine_name = medicine_name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.__readings = []

    def record_temperature(self, temperature):
        self.__readings.append(temperature)

    def is_safe(self, temperature):
        return self.min_temp <= temperature <= self.max_temp

    @property
    def safe_percentage(self):
        if not self.__readings:
            return 0

        safe_count = sum(
            self.is_safe(temp) for temp in self.__readings
        )

        return (safe_count / len(self.__readings)) * 100

    def display_report(self):
        print(f"Medicine: {self.medicine_name}")

        for temperature in self.__readings:
            status = "SAFE" if self.is_safe(temperature) else "UNSAFE"
            print(f"{temperature}°C - {status}")

        print(f"Safe readings: {self.safe_percentage:.2f}%")


container = MedicineContainer("Insulin", 2, 8)

container.record_temperature(4)
container.record_temperature(7)
container.record_temperature(10)
container.record_temperature(3)

container.display_report()
