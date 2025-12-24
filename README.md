🐾 Pet Name Generator (LLM-Powered)

An AI-powered web application that generates creative pet names based on animal type and color using LangChain, Llama 3 (via Ollama), and Streamlit.

This project demonstrates practical usage of LLMs, prompt engineering, and modern LangChain (Runnable API) with a clean separation between UI and LLM logic.

🚀 Features

Generate five creative pet names based on:

Animal type (e.g., cow, dog, cat)

Pet color (e.g., black, white, brown)

Uses local LLM inference via Ollama (no API cost)

Built with modern LangChain 1.x Runnable architecture

Simple and interactive Streamlit UI

Clean project structure suitable for portfolio use

🧠 Tech Stack

Python

LangChain (Core + Runnable API)

Llama 3 (via Ollama)

Streamlit

Git & GitHub

📂 Project Structure
Pet-Name-Generator/
│
├── main.py                # Streamlit UI
├── langchain_helper.py    # LLM logic and prompt handling
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Prerequisites

Make sure you have the following installed:

Python 3.9+

Git

Ollama

Install Ollama

👉 https://ollama.com

Pull the model:

ollama pull llama3


Ensure Ollama is running:

ollama run llama3

📦 Installation
1. Clone the repository
git clone https://github.com/Sidharth-prog-eng/Pet-Name-Generator.git
cd Pet-Name-Generator

2. Create virtual environment
python -m venv env
source env/bin/activate   # Linux / WSL
# env\Scripts\activate    # Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run main.py


Open in browser:

http://localhost:8501

🧪 Example Prompt Logic

The LLM is prompted as follows:

“I have a cow pet. It is black in color. Suggest five cool pet names. Return only the names as a numbered list.”

This ensures:

Controlled output

Consistent formatting

Minimal hallucination

💡 Why Ollama?

Free and local LLM inference

No API keys required

Faster iteration while learning

Architecture is model-agnostic and can be easily switched to:

OpenAI

Anthropic

Azure OpenAI

🎯 Learning Outcomes

Modern LangChain (1.x) usage

Runnable-based prompt pipelines

Local LLM integration

Prompt engineering with structured outputs

Streamlit + LLM application design

Clean GitHub project hygiene

🔮 Future Improvements

Dropdown inputs for animal type and color

JSON-formatted output

Conversation memory

Multi-agent name refinement

FastAPI backend

Docker support

👤 Author

Sidharth K

GitHub: https://github.com/Sidharth-prog-eng

LinkedIn: https://www.linkedin.com/in/sidharth-k-b450542b0

📜 License

This project is open-source and available for educational purposes.
