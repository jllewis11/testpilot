from langchain_openai import OpenAI
from langchain_together import Together
from utils.connector import select_service
import abc 

class Agent:
    def __init__(self, llm, model):
        if llm is None:
            llm = select_service()
        self.llm = llm
        if model is None:
            if llm == "openai":
                model = OpenAI(temperature=0.5)
        self.model = model


    @abc.abstractmethod
    def parse_output(self, raw_result, parsed_output):
        raise NotImplementedError()


class OpenAICodeGenerator:
    def __init__(self, model: OpenAI):
        self.model = model

    def generate_code(self, prompt: str) -> str:
        # Set up the prompt for the OpenAI model
        prompt_template = """
        Given the following python program, write a Python test program based upon the requirement, program, and TDD principles.:

        {prompt}

        Here's the Python code:
        """
        prompt_text = prompt_template.format(prompt=prompt)

        # Generate text with the OpenAI model
        response = self.model.generate(prompt_text, max_tokens=2048)

        # Parse the response and extract the generated code
        # Initialize the sanitizer
        sanitizer = Sanitizer()

        # Assume "output" is the output from TogetherAI
        output = sanitizer.sanitize_text(output)
        parsed_output = parser.parse(response.text)

        # Return the generated code
        return parsed_output
    
class TogetherCodeGenerator:
    def __init__(self, model: Together):
        self.model = model

    def generate_code(self, prompt: str) -> str:
        # Set up the prompt for the Together model
        prompt_template = """
        Given the following python program, write a Python test program based upon the requirement, program, and TDD principles.:

        {prompt}

        Here's the Python code:
        """
        prompt_text = prompt_template.format(prompt=prompt)

        # Generate text with the Together model
        response = self.model.generate(prompt_text, max_tokens=2048)

        # Parse the response and extract the generated code
        parser = StrOutputParser()
        parsed_output = parser.parse(response.text)

        # Return the generated code
        return parsed_output
