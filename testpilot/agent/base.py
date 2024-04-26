from langchain_openai import OpenAI
from langchain_together import Together
from ..utils.connector import select_service
from langchain.chains import LLMChain
import abc
from rich.console import Console
from openai import OpenAI

console = Console()


class Agent:
    def __init__(self, llm, model):
        if llm is None:
            llm = select_service()
        self.llm = llm


    @abc.abstractmethod
    def parse_output(self, raw_result, parsed_output):
        raise NotImplementedError()


class OpenAICodeGenerator:
    def __init__(self, model: OpenAI):
        self.model = model

    def generate_code(self, prompt: str) -> str:
        # Set up the prompt for the OpenAI model
        console.print(prompt)
        console.print(type(self.model))
        prompt_template = """
        You are an expert programmer that helps to review Python code for bugs.
        Your task is to write 1 test to check the correctness of a function that solves a programming problem.
        Write the test in pytest format.
        Problem: {prompt}
        
        """
        output = self.model.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_template.format(prompt=prompt)}
            ],
        )

        # TODO: Parse the response and extract the generated code
        # Return the generated code
        return output.choices[0].message


class TogetherCodeGenerator:
    def __init__(self, model: Together):
        self.model = model

    def generate_code(self, prompt: str) -> str:
        # Set up the prompt for the Together model
        console.print(prompt)
        prompt_template = f"""
        write a unit test in pytest for this function:
        Function: {prompt}
        
        """
        output = self.model.invoke(prompt_template)

        # TODO: Parse the response and extract the generated code

        return output
