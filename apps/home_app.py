import os
import streamlit as st
from hydralit import HydraHeadApp

MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        code_expander = st.beta_expander('Show App Code')
        code_expander.code(
"""
import os
import streamlit as st
from hydralit import HydraHeadApp

MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        code_expander = st.beta_expander('Show Host Code')
        code_expander.code(

        )
        try:
            col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.beta_columns([1,2,2,2,1])
            
            col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)
            col_header_text.title('**Hydralit Explorer Home**')     
            if col_header_text.button('This will open a new tab and go'):
                self.do_redirect("https://hotstepper.readthedocs.io/index.html")

            _,_,col_logo, col_text,_ = st.beta_columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            col_text.subheader("This explorer has multiple applications, each application could be run individually, however where is the fun in that? Below is a sample home page that has redirection buttons within the content to jump to a particular app, or you can use the navigation menu at the top.")

            st.markdown('<br><br>',unsafe_allow_html=True)

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Cheat Sheet ➡️'):
                self.do_redirect('Cheat Sheet')
            col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            col_text.info("This application is all credit to [streamlit cheat sheet](https://github.com/daniellewisDL/streamlit-cheat-sheet), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            #The sample content in a sub-section with jump to format.
            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Sequency Denoising ➡️'):
                self.do_redirect('Sequency Denoising')
            col_logo.image(os.path.join(".","resources","denoise.png"),width=50,)
            col_text.info("This application is a quick look at some analysis of vessel queue data with discrete denoising using Sequency methods as provided by the [Hotstepper](https://github.com/TangleSpace/hotstepper) package.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Solar Mach ➡️'):
                self.do_redirect('Solar Mach')
            col_logo.image(os.path.join(".","resources","satellite.png"),width=50,)
            col_text.info("This application is all credit to [Solar-MACH](https://github.com/jgieseler/Solar-MACH), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Spacy NLP ➡️'):
                self.do_redirect('Spacy NLP')
            col_logo.image(os.path.join(".","resources","belgium.png"),width=50,)
            col_text.info("This application is all credit to [spacy-streamlit-demo](https://github.com/ines/spacy-streamlit-demo), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Uber Pickups ➡️'):
                self.do_redirect('Uber Pickups')
            col_logo.image(os.path.join(".","resources","taxi.png"),width=50,)
            col_text.info("This application is all credit to [demo-uber-nyc-pickups](https://github.com/streamlit/demo-uber-nyc-pickups), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

        
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

"""
        )
        try:
            col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.beta_columns([1,2,2,2,1])
            
            col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)
            col_header_text.title('**Hydralit Explorer Home**')     
            if col_header_text.button('This will open a new tab and go'):
                self.do_redirect("https://hotstepper.readthedocs.io/index.html")

            _,_,col_logo, col_text,_ = st.beta_columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            col_text.subheader("This explorer has multiple applications, each application could be run individually, however where is the fun in that? Below is a sample home page that has redirection buttons within the content to jump to a particular app, or you can use the navigation menu at the top.")

            st.markdown('<br><br>',unsafe_allow_html=True)

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Cheat Sheet ➡️'):
                self.do_redirect('Cheat Sheet')
            col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            col_text.info("This application is all credit to [streamlit cheat sheet](https://github.com/daniellewisDL/streamlit-cheat-sheet), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            #The sample content in a sub-section with jump to format.
            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Sequency Denoising ➡️'):
                self.do_redirect('Sequency Denoising')
            col_logo.image(os.path.join(".","resources","denoise.png"),width=50,)
            col_text.info("This application is a quick look at some analysis of vessel queue data with discrete denoising using Sequency methods as provided by the [Hotstepper](https://github.com/TangleSpace/hotstepper) package.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Solar Mach ➡️'):
                self.do_redirect('Solar Mach')
            col_logo.image(os.path.join(".","resources","satellite.png"),width=50,)
            col_text.info("This application is all credit to [Solar-MACH](https://github.com/jgieseler/Solar-MACH), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Spacy NLP ➡️'):
                self.do_redirect('Spacy NLP')
            col_logo.image(os.path.join(".","resources","belgium.png"),width=50,)
            col_text.info("This application is all credit to [spacy-streamlit-demo](https://github.com/ines/spacy-streamlit-demo), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

            _,_,col_logo, col_text,col_btn = st.beta_columns(MENU_LAYOUT)
            if col_text.button('Uber Pickups ➡️'):
                self.do_redirect('Uber Pickups')
            col_logo.image(os.path.join(".","resources","taxi.png"),width=50,)
            col_text.info("This application is all credit to [demo-uber-nyc-pickups](https://github.com/streamlit/demo-uber-nyc-pickups), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

        
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





