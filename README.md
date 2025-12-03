# 🤖 Flinn Makers Day - Building Agentic Applications

Welcome to the Flinn Makers Day course! In this hands-on workshop, we'll collaboratively build a **Meal Planner Agent** using LangChain and LangGraph.

## 📝 Overview

This repository contains a template for building intelligent agents using LangGraph and LangChain. During the Makers Day course, we'll transform the example clinical writing agent into a meal planning assistant that can:
- Store and manage your favourite recipes
- Plan weekly meals
- Generate shopping lists
- Adhere to your dietary preferences

The repository includes:
- **Example Agent** (`example_agent`) - A reference implementation showing best practices
- **Your Agent** (`my_agent`) - Your workspace to build the meal planner agent
- **Testing Framework** - Skeleton structure for unit, integration, and evaluation tests
- **Development Tools** - Pre-configured linting, formatting, and type checking

### 🧑‍💻 Tech Stack
- **Python 3.13** - Core language
- **LangGraph** - Framework for building stateful, multi-actor LLM applications
- **LangChain** - Library for LLM integrations and interactions
- **Pydantic** - Data validation and modeling
- **Poetry** - Dependency management
- **LangSmith** - Tracing and evaluation

## 📁 Repository Structure

```
flinn-building-agentic-applications/
├── src/
│   ├── common/              # Shared utilities
│   │   ├── middleware.py    # Common middleware
│   │   └── model_identifiers.py  # Model configuration
│   ├── example_agent/       # Reference implementation
│   │   ├── agents/          # Agent implementation
│   │   │   ├── context.py   # Context schema
│   │   │   ├── main.py      # Main agent graph
│   │   │   └── state.py     # State schema
│   │   ├── prompts/         # Prompts
│   │   │   └── agent.py
│   │   └── tools/           # All agent tools
│   └── my_agent/            # Your meal planner agent
│       └── ...              # Same as example_agent
├── test/
│   ├── unit/               # Unit tests (skeleton)
│   ├── integration/        # Integration tests (skeleton)
│   └── eval/               # Evaluation tests (skeleton)
├── notebooks/              # Jupyter notebooks for experimentation
├── pyproject.toml          # Project dependencies
└── langgraph.json          # LangGraph configuration
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13
- Poetry
- OpenAI API key
- LangSmith API key (for tracing and evaluation)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd flinn-building-agentic-applications
```

2. **Install Poetry** (if not already installed)
```bash
pip install poetry
```

3. **Install dependencies**
```bash
poetry install
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```
OPENAI_API_KEY="your-openai-api-key-here"

# LangSmith Tracing Configuration
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"
LANGSMITH_API_KEY="your-langsmith-api-key-here"
LANGSMITH_PROJECT="flinn-makers-day-meal-planner"

LOG_LEVEL="ERROR"
```

**Note:** You'll receive API keys during the Makers Day course. LangSmith tracing is optional but highly recommended for debugging and understanding your agent's behavior.

## 💻 Running the Agents

### Local Development

Run the agents locally using the LangGraph development server:

```bash
poetry run langgraph dev
```

This will start the server and open LangGraph Studio in your browser, where you can:
- Interact with your meal planner agent
- Test the example agent for reference
- Monitor conversational state and agent decisions
- Inspect graph execution paths
- View trace details for each node
- Debug tool calls and responses

### Deploy to LangGraph Cloud

Once you've built and tested your meal planner agent locally, you can deploy it to LangGraph Cloud for production use:

```bash
# First, authenticate with LangGraph Cloud
langgraph cloud login

# Deploy your agent
langgraph cloud deploy
```

Your agent will be accessible via a REST API and can be integrated into other applications.

## 🧪 Testing

The project includes a testing framework with skeleton code ready for implementation:

### Unit Tests
Test individual components (tools, prompts, state management):
```bash
poetry run poe test:unit
```

### Integration/E2E Tests
Test the complete agent workflow:
```bash
poetry run poe test:integration
```

### Evaluation Tests
Run evaluation tests for specific scenarios:
```bash
PYTHONPATH=. poetry run python test/eval/<eval_name>.py
```

**Note:** The test directories contain skeleton files. During the course, you'll implement tests for your meal planner agent.

## 🧹 Code Quality

### Pre-Commit Checks

Before committing code, run the pre-commit workflow using the Cursor command `.cursor/commands/pre-commit/code-checks.md`. It will run and fix errors surfaced by the commands:

```bash
# Format code and install types
poetry run poe clean

# Run static analysis checks (Black, Flake8, Mypy, Vulture)
poetry run poe check

# Run unit tests
poetry run poe test:unit
```

### Static Analysis Tools
- **Black** - Code formatting
- **Flake8** - Linting
- **Mypy** - Type checking
- **Vulture** - Dead code detection

## 🔗 Resources

### Documentation
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) - Official LangGraph docs
- [LangChain Documentation](https://python.langchain.com/) - LangChain Python docs
- [LangSmith Documentation](https://docs.smith.langchain.com/) - Tracing and evaluation platform

### Course Materials
- **Example Agent**: Check `src/example_agent/` for a complete reference implementation
- **Your Workspace**: Build your meal planner in `src/my_agent/`
- **LangGraph Studio**: Visual debugging interface (opens automatically with `langgraph dev`)

### Helpful Commands

```bash
# Development workflow (clean, check, test)
poetry run poe dev

# Format code only
poetry run poe clean

# Run static analysis only
poetry run poe check

# Start LangGraph Studio
poetry run langgraph dev
```

## 📚 What You'll Learn

During this Makers Day course, you'll:
1. **Understand Agent Architecture** - Learn how LangGraph structures stateful AI agents
2. **Build Custom Tools** - Create tools for recipe search, meal planning, and more
3. **Design Effective Prompts** - Craft prompts that guide your agent effectively
4. **Handle State Management** - Manage conversation state and context
5. **Debug and Trace** - Use LangSmith to understand agent behavior

## 🤝 Getting Help

During the course, feel free to:
- Ask questions at any time
- Reference the `example_agent` for guidance
- Use LangGraph Studio to debug your agent
- Check LangSmith traces to understand what went wrong

Happy coding! 🚀
