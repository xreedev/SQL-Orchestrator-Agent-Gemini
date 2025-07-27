# SQL Orchestrator Agent

A Python orchestrator that directs user prompts to specialized agents—SQLAgent for database queries and GenericAgent for general questions—then formats and presents results via a FinalAgent.

## Overview

* **OrchestratorAgent**: Analyzes user input and decides which agent to invoke.
* **SQLAgent**: Constructs SQL queries based on user questions and returns the query string.
* **GenericAgent**: Handles general knowledge or reasoning questions.
* **FinalAgent**: Merges raw results (from SQLAgent or GenericAgent) into a human-readable response.
* **DataBase**: Wrapper around an SQLite database providing table creation and data retrieval.

## Workflow

1. **Read Input**: Continuously prompt the user until they signal to exit.
2. **Route Prompt**: Use the OrchestratorAgent to determine if the request is a database query or a general question.
3. **Execute and Retrieve**:

   * If routed to SQLAgent, generate an SQL statement and fetch results from the DataBase.
   * If routed to GenericAgent, compute the answer directly.
4. **Finalize Response**: Pass the fetched data or computed answer to the FinalAgent to format a user-facing reply.

## Components

* **Agents**:

  * `OrchestratorAgent`: Decision-maker for routing prompts.
  * `SQLAgent`: SQL query generator with knowledge of your database schema.
  * `GenericAgent`: Handles non-SQL tasks or open-ended queries.
  * `FinalAgent`: Produces the final conversational response.

* **Database Wrapper**:

  * Automatically creates required tables (`subjects`, `teachers`, `marks`) on initialization.
  * Offers methods for inserting sample data and retrieving query results.

## Tech Stack

* **Python 3.x**: Core language for agent orchestration and database interaction.
* **SQLite**: Lightweight file-based database for storing `subjects`, `teachers`, and `marks`.
* **GeminiAgent (via `gemini_agent`)**: Base class for all AI agents (Orchestrator, SQL, Generic, Final).
* **SQLite3**: Python module for direct SQLite access.

## Basic Setup

* Ensure Python 3.x is installed and all dependencies are available.
* Place the orchestrator, agent, and database wrapper modules in your project directory.
* Initialize the `DataBase` with your database file (e.g., `school.db`).

