# GenAI - Multi-Application AI Project Suite

A comprehensive suite of Generative AI applications built with LangChain, leveraging multiple LLM providers and vector databases for various use cases including RAG systems, chatbots, and data retrieval applications.

**Author:** [@dctn](https://github.com/dctn)  
**Version:** 0.1.0

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Applications](#applications)
- [Notebooks](#notebooks)
- [Dependencies](#dependencies)
- [File & Folder Details](#file--folder-details)
- [Usage](#usage)
- [Contributing](#contributing)

---

## 🎯 Project Overview

This project is a comprehensive exploration of Generative AI technologies, focusing on:

1. **Retrieval-Augmented Generation (RAG)** - Systems that retrieve and augment responses using external data sources
2. **LLM Integration** - Seamless integration with multiple LLM providers (Groq, Google Generative AI, OpenRouter)
3. **Vector Databases** - Efficient storage and retrieval of embeddings using ChromaDB and FAISS
4. **Web Scraping & Data Processing** - Processing of unstructured data from URLs and documents
5. **Exam Question Retrieval** - TNPSC (Tamil Nadu Public Service Commission) exam question matching system
6. **Real-time Monitoring** - Amazon product price monitoring and notification system

---

## ⭐ Key Features

- 🤖 **Multi-Provider LLM Support** - Groq, Google Generative AI, OpenRouter, LangChain OpenAI
- 📚 **RAG System** - Retrieval-Augmented Generation for context-aware responses
- 🗄️ **Vector Database Integration** - ChromaDB and FAISS for efficient similarity search
- 🌐 **Web Interface** - Streamlit-based interactive applications
- 📄 **Document Processing** - PDF, text, and web content loading and chunking
- 🔗 **URL Web Scraping** - Dynamic content extraction from websites using BeautifulSoup
- 💾 **Multiple Data Sources** - Hugging Face datasets, ChromaDB, FAISS
- 🔍 **Similarity Search** - Find semantically similar questions and documents
- ⚙️ **HuggingFace Embeddings** - sentence-transformers for semantic similarity

---

## 📁 Project Structure

```
GEN AI/
├── 📄 README.md                          # Project documentation (this file)
├── 📄 main.py                            # Main entry point
├── 📄 pyproject.toml                     # Project configuration and dependencies
├── 📄 controller_price_alter.py          # Amazon price monitoring tool
├── 📄 starter.ipynb                      # Starter notebook for experimentation
├── 📊 .python-version                    # Python version specification
├── 📦 .venv/                             # Virtual environment
├── 🔐 .env                               # Environment variables (API keys)
│
├── 📂 apps/                              # Streamlit applications
│   ├── simple_llm.py                     # URL Q&A chatbot application
│   └── TNPSC_retrevial_system.py         # TNPSC exam question retrieval system
│
├── 📂 notebook/                          # Jupyter notebooks for experimentation
│   ├── starter.ipynb                     # Initial setup and exploration
│   ├── simple__llm_app.ipynb             # Simple LLM app development
│   ├── chatbot_history.ipynb             # Chatbot with conversation history
│   ├── tnpsc_RAG.ipynb                   # TNPSC RAG system notebook
│   ├── 📂 chroma_exam_db/                # ChromaDB storage for exam questions
│   │   ├── chroma.sqlite3
│   │   └── 7ecb70f5-a47b-43fd-97f2-22aa8a94057e/
│   ├── 📂 chromadb_text_docs/            # ChromaDB storage for text documents
│   │   ├── chroma.sqlite3
│   │   └── ac7dcb6c-ecd4-4126-909f-f7d5914ba11d/
│   └── 📂 faiss/                         # FAISS vector index
│       └── faiss_index.faiss
│
├── 📂 files/                             # Data and resource files
│   ├── artificial_intelligence.txt       # AI reference text
│   ├── index.html                        # HTML index file
│   ├── index_raw.txt                     # Raw index text
│   ├── openapi.json                      # OpenAPI specification
│   ├── test.txt                          # Test data
│   ├── gigr.pdf                          # PDF document
│   └── 📂 tnpsc/                         # TNPSC dataset
│       └── 📂 train/                     # Training dataset
│           ├── data-00000-of-00001.arrow # Arrow format data
│           ├── dataset_info.json         # Dataset metadata
│           └── state.json                # Dataset state
│       └── dataset_dict.json             # Dataset dictionary
│
├── 📂 chromadb_text_docs/                # ChromaDB storage (root level)
│   ├── chroma.sqlite3                    # SQLite database
│   └── 757c8160-e859-466d-b81a-5f900849f744/ # Collection storage
│
├── 📂 artifacts/                         # Generated artifacts
│   └── simple_llm.txt                    # Output from simple LLM
│
├── 📄 perfect_Resume_i.pdf               # Resume document
├── 📄 perfect_Resume_2.pdf               # Resume document
├── 📄 resume.pdf                         # Resume document
├── 📄 a_my_resume.pdf                    # Resume document
├── 📄 full_stack.pdf                     # Full-stack documentation
├── 🔒 .env                               # Environment variables (API keys)
├── 📝 .gitignore                         # Git ignore rules
├── 📚 pyproject.toml                     # Python project manifest
├── 📦 uv.lock                            # Dependency lock file
└── 📂 .idea/                             # PyCharm IDE configuration
```

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip or uv package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository:**
```bash
git clone <repository-url>
cd "GEN AI"
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -e .
# Or using uv:
uv sync
```

4. **Configure environment variables:**
   Create a `.env` file in the root directory with the following:
```env
HUGGING_FACE_TOKEN=your_hugging_face_token
GOOGLE_API_KEY=your_google_api_key
GROQ_KEY=your_groq_api_key
OPEN_ROUTER=your_open_router_key
```

---

## ⚙️ Configuration

### API Keys Required

This project supports multiple LLM providers. Set up the following APIs as needed:

| Provider | Environment Variable | Purpose |
|----------|---------------------|---------|
| **Groq** | `GROQ_KEY` | Fast inference with open models |
| **Google Generative AI** | `GOOGLE_API_KEY` | Gemini model access |
| **OpenRouter** | `OPEN_ROUTER` | Multi-model routing |
| **HuggingFace** | `HUGGING_FACE_TOKEN` | Model and dataset access |

### Python Version

This project requires Python 3.12 or higher. Check `.python-version` file for version specification.

---

## 📱 Applications

### 1. **Simple LLM URL Q&A Chatbot** (`apps/simple_llm.py`)

**Purpose:** Web-based Q&A system that scrapes URLs and answers questions based on the retrieved content.

**Features:**
- URL content scraping using Selenium/BeautifulSoup
- Recursive text chunking (500 chars, 100 overlap)
- ChromaDB vector storage
- HuggingFace embeddings (sentence-transformers/all-MiniLM-L6-v2)
- Streamlit web interface
- Session state management for efficient retrieval

**How it works:**
1. User inputs a website URL
2. Application scrapes and processes the content
3. Text is split into chunks and converted to embeddings
4. Chunks are stored in ChromaDB vector database
5. User asks questions → retrieved relevant chunks → LLM generates answer

**Run:**
```bash
streamlit run apps/simple_llm.py
```

**Stack:**
- LangChain with Groq LLM
- WebBaseLoader for URL content
- RecursiveCharacterTextSplitter for chunking
- ChromaDB vector database
- HuggingFace embeddings

---

### 2. **TNPSC Exam Question Retrieval System** (`apps/TNPSC_retrevial_system.py`)

**Purpose:** Semantic search system for Tamil Nadu Public Service Commission (TNPSC) exam questions.

**Features:**
- Loads TNPSC exam dataset from Hugging Face
- Feature engineering to extract answers from multiple choice options
- Semantic similarity search using embeddings
- Configurable number of similar questions (3-10)
- Similarity score filtering (threshold: 0.9)
- Metadata display: options, answers, exam paper info, download links

**How it works:**
1. Load TNPSC exam questions dataset from Hugging Face
2. Extract answers from multiple-choice options
3. Convert questions to vector embeddings
4. Store in ChromaDB vector database
5. User enters a question → finds semantically similar exam questions
6. Displays top N similar questions with full metadata

**Dataset:** `snegha24/Tamil_tnpscExam` from Hugging Face

**Run:**
```bash
streamlit run apps/TNPSC_retrevial_system.py
```

**Stack:**
- Hugging Face datasets API
- Pandas for data manipulation
- HuggingFace embeddings
- ChromaDB vector storage
- Streamlit UI

**Metadata tracked:**
- Options
- Correct answer
- Original question number
- Source link
- Exam paper filename

---

### 3. **Amazon Price Monitor** (`controller_price_alter.py`)

**Purpose:** Monitors Amazon product prices and sends email notifications when prices change.

**Features:**
- Web scraping with BeautifulSoup
- Price tracking and comparison
- Email notifications via Resend API
- Handles multiple CSS selectors for price elements
- Persistent price storage

**How it works:**
1. Fetches product page from Amazon URL
2. Extracts current price using CSS selectors
3. Compares with last known price
4. Sends email if price changes
5. Updates stored price

**Configuration:**
- Update `url` variable with Amazon product link
- Set `TO_EMAIL` for notifications
- Configure Resend API key in `.env`

**Run:**
```bash
python controller_price_alter.py
```

**Technologies:**
- BeautifulSoup for HTML parsing
- Requests for HTTP requests
- Resend for email service
- Lxml for HTML processing

---

## 📓 Notebooks

### 1. **Starter Notebook** (`notebook/starter.ipynb`)

Initial exploration notebook featuring:
- PDF loading with LangChain
- Resume parsing
- Job description processing
- LLM usage tracking and cost analysis
- Integration with HuggingFace embeddings

**Use case:** Resume-JD matching and analysis

---

### 2. **Simple LLM App Notebook** (`notebook/simple__llm_app.ipynb`)

Development and testing notebook for the Simple LLM application with iterative refinements.

---

### 3. **Chatbot History Notebook** (`notebook/chatbot_history.ipynb`)

Builds a conversational chatbot with:
- Conversation history management
- Context maintenance across turns
- LLM integration with memory

---

### 4. **TNPSC RAG Notebook** (`notebook/tnpsc_RAG.ipynb`)

Development and testing of TNPSC exam question retrieval system with RAG capabilities.

---

## 📦 Dependencies

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **langchain** | >=1.2.7 | LLM framework |
| **langchain-groq** | >=1.1.1 | Groq integration |
| **langchain-google-genai** | >=4.2.0 | Google Generative AI |
| **langchain-openai** | >=1.1.7 | OpenAI integration |
| **langchain-huggingface** | >=1.2.0 | HuggingFace models |
| **langchain-chroma** | >=1.1.0 | ChromaDB integration |
| **chromadb** | >=1.4.1 | Vector database |
| **faiss-cpu** | >=1.13.2 | FAISS vector index |
| **sentence-transformers** | >=5.2.2 | Embeddings model |
| **streamlit** | >=1.54.0 | Web UI framework |
| **jupyter** | >=1.1.1 | Notebook environment |
| **pandas** | (via datasets) | Data manipulation |
| **datasets** | >=4.6.1 | Hugging Face datasets |
| **bs4** | >=0.0.2 | Web scraping |
| **pypdf** | >=6.6.1 | PDF processing |
| **requests** | >=2.32.5 | HTTP library |
| **python-dotenv** | >=1.2.1 | Environment variables |
| **lxml** | >=6.0.2 | XML/HTML processing |

See [pyproject.toml](pyproject.toml) for complete dependency list.

---

## 📂 File & Folder Details

### Root Level Files

| File | Purpose |
|------|---------|
| **main.py** | Entry point script with basic hello world |
| **controller_price_alter.py** | Amazon price monitoring utility |
| **pyproject.toml** | Project metadata and dependencies |
| **README.md** | This documentation |
| **.env** | Environment variables (API keys) - Do NOT commit |
| **.python-version** | Python version specification |
| **.gitignore** | Git ignore rules |
| **uv.lock** | Dependency lock file for reproducibility |
| **starter.ipynb** | Initial exploration notebook |

### `/apps` Directory

Streamlit applications ready for deployment:
- **simple_llm.py**: URL-based Q&A chatbot (50 lines)
- **TNPSC_retrevial_system.py**: Exam question retrieval system (90+ lines)

### `/notebook` Directory

Jupyter notebooks for development and experimentation:
- Development notebooks for each major feature
- Experiment tracking and prototyping
- Contains embedded ChromaDB and FAISS indexes

### `/files` Directory

Data and resource files:
- **tnpsc/**: TNPSC dataset (Arrow format, ~1MB)
- Text files for testing and reference
- HTML and JSON specifications
- PDF documents (full_stack.pdf, gigr.pdf)

### `/artifacts` Directory

Generated outputs from applications:
- **simple_llm.txt**: Output from simple LLM processing

### `/chromadb_text_docs` Directory

ChromaDB vector store at root level for persistent text embeddings.

### Resume PDFs

Multiple resume files for testing and matching:
- perfect_Resume_i.pdf
- perfect_Resume_2.pdf
- resume.pdf
- a_my_resume.pdf

---

## 💡 Usage Examples

### Example 1: Run Simple LLM URL Chatbot

```bash
# Terminal 1: Start the app
streamlit run apps/simple_llm.py

# In browser:
# 1. Enter URL: https://example.com
# 2. Wait for scraping
# 3. Ask question: "What is the main topic?"
# 4. Get AI-generated answer based on page content
```

### Example 2: Search TNPSC Questions

```bash
streamlit run apps/TNPSC_retrevial_system.py

# In browser:
# 1. Enter question: "What is capital of India?"
# 2. Select number of similar questions (3-10)
# 3. View similar exam questions with:
#    - Full question text
#    - All options
#    - Correct answer
#    - Similarity score
#    - Original exam paper link
```

### Example 3: Monitor Amazon Prices

```bash
# Edit controller_price_alter.py with:
# - Product URL
# - Email address
# - API keys in .env

python controller_price_alter.py
```

### Example 4: Use in Python Code

```python
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import WebBaseLoader

# Load and embed URL content
loader = WebBaseLoader("https://example.com")
docs = loader.load()

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in ChromaDB
db = Chroma.from_documents(docs, embeddings)

# Search
results = db.similarity_search("your question")
```

---

## 🔧 Development

### Adding New Applications

1. Create new `.py` file in `/apps` directory
2. Use Streamlit for UI: `import streamlit as st`
3. Integrate with LangChain components
4. Follow existing patterns for LLM and vector DB setup

### Adding New Notebooks

1. Create `.ipynb` file in `/notebook` directory
2. Use same patterns as existing notebooks
3. Document purpose and use case clearly

### Testing RAG Systems

Use the provided notebooks to test:
- Embedding quality
- Retrieval performance
- Answer generation quality
- Cost tracking with `llm_usage_tracker`

---

## 🔐 Security Notes

⚠️ **Important:**
- Never commit `.env` file with real API keys
- Keep API keys in `.env` file locally only
- Use environment variables for deployment
- Regenerate keys if accidentally exposed
- Use restricted API key scopes when possible

---

## 📊 Model Information

### Embedding Model
- **Default:** `sentence-transformers/all-MiniLM-L6-v2`
- **Dimension:** 384
- **Use:** Semantic similarity search

### LLM Models Supported
- **Groq:** `openai/gpt-oss-20b` (fast, cost-effective)
- **Google:** Gemini (via langchain-google-genai)
- **OpenAI:** GPT-3.5, GPT-4 (via OpenRouter)

### Vector Databases
- **ChromaDB:** Main vector store for embeddings
- **FAISS:** Alternative high-performance index

---

## 📈 Cost Tracking

This project includes LLM usage tracking via `llm_usage_tracker` package:

```python
from llm_usage_tracker import setup_patch, print_usage_costs

setup_patch()  # Enable tracking
# ... run your code ...
print_usage_costs()  # View costs
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit pull request

---

## 📝 License

This project is created and maintained by [@dctn](https://github.com/dctn).

---

## 🆘 Troubleshooting

### ChromaDB Issues
- Clear `.sqlite3` files if schema conflicts occur
- Ensure embeddings dimension matches stored vectors

### API Key Issues
- Verify `.env` file is in root directory
- Check `load_dotenv()` is called before accessing keys
- Ensure keys have required permissions

### Embedding Issues
- Download embedding model manually if internet issues
- Check HuggingFace token validity
- Verify sufficient disk space for model files

### Streamlit Issues
- Clear cache: `streamlit cache clear`
- Use `--logger.level=debug` for debugging
- Check port 8501 availability

---

## 📚 References

- [LangChain Documentation](https://python.langchain.com)
- [ChromaDB Documentation](https://docs.trychroma.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)

---

## 📞 Support

For issues, questions, or suggestions:
- Create an issue on GitHub
- Contact: [@dctn](https://github.com/dctn)

---

**Last Updated:** June 28, 2024  
**Status:** Active Development 🚀
