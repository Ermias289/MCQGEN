import json
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain

#loading json file
with open('C:\Complete_Content\All_Project\TEST_FOR_EVERYTHING\langchain\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#print(RESPONSE_JSON)