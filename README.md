## Project Overview
**InnoVenture** is an AI agent framework based project that provides investment advice to venture capitalists for **startups**.

## Things we did
We came up with an agent framework to model a venture capitalist interacting with an **Investment Insights Manager**. The manager coordinates a team comprising of 3 other members with the job roles of **Business Metrics Analyst**, **Social Media Analyst** and **News Trend Analyst**.  
- The **Business Metrics Analyst** is responsible for providing insights to the Investment Insights Manager about the company's financial trajectory.  
- The **Social Media Analyst** is responsible for providing a clearer picture to the Investment Insights Manager about the company's social media value.  
- The **News Trend Analyst** is responsible for detailing the public image of the startup to the Investment Insights Manager.  
After taking in input from the other 3 roles, the **Investment Insights Manager** creates an analysis report with its investment advice for the venture capitalist.


## Technologies
We utilised **crewai** for our agent framework and **poetry** to manage the project.  
We utilized **Ollama Llama 3.2** model locally to create and use our agent framework.  
We utlized **SerperDevTool** as our web scraping API.  

## Citations
### Use of AI
- Utilized Chatgpt to understand how to download and run Ollama.
- Utilized Chatgpt to troubleshoot the crewai installation.
- Utilized Chatgpt to generate agent and task descriptions in the yaml files.
- Utilized Chatgpt to create the frontend part of the project (which we are not submitting).

### Tutorials followed
#### CrewAI tutorials
- [CrewAI crash course on Yt](https://www.youtube.com/watch?v=sPzc6hMg7So&pp=ygUPY3Jld2FpIHR1dG9yaWFs)
- [Official CrewAI documentation](https://docs.crewai.com/introduction)

#### Repositories referenced for coding
- [Crew AI examples](https://github.com/crewAIInc/crewAI-examples)
- [Crew AI crash course source code](https://github.com/bhancockio/crew-ai-crash-course?utm_source=convertkit&utm_medium=email&utm_campaign=Welcome%20to%20the%20AI%20Goldmine%20-%20Your%20Source%20Code%20Awaits!%20-%205630728)

### Future Improvements
- To make this more realistic and accurate, we will likely add more roles such as **Financial Analyst**, **Business Analyst**. The reasoning is that then these agents can provide the most accurate information for their niche areas, which can then be used further up the chain of the command to provide better reasoning.
- We are thinking of also adding a second team with an Investment Insights Manager. The idea is that the two Investment Insights Manager could participate in a  discussion with a senior person (probably **Head Manager**) to come to an understanding. This idea is a hypothesis, since we are not sure on whether two managers with the same agent and task descriptions will produce different output *yet*.
- Currently, we only utilized *Ollama Llama 3.2* model since it is open source and can be run locally (other models had rate limits that seemed too easy to cross over). We would like to experiment with utilizing differing models for our agents when possible (with more $$$).
- Also thinking about helper agents - for example, a **Social Media Intern** who actually collects all the statistics required and sends them to the Social Media Analyst. We are not sure yet though, the benefits of whether splitting tasks at this smaller level would outweight the costs of running another agent.
