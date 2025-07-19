# 🧠 AI Research Assistant 🤖📄

Welcome to the **AI Research Assistant** – a smart, automated, and customizable CLI-based tool that helps you research topics, summarize them, and save your results using advanced LLMs 🦾 powered by 🧬 OpenAI and 📚 Wikipedia.

---

## 🚀 Features

✨ Built with **LangChain**, **OpenAI GPT-4o-mini**, and **Wikipedia/DuckDuckGo**  
📦 Outputs structured data using `Pydantic`  
💡 Automatically searches, summarizes, and stores results  
💾 Save research into timestamped `.txt` files  
🔧 Modular and extendable tooling system

---

## 🛠️ Tech Stack

| Tool/Library        | Purpose                             |
|---------------------|-------------------------------------|
| 🌐 `DuckDuckGo`     | Web search                          |
| 📚 `Wikipedia`       | Encyclopedia reference              |
| 🧠 `LangChain`       | Agent and prompt management         |
| 🤖 `OpenAI GPT-4o`   | Language model                      |
| 🧾 `Pydantic`        | Output parsing & validation         |
| 🔐 `dotenv`          | Environment variable management     |

---

## 📦 Installation

Make sure you have **Python 3.11+** installed. Then, follow these steps:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirement.txt
🔧 How to Use
🌱 Add your OpenAI API Key in a .env file like this:

ini
Copy
Edit
OPENAI_API_KEY=your_api_key_here
🧠 Run the assistant:

bash
Copy
Edit
python main.py
📝 Type your query when prompted and let the assistant do its magic!

📁 Project Structure
bash
Copy
Edit
.
├── main.py              # Entry point for research assistant
├── tools.py             # Tool definitions (save, search, wiki)
├── requirement.txt      # Python dependencies
└── .env                 # Your OpenAI API key (not tracked)
🛡️ Output Example
Here's a sample output saved in a .txt file:

---Research Output--- 
2025-07-19_10-45-32

Topic: Capital of Japan
Summary: Tokyo is the capital of Japan, known for...
Sources: ["https://en.wikipedia.org/wiki/Tokyo"]
Tools Used: ["Wikipedia", "DuckDuckGo", "Save"]
🌍 Contributing
Pull requests are welcome! Feel free to open an issue or suggest new tools and features 🛠️



Made with ❤️ using Python & AI – by [IMRAN]

Let me know if you'd like it customized further (e.g., for your GitHub username, a logo, or a demo
