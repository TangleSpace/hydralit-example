import datetime
import io
from hydralit import HydraHeadApp

import astropy.units as u
import pandas as pd
import streamlit as st
from astropy.coordinates import SkyCoord
from sunpy.coordinates import frames

from apps.extras.backmapping import *
import hydralit_components as hc


class SolarMach(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        
        st.title('Solar-MACH')

        st.subheader('Source for this great app is from the Streamlit gallery [Solar-MACH](https://github.com/jgieseler/Solar-MACH). An example of how easy it is to convert an existing application and use within a Hydralit multi-page application, see the secret saurce [here] (https://github.com/TangleSpace/hydralit).')
        st.markdown('<br><br>',unsafe_allow_html=True)
        st.markdown('## Multi-spacecraft longitudinal configuration plotter')

        # provide date and time
        with st.sidebar.container():
            d = st.sidebar.date_input("Select date", datetime.date.today()-datetime.timedelta(days = 2))
            t = st.sidebar.time_input('Select time', datetime.time(1, 30))
            date = datetime.datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")

        # plotting settings
        with st.sidebar.container():
            st.sidebar.subheader('Plot options:')
            plot_spirals = st.sidebar.checkbox('Parker spiral for each body', value=True)
            plot_sun_body_line = st.sidebar.checkbox('Straight line from Sun to body', value=True)
            show_earth_centered_coord = st.sidebar.checkbox('Add Earth-aligned coord. system', value=False)
            transparent = st.sidebar.checkbox('Transparent background', value=False)

            plot_reference = st.sidebar.checkbox('Plot reference (e.g. flare)', value=True)

            with st.sidebar.expander("Reference coordinates (e.g. flare)", expanded=plot_reference):
                reference_sys = st.radio('Coordinate system:', ['Carrington', 'Stonyhurst'], index=0)
                if reference_sys == 'Carrington':
                    reference_long = st.slider('Longitude:', 0, 360, 20)
                    reference_lat = st.slider('Latitude:', -90, 90, 0)
                if reference_sys == 'Stonyhurst':
                    reference_long = st.slider('Longitude:', -180, 180, 20)
                    reference_lat = st.slider('Latitude:', -90, 90, 0)
                    # convert Stonyhurst coordinates to Carrington for further use:
                    coord = SkyCoord(reference_long*u.deg, reference_lat*u.deg, frame=frames.HeliographicStonyhurst, obstime=date)
                    coord = coord.transform_to(frames.HeliographicCarrington(observer='Sun'))
                    reference_long = coord.lon.value
                    reference_lat = coord.lat.value
                import math
                reference_vsw = int(float(st.text_input('Solar wind speed for reference', 400)))
            if plot_reference is False:
                reference_long = None
                reference_lat = None

        st.sidebar.subheader('Choose bodies/spacecraft and measured solar wind speeds')
        with st.sidebar.container():
            full_body_list = \
                st.sidebar.text_area('Bodies/spacecraft (scroll down for example list)',
                                    'STEREO A, Earth, BepiColombo, PSP, Solar Orbiter, Mars',
                                    height=50)
            vsw_list = \
                st.sidebar.text_area('Solar wind speed per body/SC (mind the order!)', '400, 400, 400, 400, 400, 400',
                                    height=50)
            body_list = full_body_list.split(',')
            vsw_list = vsw_list.split(',')
            body_list = [body_list[i].strip() for i in range(len(body_list))]
            wrong_vsw = False
            try: 
                vsw_list = [int(vsw_list[i].strip()) for i in range(len(vsw_list))]
            except ValueError:
                wrong_vsw = True

            all_bodies = print_body_list()
            # ugly workaround to not show the index in the table: replace them with empty strings
            all_bodies.reset_index(inplace=True)
            all_bodies.index = [""] * len(all_bodies)
            st.sidebar.table(all_bodies['Key'])

            st.sidebar.markdown('[Complete list of available bodies](https://ssd.jpl.nasa.gov/horizons.cgi?s_target=1#top)')

        if wrong_vsw:
            st.error('ERROR: There is something wrong in the solar wind speed list! Maybe some missing or wrong comma?')
            st.stop()


        if len(body_list) == len(vsw_list):
            # initialize the bodies
            c = HeliosphericConstellation(date, body_list, vsw_list, reference_long,
                                        reference_lat)

            # make the longitudinal constellation plot
            plot_file = 'Solar-MACH_'+datetime.datetime.combine(d, t).strftime("%Y-%m-%d_%H-%M-%S")+'.png'

            c.plot(
                plot_spirals=plot_spirals,                            # plot Parker spirals for each body
                plot_sun_body_line=plot_sun_body_line,                # plot straight line between Sun and body
                show_earth_centered_coord=show_earth_centered_coord,  # display Earth-aligned coordinate system
                reference_vsw=reference_vsw,                          # define solar wind speed at reference
                transparent = transparent,
                # outfile=plot_file                                     # output file (optional)
            )

            # download plot
            filename = 'Solar-MACH_'+datetime.datetime.combine(d, t).strftime("%Y-%m-%d_%H-%M-%S")
            plot2 = io.BytesIO()
            plt.savefig(plot2, format='png', bbox_inches="tight")
            # plot3 = base64.b64encode(plot2.getvalue()).decode("utf-8").replace("\n", "")
            # st.markdown(f'<a href="data:file/png;base64,{plot3}" download="{plot_file}" target="_blank">Download figure as .png file</a>', unsafe_allow_html=True)
            download_button_str = self.download_button(plot2.getvalue(), filename+'.png', f'Download figure as .png file', pickle_it=False)
            #st.markdown(download_button_str, unsafe_allow_html=True)

            # display coordinates table
            df = c.coord_table
            df.index = df['Spacecraft/Body']
            df = df.drop(columns=['Spacecraft/Body'])
            df = df.round(0)
            df = df.rename(columns=
                {"Spacecraft/Body": "Spacecraft / body",
                "Carrington Longitude (°)": "Carrington longitude",
                "Latitude (°)": "Carrington latitude",
                "Heliocentric Distance (AU)": "Heliocent. distance",
                "Longitudinal separation to Earth's longitude": "Longitud. separation to Earth longitude",
                "Latitudinal separation to Earth's latitude": "Latitud. separation to Earth latitude", 
                "Vsw": "Solar wind speed",
                "Magnetic footpoint longitude (Carrington)": "Magnetic footpoint Carrington longitude",
                "Longitudinal separation between body and reference_long": "Longitud. separation bw. body & reference",
                "Longitudinal separation between body's mangetic footpoint and reference_long": "Longitud. separation bw. body's magnetic footpoint & reference",
                "Latitudinal separation between body and reference_lat": "Latitudinal separation bw. body & reference"})
            st.table(df.T)

            # download coordinates
            # filename = 'Solar-MACH_'+datetime.datetime.combine(d, t).strftime("%Y-%m-%d_%H-%M-%S")
            # csv = c.coord_table.to_csv().encode()
            # b64 = base64.b64encode(csv).decode()
            # st.markdown(f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv" target="_blank">Download table as .csv file</a>', unsafe_allow_html=True)
            download_button_str = self.download_button(c.coord_table, filename+'.csv', f'Download table as .csv file', pickle_it=False)
            #st.markdown(download_button_str, unsafe_allow_html=True)
        else:
            st.error(f"ERROR: Number of elements in the bodies/spacecraft list \
                    ({len(body_list)}) and solar wind speed list ({len(vsw_list)}) \
                    don't match! Please verify that for each body there is a solar \
                    wind speed provided!")

        # footer
        st.markdown("""---""")
        st.markdown('The *Solar MAgnetic Connection Haus* (Solar-MACH) tool is a \
                    multi-spacecraft longitudinal configuration plotter. It was \
                    originally developed at the University of Kiel, Germany, and further \
                    discussed within the [ESA Heliophysics Archives USer (HAUS)]\
                    (https://www.cosmos.esa.int/web/esdc/archives-user-groups/heliophysics) \
                    group. It is now opened to everyone ([original code]\
                    (https://github.com/esdc-esac-esa-int/Solar-MACH)).')

        st.markdown('[Forked and modified](https://github.com/jgieseler/Solar-MACH) by \
                    [J. Gieseler](https://jgieseler.github.io) (University of Turku, Finland). \
                    [**Get in contact**](mailto:jan.gieseler@utu.fi?subject=Solar-MACH).')

        col1, col2 = st.columns((5,1))
        col1.markdown("The development of the online tool has received funding from the \
                    European Union's Horizon 2020 research and innovation programme \
                    under grant agreement No 101004159 (SERPENTINE).")
        col2.markdown('[<img src="https://serpentine-h2020.eu/wp-content/uploads/2021/02/SERPENTINE_logo_new.png" \
                        height="80">](https://serpentine-h2020.eu)', unsafe_allow_html=True)

        st.markdown('Powered by: \
                    [<img src="https://matplotlib.org/stable/_static/logo2_compressed.svg" height="25">](https://matplotlib.org) \
                    [<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" height="30">](https://streamlit.io) \
                    [<img src="https://raw.githubusercontent.com/sunpy/sunpy-logo/master/generated/sunpy_logo_landscape.svg" height="30">](https://sunpy.org)', \
                    unsafe_allow_html=True)
