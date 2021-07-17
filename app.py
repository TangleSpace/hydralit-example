import sys
sys.path.append('..')

from hydralit import HydraApp
import streamlit as st
import apps


if __name__ == '__main__':
    #------------all valid container references, do not initilise or page config will not be applied (this is from beta containers, beta, who knew!).
    #my_container = st.sidebar
    # my_container = st.sidebar.beta_container
    # my_container = st.sidebar.beta_columns
    #my_container = st
    # my_container = st.beta_container
    # my_container = st.beta_columns
    my_container = None

    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='Secure Hydralit Data Explorer',favicon="🐙",nav_container=my_container,nav_horizontal=True,hide_streamlit_markers=True)
  
    #add all your application classes here
    app.add_app("Cheat Sheet", icon="📚", app=apps.CheatApp())
    app.add_app("Sequency Denoising",icon="🔊", app=apps.WalshApp(title='Walsh Data'))
    app.add_app("Sequency Denoising1",icon="🔊", app=apps.WalshApp(title='Walsh Data'))
    app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title='Solar-MACH'))

    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True) 

    app.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC())

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!

    #app.add_app("Login", apps.LoginApp(title='Login'),is_login=True,logout_label='Piss Off 🖕')
    #YEP, JUST REMOVE THIS AND IT'S NOT LONGER NEEDING A LOGIN
    #app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    complex_nav = {
        'Home': ['Home'],
        'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
        'Hotstepper 🔥': ["Sequency Denoising","Sequency Denoising1"],
        'Models 🧩': ["Spacy NLP","Uber Pickups"],
    }
    
    #add a custom loader for app transitions
    #app.add_loader_app(apps.MyLoadingApp())

    #st.write('**This is completely outside of all HydraApp and HydraHeadApps, we can do whatever we want!** 🤪')

    #run with default menu layout
    #app.run()

    #if the menu is looking shit, use some sections
    app.run(complex_nav)
