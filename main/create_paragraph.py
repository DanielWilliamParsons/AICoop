
import random
from AICoop.agents.Blackboard import Blackboard
from AICoop.agents.decomposer_agent import DecomposerAgent
from AICoop.agents.topic_agent import TopicAgent
from AICoop.agents.paragraph_agent import ParagraphAgent
from AICoop.agents.editor_agent import EditorAgent

def choose_next_agent(agent,agents, graph):
    edges = graph.get(agent.name, {})
    if not edges:
        return None
    names, probs = zip(*edges.items()) # Separate key-value pairs into two parallel tuples, e.g., [("ParagraphAgent", "EditorAgent"), (0.8, 0.2)]
    chosen = random.choices(names, weights=probs, k = 1)[0]
    return agents[chosen]

def main():
    task = "Create a paragraph for reading for CEFR Level B1 on the topic of daily life routines."

    graph = {
        "DecomposerAgent": {"TopicAgent": 0.7, "ParagraphAgent": 0.3},
        "TopicAgent": {"ParagraphAgent": 0.8, "EditorAgent": 0.2},
        "ParagraphAgent": {"EditorAgent": 1.0},
        "EditorAgent": {}
    }

    bb = Blackboard()
    agents = {
        "DecomposerAgent": DecomposerAgent("DecomposerAgent", graph, bb),
        "TopicAgent": TopicAgent("TopicAgent", graph, bb),
        "ParagraphAgent": ParagraphAgent("ParagraphAgent", graph, bb),
        "EditorAgent": EditorAgent("EditorAgent", graph, bb)
    }

    bb.write(task, "User")

    for step in range(10):
        agent = random.choice(list(agents.values()))
        print(f"\n[Step {step}] {agent.name} is active")

        agent.study_blackboard()
        recipient = choose_next_agent(agent, agents, graph)
        if recipient:
            agent.send_direct(f"Message about step: {step}", recipient)


if __name__ == "__main__":
    main()