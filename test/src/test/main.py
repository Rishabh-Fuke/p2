#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime
from crew import Test

"""
ok now i want to the program to take in input the link to a github repo. 
Then I want my crewai agent to analyze the project in it. 
tell me how i should proceed to do this.

"""

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew after prompting the user for code input.
    """
    print("Please paste the code you want to review. Press Ctrl-D (or Ctrl-Z on Windows) then Enter when done:")
    user_code_lines = []
    while True:
        try:
            line = input()
            user_code_lines.append(line)
        except EOFError:
            break
    user_code = "\n".join(user_code_lines)

    if not user_code.strip():
        print("No code provided. Exiting.")
        return

    print("\n--- Code to be reviewed: ---")
    print(user_code)
    print("--- Starting review... ---\n")

    inputs = {
        'code_input': user_code,
    }
    
    try:
        Test().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Example code snippet for training context if needed
    example_code_train = """
def add(a, b):
    return a + b
"""
    inputs = {
        "code_input": example_code_train, 
        # "topic": "Code Reviewer", # Can be removed or adapted
        # 'current_year': str(datetime.now().year)
    }
    try:
        Test().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

# replay() and test() functions might need adjustment if their input expectations change.
# For now, they are left as is, but you might want to pass 'code_input' to them as well.

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        # Replay might not work directly with a new task structure without specific setup
        # or if the original task that was recorded used different inputs.
        print("Warning: Replay function might need adjustments for the new task structure and inputs.")
        Test().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(): # Renamed from 'test' to avoid conflict if there's a module named 'test'
    """
    Test the crew execution and returns the results.
    """
    example_code_test = """
class SimpleClass:
    pass
"""
    inputs = {
        "code_input": example_code_test,
        # "topic": "AI LLMs", # Can be removed or adapted
        # "current_year": str(datetime.now().year)
    }
    
    try:
        # Test function might also need specific inputs or LLM for evaluation
        print("Warning: Test function might need adjustments for the new task structure and inputs.")
        Test().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
    
run()