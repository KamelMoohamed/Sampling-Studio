from asyncio.windows_events import NULL
from logging import PlaceHolder
import streamlit as st
from matplotlib import pyplot as plt
from data_processing import processing
from UI.header import headerUI
from UI.left_navbar import leftNavBar
from UI.right_navbar import rightNavBar
from UI.center_signal_view import centerSignalView
import numpy as np
import pandas as pd



class AppUi:
    def __init__(self):
        if 'signals' not in st.session_state:
            st.session_state.signals = []
        
        if 'generatedSignals' not in st.session_state:
            st.session_state.generatedSignals = []
        
        if 'sampledSignal' not in st.session_state:
            st.session_state.sampledSignal = NULL
        
        if 'signalObject' not in st.session_state:
            self.signalObject = processing.SignalProcessing()
            st.session_state.signalObject = self.signalObject
        
        if 'fileToDownload' not in st.session_state:
            st.session_state.fileToDownload = pd.DataFrame({'t':[], 'y':[]}).to_csv(index=False).encode('utf-8')
        
        if 'fileToDownloadName' not in st.session_state:
            st.session_state.fileToDownloadName = "Untitled"
        
        if 'recCounter' not in st.session_state:
            st.session_state.recCounter = 0
        
        if 'mixCounter' not in st.session_state:
            st.session_state.mixCounter = 0

        if 'signalCounter' not in st.session_state:
            st.session_state.signalCounter = 0
        
        if 'generatedSignalCounter' not in st.session_state:
            st.session_state.generatedSignalCounter = 0

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
        st.session_state.header = headerUI()

        # layout
        cols = st.columns([0.1, 2, 0.1, 5, 0.1, 2, 0.1])
        with cols[1].container():
            st.session_state.leftNav = leftNavBar()
        with cols[3].container():
            st.session_state.graphWidget = centerSignalView()
        with cols[5].container():
            st.session_state.rightNav = rightNavBar()

    def upload_signal(self):
        try:
            filePath = self.save_file(st.session_state.signalUploader)
            st.session_state.signals.append(self.signalObject.reading_signal(filePath))
        except Exception as errorMessage:
            self.show_error(errorMessage)

    

    def delete_signal(self, signalName):
        try:
            for signal in range(len(st.session_state.signals)):
                if (st.session_state.signals[signal]['name'] == signalName):
                    st.session_state.signals = st.session_state.signals[:signal] + st.session_state.signals[signal + 1:]

            self.show_error("Please select signal to delete.")
        except:
            self.show_error("Can't Delete this signal.")

    def start_signal_drawing(self, filePath):
        try:
            self.draw_signal(self.signalObject.signal)
            st.session_state.signal = self.signalObject

        except Exception as errorMessage:
            self.show_error(errorMessage)



    def draw_signal(self, signal):
        try:
            st.session_state.graphWidget.draw_signal(signal)
        except:
            raise ValueError("The Input Data isn't a signal, and Can't be plotted.")

    def draw_sampled_signal(self, signal):
        try:
            st.session_state.graphWidget.draw_sampled_signal(signal)
        except:
            raise ValueError("The Input Data isn't a signal, and Can't be plotted.")

    def show_error(self, errorMessage):
        st.error(errorMessage)
    