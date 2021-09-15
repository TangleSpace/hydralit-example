import streamlit as st
from hydralit import HydraHeadApp


class MyLoadingApp(HydraHeadApp):

    def run(self,app_target):

        try:
            with st.spinner("✨ this is a custom loading app, you can create your own, loading...."):
                app_target.run()
      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

