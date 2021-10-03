import spacy_streamlit
from pathlib import Path
import streamlit as st
import srsly
import os
import importlib

from hydralit import HydraHeadApp

class SpacyNLP(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):

        #st.experimental_set_query_params(selected=self.title)

        MODELS = srsly.read_json(os.path.join(Path(__file__).parent,"extras","models.json"))
        DEFAULT_MODEL = "en_core_web_sm"
        DEFAULT_TEXT = "David Bowie moved to the US in 1974, initially staying in New York City before settling in Los Angeles."
        DESCRIPTION = """**Explore trained [spaCy v3.0](https://nightly.spacy.io) pipelines**"""

        def get_default_text(nlp):
            # Check if spaCy has built-in example texts for the language
            try:
                examples = importlib.import_module(f".lang.{nlp.lang}.examples", "spacy")
                return examples.sentences[0]
            except (ModuleNotFoundError, ImportError):
                return ""

        st.subheader('Source for this great app is from the Streamlit gallery [NLP with spaCy](https://github.com/ines/spacy-streamlit-demo). An example of how easy it is to convert an existing application and use within a Hydralit multi-page application, see the secret saurce [here] (https://github.com/TangleSpace/hydralit).')
        st.markdown('<br><br>',unsafe_allow_html=True)

        st.info(r"Yes, this application will show an error if you don't have the 'en_core_web_sm' Spacy model installed, this was left to show that if an app crashes, it won't affect the HydraApp or the other HydraHeadApps, this app will crash and burn on it's own. If you want to fix the error, just install the missing model with [**python -m spacy download en_core_web_sm**](https://spacy.io/usage)")
        spacy_streamlit.visualize(
            MODELS,
            default_model=DEFAULT_MODEL,
            visualizers=["parser", "ner", "similarity", "tokens"],
            show_visualizer_select=True,
            sidebar_description=DESCRIPTION,
            get_default_text=get_default_text
        )