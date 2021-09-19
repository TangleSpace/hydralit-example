from loaders.loaders import point_line
import time
import streamlit as st
from hydralit import HydraHeadApp
from loaders import hydralit_spinner, Loaders


class QuickLoaderApp(HydraHeadApp):

    def __init__(self, title = 'QLoader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self,app_target):

        try:
            app_title = ''
            if hasattr(app_target,'title'):
                app_title = app_target.title
            
            #with hydralit_spinner("✨ This is a custom loading app, now loading {}".format(app_title), loader_name=Loaders.tester2,height=512):
            #    time.sleep(int(self.delay))
            app_target.run()
      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

