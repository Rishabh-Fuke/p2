from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai.agents.agent_builder.base_agent import BaseAgent # No longer strictly needed if only using one agent type defined via config
# from typing import List # No longer strictly needed if not type hinting lists of agents/tasks directly here
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Test():
    """Code Review Crew"""
    # agents_config and tasks_config are loaded by CrewBase from your .yaml files

    @agent
    def code_analyzer(self) -> Agent:
        """Defines the Code Analyzer agent."""
        return Agent(
            config=self.agents_config['code_analyzer'], # type: ignore[index]
            verbose=True
        )

    @task
    def code_analysis_task(self) -> Task:
        """Defines the Code Review task."""
        return Task(
            config=self.tasks_config['code_review_task'], # type: ignore[index]
            agent=self.code_analyzer() # Updated reference
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Code Review crew"""
        return Crew(
            agents=[self.code_analyzer()],   # Updated reference
            tasks=[self.code_analysis_task()],   # Pass the task instance in a list
            process=Process.sequential,
            verbose=True
        )
