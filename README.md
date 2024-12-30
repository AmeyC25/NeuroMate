# NeuroMate
Neurosurgeon's Best Buddy 🧠🤖

Your ultimate Agentic RAG system—designed to assist neurosurgeons with precision and efficiency. CUrrent Prototype working on Gemma2-9b-it, Hybrid Search RAG system seamlessly combines semantic and syntactic search to make your tasks effortless.

How to Set Up and Run 🚀

1️⃣ Prepare Your Environment
Install an IDE: Make sure you have VS Code (or your favorite IDE).
Set Up a Virtual Environment:

python -m venv {your-venv-name}
Activate the Virtual Environment:
On Windows:
.\{your-venv-name}\Scripts\activate
On macOS/Linux:
source {your-venv-name}/bin/activate

2️⃣ Install Requirements
Download all dependencies with:


pip install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file in the root directory of your project and add the following keys:

env

GOOGLE_API_KEY=your-google-api-key  
GROQ_API_KEY=your-groq-api-key  

4️⃣ Organize Your Data
Place all the necessary PDF files in a folder named Data inside your project directory.

5️⃣ Run the Application
Start the app with:


streamlit run app.py
Features 💡
Hybrid Search (Semantic + Syntactic)
Powered by Gemma2-9b-it from Google
PDF support for efficient knowledge extraction



Pro Tip 💡: Ensure your .env file is listed in .gitignore to keep your API keys secure!

Happy Brainstorming! 🧠✨

