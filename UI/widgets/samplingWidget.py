import streamlit as st
from stateManagement.stateManagement import stateManagement


class samplingWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        slider_val = st.slider(
            "Sampling", key="sampling_slider", min_value=0, max_value=150)
        if slider_val:
            try:
                if slider_val != 0:
                    st.session_state.sampledSignal = st.session_state.signalObject.sample_signal(
                        st.session_state.signal, slider_val)

                    state.draw_sampled_signal()

                else:
                    st.error("Sample Rate Can't be 0 ...")
            except:

                state.draw_empty_graph()
                st.error(
                    "Error Occur in sampling, please check and try again...")

        reconstructButton = st.button("Reconstruct")
        if reconstructButton:
            try:
                if 'sampledSignal' in st.session_state:
                    st.session_state["SNR_slider"] = 0
                    if st.session_state.sampledSignal.empty:
                        st.error(
                            "Nothing to reconstruct this signal...")

                        state.draw_empty_graph()
                    else:
                        st.session_state.signal = st.session_state.signalObject.reconstruct_signal(
                            st.session_state.sampledSignal)
                        st.session_state.signalsPanel.add_signal({
                            'name': 'Reconstructed Signal {}'.format(st.session_state.recCounter),
                            'signal': st.session_state.signal
                        })

                        st.session_state.recCounter += 1

                        state.draw_signal()
            except:
                st.error("Can't Reconstruct this signal...")

                state.draw_empty_graph()
            st.experimental_rerun()