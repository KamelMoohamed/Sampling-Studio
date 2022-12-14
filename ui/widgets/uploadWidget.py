import streamlit as st
from stateManagement.stateManagement import stateManagement


class uploadWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        try:
            # upload signal
            uploadedSignals = st.file_uploader(
                "Upload Signal", type=["csv"], key='uploadButton', on_change=self.change_upload_value)

            # set uploaded signal to state
            if (uploadedSignals is not None) and (st.session_state.Mode == 1):
                path = state.save_file(uploadedSignals)
                state.set_uploaded_signal(path=path)
        except Exception as e:
            st.error(e)

    def change_upload_value(self):
        #  changing mode to upload mode
        st.session_state.Mode = 1
