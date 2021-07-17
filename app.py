import streamlit as st
from hydralit import HydraApp
import apps

if __name__ == '__main__':

    #------------all valid container references, do not initilise or page config will not be applied.
    # my_container = st.sidebar
    # my_container = st.sidebar.beta_container
    # my_container = st.sidebar.beta_columns
    #my_container = st
    # my_container = st.beta_container
    # my_container = st.beta_columns
    my_container = None

    app = HydraApp(title='Hydralit Data Explorer',favicon="🐙",nav_container=my_container,nav_horizontal=True)

    # Add all your application classes here
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home')) #if we don't specify one (is_home=True), the first app will be the home page
    app.add_app("Cheat Sheet", icon="📚", app=apps.CheatApp(),is_home=True)
    app.add_app("Sequency Denoising",icon="🔊", app=apps.WalshApp(title='Walsh Data'))
    app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title='Solar-MACH'))
    app.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP2", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP3", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP4", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP5", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP6", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP7", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP8", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Spacy NLP9", icon="⌨️", app=apps.SpacyNLP())
    app.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC())


    # If the menu is cluttered, just rearrange it into sections!
    complex_nav = {
        'Home': ['Home'],
        'Intro': ['Cheat Sheet',"Solar Mach"],
        'Sequency Stuff': ["Sequency Denoising"],
        'Spacy NLP - 1': ["Spacy NLP","Spacy NLP2"],
        'Spacy NLP - 2': ["Spacy NLP5"],
        'Spacy NLP - 3': ["Spacy NLP3","Spacy NLP4"],
        'Spacy NLP - 4': ["Spacy NLP6","Spacy NLP7","Spacy NLP8","Spacy NLP9"],
        'Uber NYC': ["Uber Pickups"]
    }

    #add a custom loader for app transitions
    #app.add_loader_app(apps.MyLoadingApp())

    #st.write('**This is completely outside of all HydraApp and HydraHeadApps, we can do whatever we want!** 🤪')

    # The main app entry point
    #app.run()

    #if the menu is looking shit, use some sections
    app.run(complex_nav)
