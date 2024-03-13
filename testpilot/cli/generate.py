from ..utils.parser import OpenAICodeGenerator, TogetherCodeGenerator

from langchain_openai import OpenAI
from langchain_together import Together

import typer

def generateOpenAI(file):
    openai_model = OpenAI()
    code_generator = OpenAICodeGenerator(openai_model)


def generateTogetherAI(file):
    togetherai_model = Together()
    code_generator = TogetherCodeGenerator(togetherai_model)
    print(code_generator)
    