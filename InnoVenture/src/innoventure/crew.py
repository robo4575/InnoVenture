from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

# Uncomment the following line to use an example of a custom tool
# from innoventure.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class InnoventureCrew():
	"""Innoventure crew"""
	
	@agent
	def business_metrics_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['business_metrics_analyst'],
			tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
			llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
			verbose=False
		)
	
	@agent
	def social_media_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['social_media_analyst'],
			tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
			llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
			verbose=False
		)
	
	@agent
	def news_trend_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['news_trend_analyst'],
			tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
			llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
			verbose=False
		)
	
	@agent
	def investment_insights_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['investment_insights_manager'],
			llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
			verbose=False
		)
	
	@task
	def business_metrics_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_metrics_task'],
		)
	
	@task
	def social_media_task(self) -> Task:
		return Task(
			config=self.tasks_config['social_media_task'],
		)
	
	@task
	def news_trend_task(self) -> Task:
		return Task(
			config=self.tasks_config['news_trend_task'],
		)
	
	@task
	def investment_insights_task(self) -> Task:
		return Task(
			config=self.tasks_config['investment_insights_task'],
			output_file='report.md' #This is the file that will contain the final report
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Innoventure crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)