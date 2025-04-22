import os

def load_environment_variables():
    """
    This function is used to load the environment variables from a .env file
    """
    os.environ['GOOGLE_API_KEY'] = ''

def load_constants_and_configuration():
    """
    This function is used to load the constants and configuration for the startup process.
    The files is a yaml file and will be loaded in a global variable.
    """

def load_test_cases_prompts():
    """
    This function is used to load the test cases and prompts from a csv / excel file.
    The files will be loaded in a global variable and can be accessed from anywhere in the code.
    The prompts will be organised by categories as loaded in environment variables.
    """

def start_up_parameters():
    """
    This function is used to set up the parameters for the startup process.
    It initializes a dictionary with default values for various parameters.
    """
