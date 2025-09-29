import json
import requests

class DiscourseAgent:
    """
    This agent checks discourse patterns in a paragraph and instructs the Editor agent
    """
    def __init__(self):
        """
        Initialize the discourse agent
        """
        print("Initialize the discourse agent.")

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