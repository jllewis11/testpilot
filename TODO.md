- Prompting
    - Prompt Engineering to discover how to properly generate python test files. 
    - Do we need examples (few-shot) or can we zero-shot?
    - TDD - Coverage and requirement testing 
        - Do the test cover all lines of code or main portions? (Coverage)
        - Edge cases and accounting for input error? (Coverage)
        - Given a detailed feature request, does the function/code produce the intended results of that requirement? 
    - (Optional) - optional feedback regarding feature updates

    Tips: 
    - Models to use for production 
        codellama/CodeLlama-34b-Python-hf
        WizardLM/WizardCoder-Python-34B-V1.0
        gpt-3.5-turbo-0125
    - Use a smaller model parameter (7B) because it will be cheaper to inference.

- Generate .py files from LLM generations
    - Converting a JSON response to a test_*.py
        - pytest will recognize test_* files and automatically run those tests.
    - File structure and placement
        - If a test folder doesn't exist, create one.
        - Otherwise, add to the test folder.
    - Generating test for a specific file.py or generating tests crawling through the whole project directory
        - ex: pytest generate vs pytest generate utils.py   (Project directory vs single python file)

End of ~sprint 3/28



