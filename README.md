#  Paper2PPT — AI-Powered Research Paper to Presentation Agent

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

> Upload a LaTeX research paper → get a fully-themed PowerPoint presentation in minutes, powered by multi-agent AI.

---

##  Features

- **Multi-agent pipeline**: Three specialized agents (Summarizer → Creator → Designer) work in sequence
- **Two modes**: Single `.tex` file or full LaTeX project archive (`.zip` / `.tar.gz`) with embedded figures
- **LLM flexibility**: Choose from `llama-3.3-70b`, `qwen3-32b`, and more via [Groq](https://groq.com)
- **Agent transparency**: Live reasoning log in the sidebar shows what each agent is thinking
- **Themed output**: Corporate, Modern, or Research themes applied automatically

---

##  Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Paper2PPT Suite                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
    PPT Agent                 PPT Agent with Images
  (single .tex file)          (full LaTeX project archive)
          │                             │
          └──────────────┬──────────────┘
                         │
          ┌──────────────▼──────────────┐
          │       Agent Pipeline        │
          │                             │
          │  1. Summarizer Agent        │
          │     └─ Reads & chunks LaTeX │
          │     └─ Builds slide outline │
          │                             │
          │  2. Creator Agent           │
          │     └─ Calls ppt_create()   │
          │     └─ Builds .pptx file   │
          │                             │
          │  3. Designer Agent          │
          │     └─ Picks & applies theme│
          └─────────────────────────────┘
```

---

##  Demo

| Home | PPT Agent | PPT Agent with Images |
|---|---|---|
| Navigation landing page | Upload `.tex`, generate outline, approve, download | Upload `.zip`/`.tar.gz`, figures embedded automatically |

---

##  Project Structure

```
paper2ppt/
├── app.py                          # Home page & navigation
├── pages/
│   ├── 1_PPT_Agent.py             # Single .tex file agent
│   └── 2_PPT_Agent_with_Images.py # Archive-based agent with figure support
├── .streamlit/
│   └── secrets.toml               # Local secrets (gitignored)
├── requirements.txt
└── .gitignore
```

---

##  Getting Started

### Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com) (free tier available)

### Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/rahulomalur/paper2ppt.git
cd paper2ppt

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API keys
# Create .streamlit/secrets.toml:
mkdir -p .streamlit
cat > .streamlit/secrets.toml << EOF
GROQ_API_KEY_1 = "your_groq_api_key_here"
GROQ_API_KEY_2 = "your_groq_api_key_here"
EOF

# 4. Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

##  Deployment (Streamlit Community Cloud)

1. Fork or push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select this repo, set **Main file path** to `app.py`
4. In **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY_1 = "your_key"
   GROQ_API_KEY_2 = "your_key"
   ```
5. Click **Deploy**

---

##  How It Works

### PPT Agent (single `.tex`)
1. You upload a `.tex` file
2. **Summarizer Agent** chunks the LaTeX content using `LatexTextSplitter`, sends each chunk to an LLM, and combines summaries into a master outline
3. You review and approve the outline
4. **Creator Agent** converts the outline into a structured PPTX via `ppt_create` tool
5. **Designer Agent** selects and applies the best visual theme

### PPT Agent with Images (`.zip` / `.tar.gz`)
- Same pipeline as above, but automatically locates `main.tex` in your archive
- The Creator agent generates **dedicated visual slides** for each figure found in the paper — text slide + image slide pairs

---

## 🛠️Tech Stack

| Layer | Technology |
|---|---|
| UI | [Streamlit](https://streamlit.io) |
| Agent framework | [LangChain](https://langchain.com) |
| LLM provider | [Groq](https://groq.com) |
| Presentation | [python-pptx](https://python-pptx.readthedocs.io) |
| LaTeX parsing | `langchain-text-splitters` (LatexTextSplitter) |

---

##  License

MIT License — see [LICENSE](LICENSE) for details.
