import heapq


class Patient:
    def __init__(self, name, age, priority):
        self.name = name
        self.age = age
        self.priority = priority

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Priority: {self.priority}"


class Hospital:
    def __init__(self):
        self.patient_queue = []
        self.counter = 0

    def add_patient(self, patient):
        heapq.heappush(
            self.patient_queue,
            (patient.priority, self.counter, patient)
        )

        self.counter += 1

        print(f"{patient.name} added to the patient queue.")

    def treat_next_patient(self):
        if not self.patient_queue:
            print("No patients waiting.")
            return

        priority, order, patient = heapq.heappop(self.patient_queue)

        print("\nTreating Patient:")
        print(patient)

    def display_waiting_patients(self):
        if not self.patient_queue:
            print("No patients waiting.")
            return

        print("\nPatients Waiting:")

        sorted_queue = sorted(self.patient_queue)

        for priority, order, patient in sorted_queue:
            print(patient)


hospital = Hospital()

hospital.add_patient(Patient("Arun", 45, 3))
hospital.add_patient(Patient("Meera", 67, 1))
hospital.add_patient(Patient("Kiran", 32, 4))
hospital.add_patient(Patient("Ananya", 20, 2))

hospital.display_waiting_patients()

hospital.treat_next_patient()
hospital.treat_next_patient()

hospital.display_waiting_patients()
