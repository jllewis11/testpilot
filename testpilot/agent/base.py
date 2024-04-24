from langchain_openai import OpenAI
from langchain_together import Together
from ..utils.connector import select_service
from langchain.chains import LLMChain
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
        llm_chain = LLMChain(prompt=prompt, llm=self.model)
        output = llm_chain.run(prompt_template)

        # TODO: Parse the response and extract the generated code

        # Return the generated code
        return output


class TogetherCodeGenerator:
    def __init__(self, model: Together):
        self.model = model

    def generate_code(self, prompt: str) -> str:
        # Set up the prompt for the Together model
        prompt_template = """
        Your task is to write one or more tests cases to check the correctness of a function that solves a programming problem. Check if the code might have any edge cases. Restrict to only the code given.

        You must write the comment "#Test case n:" on a separate line directly above each assert statement, where n represents the test case number, starting from 1 and increasing by one for each subsequent test case.
        
        Code: {prompt}
        """
        output = self.model.invoke(prompt_template)

        # TODO: Parse the response and extract the generated code

        return output
