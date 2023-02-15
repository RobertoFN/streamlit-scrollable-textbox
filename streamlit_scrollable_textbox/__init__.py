from distutils.command.build import build
import os
import streamlit.components.v1 as components
import streamlit as st

_RELEASE = True

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, 'frontend/build')

    _scrollable_textbox = components.declare_component(
        "scrollableTextbox",
        path=build_dir
    )
else:
    _scrollable_textbox = components.declare_component(
        "scrollableTextbox",
        url="http://localhost:3001"
    )


def scrollableTextbox(text:str, height:int=100, fontFamily:str='Helvetica', border:bool=True, key=None):
    return _scrollable_textbox(text=text, height=height, fontFamily=fontFamily, border=border, key=key, default=None)

if not _RELEASE:
    scrollableTextbox('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', fontFamily='Arial', key='1')

