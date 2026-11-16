class ProjectElection:
    def __init__(self, projects: list[str]):
        self._projects = set(projects)
        if len(self._projects) != len(projects):
            raise ValueError("Project IDs must be unique")
        self._counts = {project: [0] * len(projects) for project in projects}

    def add_ballot(self, ballot: list[str]) -> None:
        if len(ballot) != len(self._projects) or set(ballot) != self._projects:
            raise ValueError("Each ballot must rank every project exactly once")

        for position, project in enumerate(ballot):
            self._counts[project][position] += 1

    def ranking(self) -> list[str]:
        return sorted(
            self._projects,
            key=lambda project: ([-count for count in self._counts[project]], project),
        )


if __name__ == "__main__":
    election = ProjectElection(["API", "UI", "DB"])
    ballots = [
        ["API", "UI", "DB"],
        ["API", "DB", "UI"],
        ["UI", "DB", "API"],
        ["DB", "API", "UI"],
    ]

    for ballot in ballots:
        election.add_ballot(ballot)

    print(" > ".join(election.ranking()))
