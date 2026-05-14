import sys
input = sys.stdin.readline


class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.length = 0


class SuffixAutomaton:
    def __init__(self):
        self.states = [State()]
        self.last = 0

    def extend(self, character):
        current = len(self.states)
        self.states.append(State())
        self.states[current].length = self.states[self.last].length + 1

        p = self.last

        while p != -1 and character not in self.states[p].next:
            self.states[p].next[character] = current
            p = self.states[p].link

        if p == -1:
            self.states[current].link = 0

        else:
            q = self.states[p].next[character]

            if self.states[p].length + 1 == self.states[q].length:
                self.states[current].link = q

            else:
                clone = len(self.states)
                self.states.append(State())

                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].link = self.states[q].link
                self.states[clone].length = self.states[p].length + 1

                while p != -1 and self.states[p].next.get(character) == q:
                    self.states[p].next[character] = clone
                    p = self.states[p].link

                self.states[q].link = clone
                self.states[current].link = clone

        self.last = current

    def count_distinct_substrings(self):
        answer = 0

        for state_index in range(1, len(self.states)):
            state = self.states[state_index]
            parent = self.states[state.link]
            answer += state.length - parent.length

        return answer


def main():
    s = input().strip()

    automaton = SuffixAutomaton()

    for character in s:
        automaton.extend(character)

    print(automaton.count_distinct_substrings())


if __name__ == "__main__":
    main()
