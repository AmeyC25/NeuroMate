# NeuroMate
A Neurosurgeon's Best Buddy.
This is eventually going to be an Agentic RAG system which would act as a JARVIS to a Neurosurgeon.

How to run the current code?


We are currently using gemma2-9b-it model from Google for this Hybrid Search RAG system (Semantic + Syntactic)
Also, make sure that you put your pdf files in a "Data" folder in the directory(folder) of your project.

1) Ensure You have VS CODE or any other IDE you like.
2) Set-up a Virtual environment. (python -m venv {name of virenv.})
3) Download the Requirements. (pip install -r requirements.txt)
4) Create a .env file and put your Google and groq api keys there.
5) Boom, type in "streamlit run app.py".
