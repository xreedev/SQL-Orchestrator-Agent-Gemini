from orchestrator import FinalAgent,OrchestratorAgent,SQLAgent,GenericAgent
from warehouse import DataBase

orchestrator = OrchestratorAgent()
sql_agent = SQLAgent()
generic_agent = GenericAgent()
final_agent = FinalAgent()

db = DataBase("school.db")

user_prompt = 'y'

while user_prompt != 'n' :
    user_prompt = input('\n')
    orchestrator_response = orchestrator.generate_evaluation(user_prompt)

    if orchestrator_response['user']:
        print('hi', orchestrator_response['data'])

    agent_prompt = orchestrator_response['instruction']

    if orchestrator_response['data'] == 'SQLAgent':
        sql_agent_response = sql_agent.generate_evaluation(agent_prompt)
        print('Executing :', sql_agent_response['data'])

        data = db.get_data(sql_agent_response['data'])
        final_agent_response = final_agent.generate_evaluation(agent_prompt + f'{data}')
        print('(Final Agent)', final_agent_response['data'])

    elif orchestrator_response['data'] == 'GenericAgent':
        generic_agent_response = generic_agent.generate_evaluation(agent_prompt)
        print('(Generic Agent)', generic_agent_response['data'])

