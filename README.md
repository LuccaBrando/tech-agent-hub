# Multi-Source Tech Agent Hub 🚀

An autonomous AI-driven market intelligence agent that aggregates real-time breaking tech news from top-tier US publications (TechCrunch, The Verge, Ars Technica, Wired) via structured RSS feeds. Using **LangChain** and **Groq (Llama 3.3 70B)**, the agent performs advanced venture capital-style analysis, evaluates macroeconomic/engineering impacts, and synthesizes ready-to-publish, localized content for LinkedIn audiences in both English and Brazilian Portuguese.

---

## 🧠 Architecture Overview

The system bypasses typical anti-scraping blocks by utilizing lightweight, real-time XML stream parsers. The collected data is then funneled into a cognitive orchestration layer managed by LangChain.

+-------------------------------------------------+
|               Data Layer (Python)               |
|  [TechCrunch] [The Verge] [Ars Technica] [Wired] |
+-----------------------+-------------------------+
| (RSS Feeds Parser)
v
+-------------------------------------------------+
|            Orchestration (LangChain)            |
|   - LCEL Pipeline (prompt | llm)                |
|   - System Role Constraints (VC Analyst Persona) |
+-----------------------+-------------------------+
| (Context Injection)
v
+-------------------------------------------------+
|             Inference Layer (Groq)              |
|        Model: llama-3.3-70b-versatile           |
+-----------------------+-------------------------+
| (Dual Output)
v
[LinkedIn US - Deep Tech Analysis]
[LinkedIn BR - Culturally Localized Summary]

### Key Technical Highlights
* **Agnostic LLM Layer:** Built with LangChain's unified interface (`BaseChatModel`), allowing seamless provider hot-swapping (tested across OpenAI and Groq) without altering core business logic.
* **LCEL Implementation:** Uses LangChain Expression Language (`|` pipes) to build a clean, declarative, and production-ready execution chain.
* **Advanced Prompt Engineering:** Implements strict system role isolation, transforming raw text snippets into highly structured market insights (The Headlines -> Market Outlook -> Next Steps) avoiding generic chatbot platitudes.
* **Localization over Translation:** The agent doesn't just translate text; it adapts idioms, tone, and ecosystem context specifically for the Brazilian tech community.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** LangChain (Core, Groq Integration)
* **LLM Provider:** Groq Cloud (`llama-3.3-70b-versatile`)
* **Data Ingestion:** Feedparser (RSS XML Parsing)
* **Environment Management:** Python-dotenv

---

## 🚀 Getting Started

### 1. Clone & Environment Setup
Ensure you have your virtual environment isolated and dependencies installed:

```bash
git clone <your-repository-url>
cd tech-agent-hub
python -m venv venv

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install required packages
pip install feedparser requests langchain langchain-groq python-dotenv

2. Configure API Keys
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key_here

3. Run the Agent
Execute the main agent orchestration script:
python agent.py

