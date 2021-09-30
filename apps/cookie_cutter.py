import streamlit as st
from hydralit import HydraHeadApp
from hydralit_components import CookieManager


class CookieCutterApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            #cookie_manager = stx.CookieManager(key='1234')
            cookie_manager = CookieManager(key='REDKI')

            st.subheader("All Cookies:")
            cookies = cookie_manager.get_all()
            st.write(cookies)

            c1, c2, c3 = st.columns(3)
            with c1:
                st.subheader("Get Cookie:")
                cookie = st.text_input("Cookie", key="0")
                clicked = st.button("Get")
                if clicked:
                    value = cookie_manager.get(cookie)
                    st.write(value)
            with c2:
                st.subheader("Set Cookie:")
                cookie = st.text_input("Cookie", key="1")
                val = st.text_input("Value")
                if st.button("Add"):
                    cookie_manager.set(cookie, val)
            with c3:
                st.subheader("Delete Cookie:")
                cookie = st.text_input("Cookie", key="2")
                if st.button("Delete"):
                    cookie_manager.delete(cookie)

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))