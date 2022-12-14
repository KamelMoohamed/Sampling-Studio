import streamlit as st
from UI.views.header import headerui
from UI.views.signalsPanel import signalsPanel
from UI.views.operationsPanel import operationsPanel
from UI.views.signalGraph import signalGraph
from stateManagement.stateManagement import stateManagement


class Appui:
    def __init__(self):

        # stateManagement
        state = stateManagement()
        # config
        st.set_page_config(page_title='Sampling Studio')

        # styling injection
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        # header
        headerui()

        # layout
        cols = st.columns([0.2, 2, 0.1, 2, 0.1, 6, 0.2])
        with cols[1]:
            signalsPanel()
        with cols[3]:
            operationsPanel()
        with cols[5]:
            signalGraph()

    def show_error(self, errorMessage):
        st.error(errorMessage)
