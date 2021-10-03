 
 ## Hydralit Examples<img src="https://github.com/TangleSpace/hydralit/raw/main/docs/images/hydra.png" alt="drawing" width="50"/>
## [Hydralit package](https://github.com/TangleSpace/hydralit) is a wrapping and template project to combine multiple independant (or somewhat dependant) Streamlit applications into a multi-page application.

Currently the project implements a host application HydraApp and each child application simply needs to be a class deriving from the HydraHeadApp class and implement a single, simple method, run().

This is a sample project that tries to show some of the potential of using the Hydralit package to create multi-page Streamlit applications using the existing approach of creating a number of single applications and then using this package to make it easy to create a multi-page application from the individual applications in a simple way.

The ability to add as many applications as you wish and create a dedicated secure login application to front door all the seperate applications, means you can think about your project code and just add it to the host Hydralit application and you have a full-blooded, state aware multi-page application, with security and navigation.

If you find this project useful, please give it a star or atleast a "hey! i find this useful, thanks" callout, I hope to make everyones life alittle easier by using Hydralit.

### You can try it out by installing the project requirements and then running the sample secure app as below.

##### First install the project dependencies using the requirements.txt file, then let rip as below.
```bash
pip install -r requirements.txt
```

## Installation
Hydralit can be installed from PyPI:

```bash
pip install hydralit
```

You can run the sample secure app with the commands below. (dummy login details are, u:joe, p:joe).

```bash
hydralit_example> streamlit run secure_app.py
```

<h1><a href="https://hydralit-secure-sample.herokuapp.com/">You can see this example running here</a></h1>
<img src="https://github.com/TangleSpace/hydralit-example/raw/main/docs/images/hydralit-secure-example.gif" alt="example" width="80%"/>

The host application code is shown below as an example of how such a multi-page application with authentication and lots of bells and whistles can be created with very little code, yet alot of configuration potential.


#### secure_app.py
```python
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
        use_banner_images=["./resources/hydra.png",None,{'header':"<h1 style='text-align:center;padding: 0px 0px;color:grey;font-size:200%;'>Secure Hydralit Explorer</h1><br>"},None,"./resources/lock.png"], 
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        navbar_sticky=False,
        navbar_animation=True,
        navbar_theme=over_theme,
        
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
    app.add_app("Loader Playground", icon="⏲️", app=apps.LoaderTestApp(title="Loader Playground"))
    app.add_app("Cookie Cutter", icon="🍪", app=apps.CookieCutterApp(title="Cookie Cutter"))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    app.add_loader_app(apps.MyLoadingApp(delay=0))

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

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'Loader Playground': ['Loader Playground'],
            'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            'Hotstepper 🔥': ["Sequency Denoising","Sequency (Secure)"],
            'Clustering': ["Uber Pickups"],
            'NLP': ["Spacy NLP"],
            'Cookie Cutter': ['Cookie Cutter']
        }
    elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Loader Playground': ['Loader Playground'],
            'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            'Hotstepper 🔥': ["Sequency Denoising"],
            'Clustering': ["Uber Pickups"],
            'NLP': ["Spacy NLP"],
            'Cookie Cutter': ['Cookie Cutter']
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
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------

```
