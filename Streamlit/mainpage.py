from asyncio import run
import streamlit as st
from streamlit_option_menu import option_menu
import os

import Homepage, AboutUs, Gallery
st.set_page_config(
    page_title="Vike",
)



class Multiapp:

    def __init__(self):
        self.apps = []

    def add_App(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def run():
        # app = st.sidebar()
        with st.sidebar:
            app = option_menu(
                menu_title='Navigation',
                options=['Homepage','AboutUs','Gallery'],
                icons=['house-fill','person-circle','card-image'],
                menu_icon='arrow-90deg-down',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#ffff00"},
        "nav-link-selected": {"background-color": "blue"},}
            )

        if app == "Homepage" :
            Homepage.app()
        if app== "AboutUs":
            AboutUs.app()
        if app== "Gallery" :
            Gallery.app()
        

    run()