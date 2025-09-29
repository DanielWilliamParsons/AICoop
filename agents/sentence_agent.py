import json
import requests
from AICoop.AICoop.agents.BaseAgent import BaseAgent
from AICoop.AICoop.agents.Blackboard import Blackboard

class SentenceAgent(BaseAgent):
    """
    This agent checks sentence length and sentence readability and instructs the editor agent
    """
    def __init__(self, name, graph, blackboard: Blackboard):
        """
        Initialize the sentence agent
        """
        print("Initialize the sentence agent.")
        super().__init__(name, graph, blackboard)

    def _send_request(self, payload, agent_type, temperature=0.001, n_predict=128):
        try:
            response = requests.post(
                f"{self.server_url}/chat/completions",
                headers={"Content-Type": "application/json"},
                data = json.dumps({
                        "messages": [],
                        "chat_template_kwargs": {
                            "agent_type": agent_type,
                        },
                        "n_predict": n_predict,
                        "temperature": temperature,
                        "top_p": 0.85,
                        "logprobs": 1000,
                        "echo": False,
                        "stop": ["<|user|>", "<|system|>"]
                }),
                timeout = 30,
            )

            if response.status_code != 200:
                raise RuntimeError(f"Server error: {response.status_code} with body: {response.text[:200]}")
            return response.json()
        except Exception as e:
            print("Error: ", e)