from distutils.command.build import build
import os
import streamlit.components.v1 as components
import streamlit as st

_RELEASE = True

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, 'frontend/build')

    _scrollable_textbox = components.declare_component(
        "ScrollableTextbox",
        path=build_dir
    )
else:
    _scrollable_textbox = components.declare_component(
        "ScrollableTextbox",
        url="http://localhost:3001"
    )


def ScrollableTextbox(text:str, height:int=100, border:bool=True, key=None):
    return _scrollable_textbox(text=text, height=height, border=border, key=key, default=None)

if not _RELEASE:
    ScrollableTextbox('This is some \ntext', key='1')

