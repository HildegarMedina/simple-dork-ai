from config.prompts import GENERATE_DORK

class DorkGenerator:
    def __init__(self, chatgpt):
        self.chatgpt = chatgpt

    def generate(self, description):
        prompt = GENERATE_DORK
        prompt = prompt.replace("{description}", description)
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
        return self.chatgpt.completion(messages)
