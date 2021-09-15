from hydralit import HydraApp
import streamlit as st
import apps


if __name__ == '__main__':
    #------------all valid container references, do not initilise or page config will not be applied (this is from beta containers, beta, who knew!).
    # my_container = st.sidebar
    # my_container = st.sidebar.container
    # my_container = st.sidebar.columns
    # my_container = st
    # my_container = st.container
    # my_container = st.columns
    my_container = None

    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='Hydralit Data Explorer',favicon="🐙",nav_container=my_container,nav_horizontal=True,hide_streamlit_markers=True)
  
  #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)

    #add all your application classes here
    app.add_app("Cheat Sheet", icon="📚", app=apps.CheatApp(title="Cheat Sheet"))
    app.add_app("Sequency Denoising",icon="🔊", app=apps.WalshApp(title="Sequency Denoising"))
    app.add_app("Sequency (Secure)",icon="🔊🔒", app=apps.WalshAppSecure(title="Sequency (Secure)"))
    app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))
    app.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP(title="Spacy NLP"))
    app.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC(title="Uber Pickups"))
    app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    #app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    complex_nav = {
        'Home': ['Home'],
        'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
        'Hotstepper 🔥': ["Sequency Denoising","Sequency (Secure)"],
        'Models 🧩': ["Spacy NLP","Uber Pickups"],
    }

    # ----------USE QUERY PARAMETER NAVIGATION----------------------------------------
    # If we want to use query parameters to control the navigation, 
    # for example we could bookmark a specific app and jump straight to it.
    # --------------------------------------------------------------------------------
    query_params = st.experimental_get_query_params()
    if 'selected' in query_params:
      app.session_state.selected_app = (query_params['selected'])[0]
    # --------------------------------------------------------------------------------
    # At the top of the run() method of each child app, just 
    # add this one line and it will also update the query parameter regardless of the source of navigation
    # st.experimental_set_query_params(selected=self.title)

    #create a wrapper class
    # class MySmallApp(HydraHeadApp):

    # #wrap all your code in this method and you should be done
    #     def run(self):
    #         #--------now using query parameter nav as well as internal navigation

              st.experimental_set_query_params(selected=self.title)

    #         #-------------------existing untouched code------------------------------------------
    #         st.title('Small Application with a table and chart.')

    #         st.markdown("### Plot")
    #         df = create_table()

    #         st.line_chart(df)

    # --------------------------------------------------------------------------------

    # Run the Hydra
    app.run(complex_nav)