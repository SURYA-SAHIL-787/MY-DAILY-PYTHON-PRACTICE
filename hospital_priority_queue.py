import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class Patient:
    priority: int
    arrival_number: int
    name: str = field(compare=False)
    condition: str = field(compare=False)


class EmergencyRoom:
    def __init__(self):
        self.patient_heap = []
        self.arrival_counter = 0

    def add_patient(self, name, condition, priority):
        if priority < 1:
            raise ValueError("Priority must be 1 or greater.")

        self.arrival_counter += 1

        patient = Patient(
            priority=priority,
            arrival_number=self.arrival_counter,
            name=name,
            condition=condition
        )

        heapq.heappush(self.patient_heap, patient)
        print(f"Patient added: {name}")

    def treat_next_patient(self):
        if not self.patient_heap:
            print("No patients are waiting.")
            return

        patient = heapq.heappop(self.patient_heap)

        print(
            f"Treating {patient.name} | "
            f"Condition: {patient.condition} | "
            f"Priority: {patient.priority}"
        )

    def show_waiting_patients(self):
        if not self.patient_heap:
            print("No patients are waiting.")
            return

        print("\nWaiting patients:")

        for patient in sorted(self.patient_heap):
            print(
                f"{patient.name} - {patient.condition} "
                f"(Priority {patient.priority})"
            )


def main():
    emergency_room = EmergencyRoom()

    emergency_room.add_patient("Arun", "High fever", 3)
    emergency_room.add_patient("Meera", "Breathing difficulty", 1)
    emergency_room.add_patient("Ravi", "Broken arm", 2)
    emergency_room.add_patient("Anu", "Chest pain", 1)

    emergency_room.show_waiting_patients()

    print("\nTreatment order:")
    emergency_room.treat_next_patient()
    emergency_room.treat_next_patient()
    emergency_room.treat_next_patient()
    emergency_room.treat_next_patient()


if __name__ == "__main__":
    main()
