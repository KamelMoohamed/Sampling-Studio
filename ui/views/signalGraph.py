import streamlit as st
import plotly.graph_objects as go


class signalGraph:
    def __init__(self):

        ##################################### Init Graph params #####################################

        self.fig = go.Figure()
        self.fig.update_layout(xaxis_title="time", yaxis_title="Amplitude")
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=500,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )
        self.fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        ##################################### Draw signal #####################################
        if (not (st.session_state.currentSignal['signal'].empty)) and (st.session_state.signalView):
            self.fig.add_trace(go.Scatter(
                x=st.session_state.currentSignal['signal'].iloc[:, 0],
                y=st.session_state.currentSignal['signal'].iloc[:, 1],
                mode='lines',
                name='signal'))

        ##################################### Draw Sampling signal #####################################

        if (not (st.session_state.sampledSignal['signal'].empty)) and (st.session_state.sampleView):
            self.fig.add_trace(go.Scatter(
                x=st.session_state.sampledSignal['signal'].iloc[:, 0],
                y=st.session_state.sampledSignal['signal'].iloc[:, 1],
                mode='markers',
                name='sample'))

        ##################################### Draw Reconstructed Signal #####################################

        if (not (st.session_state.reconstructedSignal['signal'].empty)) and (st.session_state.reconstructedview):
            self.fig.add_trace(go.Scatter(
                x=st.session_state.reconstructedSignal['signal'].iloc[:, 0],
                y=st.session_state.reconstructedSignal['signal'].iloc[:, 1],
                mode='lines',
                name='Reconstructed'))

        st.plotly_chart(self.fig, use_container_width=True)
