import pandas as pd
import streamlit as st
from hydralit import HydraHeadApp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from hotstepper import Steps,Step
import hotstepper as hs
from itertools import chain
from hotstepper import Sequency


SIG_FIGURE_FMT = '{:,.2f}'

class WalshApp(HydraHeadApp):


    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    def run(self):

        try:
            st.title('Sequency Denoising')
            st.subheader('Source for this quick tutorial on using Sequency methods for denoising step change data can be found in the [Hotstepper documentation](https://hotstepper.readthedocs.io/notebooks/sequency_quickstart.html). An example of how easy it is to convert an existing application and use within a Hydralit multi-page application, see the secret saurce [here] (https://github.com/TangleSpace/hydralit).')
            st.markdown('<br><br>',unsafe_allow_html=True)

            df_vq_samp = pd.read_csv(r'https://raw.githubusercontent.com/TangleSpace/hotstepper-data/master/data/vessel_queue.csv',parse_dates=['enter','leave'],dayfirst=True)
            self.download_button(df_vq_samp,'data.csv','Download Example Data')

            st.write(
                """
                Another typical use case of Fourier transforms is to remove high frequency noise from a single by decomposing it into constituent frequency components and setting frequencies below a threshold value to zero. \
                With Sequency analysis, we have a similar functionality, except since we have step data and we are wanting to retain the nature of the step data (as steps) instead of just smoothing away the details, \
                we can use the denoise method of the Sequency module to remove the higher sequency number components. An explicit example is shown below, here for now, we pass in the direct steps data for denoising, \
                apply a strength parameter to determine how many of the high sequency components are set to zero and then we construct a new Steps object.
                """
            )

            st.code(
                """
denoise_step_changes_strong = seq.denoise(rand_steps.step_changes(),denoise_strength=0.7,denoise_mode='range')
denoise_step_changes = seq.denoise(rand_steps.step_changes(),denoise_strength=0.2)

rand_steps_denoise_strong = Steps().add_direct(data_start=rand_steps.step_keys(),data_weight = denoise_step_changes_strong)
rand_steps_denoise = Steps().add_direct(data_start=rand_steps.step_keys(),data_weight = denoise_step_changes)

ax = rand_steps.plot(label='Original Data')
rand_steps_denoise.plot(ax=ax,color='g',linewidth=2,label='Light Denoise');
rand_steps_denoise_strong.plot(ax=ax,color='r',linewidth=2,linestyle='-',label='Strong Denoise')
ax.legend();
                """
            )

            denoise_power_strong_select = st.sidebar.slider('Strong Denoise Strength',value=0.7,min_value=0.01,max_value=1.0,step=0.01)
            denoise_power_light_select = st.sidebar.slider('Light Denoise Strength',value=0.2,min_value=0.01,max_value=1.0,step=0.01)
            denoise_mode_select = st.sidebar.radio('Denoise Mode',('range','value'))

        
            seq = Sequency()
            #Create a sequence of steps that we can analyse
            steps_changes = np.random.randint(-10,12,100)
            rand_steps = Steps().add_direct(data_start=list(range(1,len(steps_changes))),data_weight = steps_changes)

            denoise_step_changes_strong = seq.denoise(rand_steps.step_changes(),denoise_strength=denoise_power_strong_select,denoise_mode=denoise_mode_select)
            denoise_step_changes = seq.denoise(rand_steps.step_changes(),denoise_strength=denoise_power_light_select,denoise_mode=denoise_mode_select)

            rand_steps_denoise_strong = Steps().add_direct(data_start=rand_steps.step_keys(),data_weight = denoise_step_changes_strong)
            rand_steps_denoise = Steps().add_direct(data_start=rand_steps.step_keys(),data_weight = denoise_step_changes)

            ax = rand_steps.plot(label='Original Data')
            rand_steps_denoise.plot(ax=ax,color='g',linewidth=2,label='Light Denoise')
            rand_steps_denoise_strong.plot(ax=ax,color='r',linewidth=2,linestyle='-',label='Strong Denoise')
            ax.legend()

            st.pyplot(ax.get_figure(),clear_figure=True)


            st.write(
                """
                As another quick example, we can apply the same technique to one of the HotStepper sample datasets, for this tutorial, we’ll only look at the first two months of data in order to better highlight what the sequency denoising can do to help better show the trend or typical step behaviour of the data.
                """
            )

            st.code(
                """
df_vq_samp = pd.read_csv(r'https://raw.githubusercontent.com/TangleSpace/hotstepper-data/master/data/vessel_queue.csv',parse_dates=['enter','leave'],dayfirst=True)

vq_samp = Steps.read_dataframe(df_vq_samp,start='enter',end='leave')
vq_clip = vq_samp.clip(ubound=pd.Timestamp(2020,3,1))

dn = seq.denoise(vq_clip.step_changes(),denoise_mode='range')
vq_clip_dn = Steps().add_direct(data_start=vq_clip.step_keys(convert_keys=True),data_weight=dn)

ax = vq_clip.plot(label='Original Data',figsize=(14,6))
vq_clip_dn.plot(ax=ax,linewidth=3,label='Sequency Denoise')
ax.legend()
                """
            )

            vq_samp = Steps.read_dataframe(df_vq_samp,start='enter',end='leave')
            vq_clip = vq_samp.clip(ubound=pd.Timestamp(2020,3,1))
            

            dn_strong = seq.denoise(vq_clip.step_changes(),denoise_strength=denoise_power_strong_select,denoise_mode=denoise_mode_select)
            dn_light = seq.denoise(vq_clip.step_changes(),denoise_strength=denoise_power_light_select,denoise_mode=denoise_mode_select)

            vq_clip_dn_strong = Steps().add_direct(data_start=vq_clip.step_keys(convert_keys=True),data_weight=dn_strong)
            vq_clip_dn_light = Steps().add_direct(data_start=vq_clip.step_keys(convert_keys=True),data_weight=dn_light)

            ax = vq_clip.plot(label='Original Data',figsize=(14,6))
            vq_clip_dn_strong.plot(ax=ax,linewidth=1.5,label='Strong Sequency Denoise')
            vq_clip_dn_light.plot(ax=ax,linewidth=1.5,label='Light Sequency Denoise')
            ax.legend()

            st.pyplot(ax.get_figure(),clear_figure=True)

            st.write(
                """
                As the last item, we can take a look at the sequency spectrum for the vessel queue data. This dataset has a large number of changes and therefore the sequency range goes quite high, however it does show a number of peaks that are significantly larger than the others, indicating a number of distinct and repeating step change patterns within the data over this period.
                """
            )

            st.code(
                """
fig, (ax,ax2,ax3) = plt.subplots(nrows=3,figsize=(12,8))
fig.tight_layout(h_pad=4)

# Sequency object to use for analysis
vq_clip_seq = Sequency()
n,sp,l = vq_clip_seq.sequency_spectrum(vq_clip.step_changes())


ax.set_title('Step Change Sequency Spectrum')
ax.set_xlabel('Sequency Number')
ax.set_ylabel('Amplitude')
ax.stem(n,sp)

# number of data points, needed to create the sampling frequency
no_points = vq_clip.step_changes().shape[0]

fr,fsp = vq_clip_seq.frequency_spectrum(vq_clip.step_changes(),2*np.pi*no_points)

ax2.set_title('Step Change Frequency Spectrum')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Amplitude')
ax2.stem(fr,fsp)

# FFT the steps values instead of the delta changes to see the difference in the spectrum.
frv,fspv = vq_clip_seq.frequency_spectrum(vq_clip.step_values(),2*np.pi*no_points)

ax3.set_title('Steps Value Frequency Spectrum')
ax3.set_xlabel('Frequency')
ax3.set_ylabel('Amplitude')
ax3.stem(frv[1:],fspv[1:]);
                """
            )


            fig, (ax,ax2,ax3) = plt.subplots(nrows=3,figsize=(12,8))
            fig.tight_layout(h_pad=4)

            # Sequency object to use for analysis
            vq_clip_seq = Sequency()
            n,sp,l = vq_clip_seq.sequency_spectrum(vq_clip.step_changes())


            ax.set_title('Step Change Sequency Spectrum')
            ax.set_xlabel('Sequency Number')
            ax.set_ylabel('Amplitude')
            ax.stem(n,sp)

            # number of data points, needed to create the sampling frequency
            no_points = vq_clip.step_changes().shape[0]

            fr,fsp = vq_clip_seq.frequency_spectrum(vq_clip.step_changes(),2*np.pi*no_points)

            ax2.set_title('Step Change Frequency Spectrum')
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Amplitude')
            ax2.stem(fr,fsp)

            # FFT the steps values instead of the delta changes to see the difference in the spectrum.
            frv,fspv = vq_clip_seq.frequency_spectrum(vq_clip.step_values(),2*np.pi*no_points)

            ax3.set_title('Steps Value Frequency Spectrum')
            ax3.set_xlabel('Frequency')
            ax3.set_ylabel('Amplitude')
            ax3.stem(frv[1:],fspv[1:])

            st.pyplot(fig,clear_figure=True)


        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

