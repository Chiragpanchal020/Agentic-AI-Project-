import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from source.langgraphahenticai.UI.StreamlitUI.uiconfigfile import Config

class LoadStreamlitU:
    def __init__(self):
        self.config = Config() #config
        self.user_controls = {}