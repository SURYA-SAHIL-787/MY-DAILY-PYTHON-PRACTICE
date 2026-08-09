class Robot:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def reverse_message(self):
        return self.message[::-1]


class RobotCompetition:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def analyse(self):
        message_lengths = {}
        unique_words = set()
        word_counts = []

        for robot in self.robots:
            message_lengths[robot.name] = len(robot.message)

            words = robot.message.lower().split()

            for word in words:
                unique_words.add(word)

            word_counts.append((robot.name, len(words)))

            print(
                robot.name,
                "Reverse Message:",
                robot.reverse_message()
            )

        print("Message Lengths:", message_lengths)
        print("Unique Words:", unique_words)
        print("Word Counts:", word_counts)


r1 = Robot("RoboX", "Find the hidden planet")
r2 = Robot("CyberZ", "Planet has secret code")
r3 = Robot("MegaBot", "Find secret energy")

competition = RobotCompetition()

competition.add_robot(r1)
competition.add_robot(r2)
competition.add_robot(r3)

competition.analyse()
