from datetime import datetime


class Evidence:
    def __init__(self, evidence_id, description, initial_holder):
        self.evidence_id = evidence_id
        self.description = description
        self.current_holder = initial_holder
        self.__transfer_history = []

        self.__record_transfer("SYSTEM", initial_holder)

    def __record_transfer(self, from_person, to_person):
        transfer = {
            "from": from_person,
            "to": to_person,
            "time": datetime.now()
        }

        self.__transfer_history.append(transfer)

    def transfer(self, new_holder):
        if new_holder == self.current_holder:
            print("Transfer rejected: Evidence is already with this person.")
            return

        old_holder = self.current_holder
        self.current_holder = new_holder
        self.__record_transfer(old_holder, new_holder)

        print(f"Evidence transferred to {new_holder}.")

    def display_chain_of_custody(self):
        print(f"\nEvidence ID: {self.evidence_id}")
        print(f"Description: {self.description}")

        for transfer in self.__transfer_history:
            time = transfer["time"].strftime("%d-%m-%Y %H:%M:%S")

            print(
                f"{transfer['from']} -> {transfer['to']} "
                f"at {time}"
            )


evidence = Evidence(
    "EV-404",
    "Damaged encrypted storage drive",
    "Officer Arun"
)

evidence.transfer("Cyber Lab")
evidence.transfer("Forensic Analyst")
evidence.transfer("Evidence Vault")

evidence.display_chain_of_custody()
