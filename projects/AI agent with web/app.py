import uuid

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver
import gradio as gr
import sqlite3
import os
def get_date():
    """Returns the current date in YYYY-MM-DD format."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

con=sqlite3.connect("chabot.db",check_same_thread=False)
checkpointer=SqliteSaver(con)
llm=ChatOllama(model="mistral")
sp="" \
"You are a helpful assistant" \
"Use the get_date toll if the user asks for date"

agent=create_agent(model=llm,tools=[get_date],system_prompt=sp,checkpointer=checkpointer)



def chat(msg,a,thread_id):
    config={"configurable":{"thread_id":1}}
    res=agent.invoke({"messages":[{"role":"user","content":msg}]},config)
    lr=res['messages'][-1].content
    return lr

with gr.Blocks() as d:
    gr.Markdown("#AI Chatbot")
    thread_id=gr.State(value=lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat,additional_inputs=[thread_id])
d.launch()