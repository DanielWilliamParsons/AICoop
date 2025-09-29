
class Blackboard:
    def __init__(self):
        self.data = []

    def write(self, item, author):
        entry = f"{author}: {item}"
        print(f"[Blackboard] {entry}")
        self.data.append(entry)

    def read(self):
        return self.data