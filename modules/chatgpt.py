import sys
import tiktoken
from openai import OpenAI
from config.config import COLOR_DANGER, COLOR_WARNING
from config.models_pricing import MODELS_PRICING

class ChatGPT:

    def __init__(self, console, model="gpt-4o-mini", max_tokens=3000):
        self.console = console
        self.model = model
        self.openai = OpenAI()
        self.max_tokens = max_tokens
        self.encoding = tiktoken.encoding_for_model(model)

    def calculate_cost(self, prompt):
        prompt_length = len(self.encoding.encode(prompt))
        response_length = self.max_tokens
        input_price = (prompt_length * MODELS_PRICING[self.model]['input']) / 1000
        output_price = (response_length * MODELS_PRICING[self.model]['output']) / 1000
        return input_price + output_price

    def completion(self, messages, prompt):
        try:
            cost = self.calculate_cost(prompt)

            response = ''
            while response not in ['y', 'yes', 'n', 'no']:
                cost = round(cost, 2)
                self.console.print(f"\n[{COLOR_WARNING}]The cost of this request is USD {cost}.\n[/{COLOR_WARNING}]") 
                response = input('Do you want to continue? (y/n): ').lower()
                if response in ['n', 'no']:
                    sys.exit(1)

            response = self.openai.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=0.7,
                messages=messages
            )
            message =  response.choices[0].message.content
            return message
        except Exception as e:
            self.console.print(f"\n[{COLOR_DANGER}]Error: {e}\n")
            sys.exit(1)