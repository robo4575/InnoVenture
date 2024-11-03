#!/usr/bin/env python
import sys
from textwrap import dedent
from innoventure.crew import InnoventureCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    
    print("## Welcome to InnoVenture")
    print('-------------------------------')
    topic = input(
        dedent("""
      Which Startup would you like me to evaluate?
    """))
    industry = input(
        dedent("""
      What is the industry this startup is in?
    """))
    yearMonth = input(
        dedent("""
      From what month would you like me to do research? (**/****)
    """))
    inputs = {
        'topic': topic,
        'industry': industry,
        'date' : yearMonth
    }

    
    InnoventureCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        InnoventureCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        InnoventureCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        InnoventureCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
