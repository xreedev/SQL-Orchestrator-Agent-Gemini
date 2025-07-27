from gemini_agent import GeminiAgent

class OrchestratorAgent(GeminiAgent):
    def __init__(self):
        orchestrator_prompt = (
            "You are an Orchestrator Agent. Based on the user's input, choose which agent to use:\n"
            "- Use \"SQLAgent\" if the question requires querying a structured database.Do not mention any DB schema or example as the agen is already equipped with the knowledge\n"
            "- Use \"GenericAgent\" for all other questions.\n\n"
            "Respond only with raw JSON containing exactly three keys:\n"
            "  - \"user\": false (indicating system/internal message)\n"
            "  - \"data\": either \"SQLAgent\" or \"GenericAgent\" (the chosen agent)\n"
            "  - \"instruction\": a clear, human-readable instruction describing what the next agent should do.\n\n"
            "Make the \"instruction\" sound like you are explaining to a person what the next agent will do, but DO NOT include any markdown, backticks, or extra text outside the JSON.\n\n"
            "Your response must be exactly like this example:\n"
            '{\n'
            '  "user": false,\n'
            '  "data": "SQLAgent",\n'
            '  "instruction": "Generate an SQL query based on the provided schema and user question."\n'
            '}\n'
            "or\n"
            '{\n'
            '  "user": false,\n'
            '  "data": "GenericAgent",\n'
            '  "instruction": "Answer the user question directly without SQL."\n'
            '}\n'
        )
        super().__init__(orchestrator_prompt)


class SQLAgent(GeminiAgent):
    def __init__(self):
        sql_prompt = (
            "You are a SQLAgent. You receive a user question and generate an SQL query to answer it.\n"
            "Here is the database schema:\n"
            "subjects(id, name)\n"
            "teachers(id, name, subject_id)\n"
            "marks(id, student_name, subject_id, marks)\n\n"
            "Generate an SQL query that answers the user's question.\n"
            "Respond **only** in this JSON format:\n"
            "Respond **only** with raw JSON. Do NOT include any backticks, markdown formatting, or extra text.\n"
            '{ "user": false, "data": "SELECT ..." }\n'
        )
        super().__init__(sql_prompt)

class FinalAgent(GeminiAgent):
    def __init__(self):
        final_prompt = (
            "You are a FinalAgent. You are given:\n"
            "- The original user question\n"
            "- The SQL query result (in table or list format)\n"
            "Write a helpful and human-readable answer.\n"
            "Respond strictly in this JSON format:\n"
            "Respond **only** with raw JSON. Do NOT include any backticks, markdown formatting, or extra text.\n"
            "{ \"user\": true, \"data\": \"The answer to the user is...\" }\n"
        )
        super().__init__(final_prompt)


class GenericAgent(GeminiAgent):
    def __init__(self):
        generic_prompt = (
            "You are a GenericAgent for general knowledge or reasoning tasks.\n"
            "Given a user question, answer it directly and clearly.\n"
            "Respond strictly in this JSON format:\n"
            "Respond **only** with raw JSON. Do NOT include any backticks, markdown formatting, or extra text.\n"
            "{ \"user\": true, \"data\": \"Here's the answer to your question...\" }\n"
        )
        super().__init__(generic_prompt)
