# GenAIHackathon25
# GenAI Legal Document Analyzer 📜✨

A full-stack web application that uses generative AI to demystify complex legal documents, making them understandable for everyone.

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

## The Problem

Legal documents like rental agreements, terms of service, and loan contracts are filled with dense, impenetrable jargon. This creates a significant information gap, exposing individuals and small businesses to financial and legal risks when they sign documents they don't fully understand.

## Our Solution

This tool acts as a friendly AI assistant for your legal documents. Users can upload a document and interact with it in simple, natural language. The application provides clear summaries, answers specific questions, and proactively scans for potential risks and "traps," empowering users to make informed decisions with confidence.



## Key Features

* **📄 Document Upload:** Supports PDF and plain text file uploads.
* **✍️ Instant Summaries:** Generates concise, easy-to-read summaries of long documents.
* **❓ Conversational Q&A:** Ask specific questions about the document in plain English and get answers directly sourced from the text.
* **⚠️ Proactive Risk Analysis:** A one-click scan that identifies and explains common contractual risks, such as hidden fees, automatic renewal clauses, and unfavorable terms.
* **🔐 Secure User Authentication:** User accounts and session management are handled by Clerk.

## Tech Stack

| Category      | Technology                                                                                                    |
|---------------|---------------------------------------------------------------------------------------------------------------|
| **Frontend** | ⚛️ Next.js, React, TypeScript, Tailwind CSS                                                                     |
| **Backend** | 🐍 Python, FastAPI                                                                                            |
| **AI / ML** | 🧠 Google Gemini, OpenAI Embeddings, Pinecone (Vector DB)                                                       |
| **Auth** | 🔐 Clerk                                                                                                      |
| **Deployment**| 🚀 Vercel (Frontend), Render (Backend)                                                                        |

---

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Node.js (v18 or later)
* Python (v3.9 or later)
* `git` installed on your machine

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
```
cd your-repo-name




Backend Setup (/server)
Navigate to the server directory:

```bash

cd server
Create and activate a virtual environment:
```
```Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Install Python dependencies:
```
Bash

pip install -r requirements.txt
```
Create an environment file:
Create a file named .env in the server directory and add your API keys:

Code snippet

# server/.env
```
PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
PINECONE_INDEX="your-pinecone-index-name"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
CLIENT_ORIGIN_URL="http://localhost:3000"
```
Run the backend server:

Bash
```
uvicorn main:app --reload
```
The backend will now be running on http://localhost:8000.

Frontend Setup (/client)
Navigate to the client directory (from the root):

Bash
```
cd client
```
Install npm dependencies:

Bash
```
npm install
```
Create an environment file:
Create a file named .env.local in the client directory and add your keys:

Code snippet

# client/.env.local

```
NEXT_PUBLIC_API_BASE_URL="http://localhost:8000"

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="YOUR_CLERK_PUBLISHABLE_KEY"
CLERK_SECRET_KEY="YOUR_CLERK_SECRET_KEY"
```
Run the frontend server:

Bash
```
npm run dev
```
The frontend will now be running on http://localhost:3000.
