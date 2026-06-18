MyAgent — Meal Planner Demo
============================

Quickstart
---------

1. Install dependencies with Poetry: `poetry install --with dev`.
2. Run the LangGraph development server and open the Studio UI:
   ```bash
   export USE_DUMMY_MODEL=true
   poetry run langgraph dev
   ```
3. Use the `my_agent` graph from the Studio to interact with the agent. Tools include:
   - `get_recipes`
   - `suggest_meal_plan`
   - `generate_shopping_list`
   - `recipe_management_*`
   - `preference_management_*`

Notes
-----
Tools that modify data (e.g., recipes and preferences) persist updates to AgentState using LangGraph's state schema. Summarization middleware compacts the conversation history. For local development, `USE_DUMMY_MODEL=true` creates a deterministic mocked model.
