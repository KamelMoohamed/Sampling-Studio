import streamlit as st
from stateManagement.stateManagement import stateManagement


class samplingWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        # get sampling value
        sampling_val = st.slider(
            "Sampling Rate", key="sampling_slider", min_value=1, max_value=20, value=5, on_change=self.change_value)

        # set sampling value to state
        if st.session_state.SamplingMode == 0:
            state.set_sampled_signal(sampleRate=sampling_val)
            state.set_reconstructed_signal()

    def change_value(self):
        #  changing mode to sampling mode
        st.session_state.SamplingMode = 0
