from hydralit import HydraApp
import streamlit as st
import apps


if __name__ == '__main__':
    over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        title='Secure Hydralit Data Explorer',
        favicon="🐙",
        hide_streamlit_markers=True,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_banner_images=["./resources/hydra.png",None,{'header':"<h1 style='text-align:center;padding: 0px 0px;color:white;font-size:200%;'>Secure Hydralit Explorer</h1><br>"},None,"./resources/lock.png"], 
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )

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

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    app.add_loader_app(apps.MyLoadingApp(delay=1))
    #app.add_loader_app(apps.QuickLoaderApp())

    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    #-----if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    #check if this is first open
    # user_access_level, username = app.check_access()
    # if user_access_level == 0 and username is None:
    #     app.set_access(1, 'guest')
    #--------------------------------------------------------------------------------------------------------------------

    #if the menu is looking shit, use some sections
    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            'Hotstepper 🔥': ["Sequency Denoising","Sequency (Secure)"],
            'Clustering': ["Uber Pickups"],
            'NLP': ["Spacy NLP"],
        }
    elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            'Hotstepper 🔥': ["Sequency Denoising"],
            'Clustering': ["Uber Pickups"],
            'NLP': ["Spacy NLP"],
        }
    else:
        complex_nav = {
            'Home': ['Home'],
        }

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)

    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()

    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    #---------------------------------------------------------------------

