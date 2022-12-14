import streamlit as st
from stateManagement.stateManagement import stateManagement


class headerui:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        # setting columns
        headerCols = st.columns([1, 10, 15, 2.5, 2.5, 1.5])

        # title
        with headerCols[1]:
            st.subheader("Sampling Studio")

        # save button
        with headerCols[3]:
            saveButton = st.button('Save', key="saveBtnKey")

        # Export button
        with headerCols[4]:
            st.download_button(label='Export', mime='text/csv', file_name=(st.session_state.currentSignal['name'] + '.csv'),
                               data=st.session_state.currentSignal['signal'].to_csv(index=False).encode('utf-8'), key="ExportButton")

        # calling save signal function on button pressed
        if saveButton:
            state.save_signal()
