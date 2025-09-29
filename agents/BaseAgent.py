from AICoop.AICoop.agents.Blackboard import Blackboard

class BaseAgent:
    def __init__(self, name, graph, blackboard: Blackboard):
        self.name = name
        self.graph = graph
        self.blackboard = blackboard

    def study_blackboard(self):
        """
        Agent notes the blackboard state and reacts to the state
        """
        print("Agent will note the blackboard and react to the state")

    def send_direct(self, message, recipient):
        """
        Send a message to a recipient
        """
        print(f"{self.name} -> {recipient.name}: {message}")
        recipient.receive_direct(message, self)

    def received_direct(self, message, sender):
        print(f"{self.name} received from {sender.name}: {message}")
        self.blackboard.write(f"(from {sender.name}) {message}", self.name)
