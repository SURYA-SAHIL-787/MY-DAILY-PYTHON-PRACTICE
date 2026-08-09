class ZombieScanner:
    def __init__(self):
        self.names = []
        self.suspicious = {}

    def add_person(self, name):
        self.names.append(name)

    def scan(self):
        unique_names = set(self.names)

        for name in unique_names:
            count = name.lower().count("z")

            if count > 0:
                self.suspicious[name] = count

    def display(self):
        results = []

        for name, count in self.suspicious.items():
            results.append((name, count))

        print("Suspicious People:")

        for item in results:
            print(item)


scanner = ZombieScanner()

scanner.add_person("Zara")
scanner.add_person("Alex")
scanner.add_person("Zozzy")
scanner.add_person("Alex")
scanner.add_person("Buzz")

scanner.scan()
scanner.display()
