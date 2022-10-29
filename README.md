<h2> Streamlit Scrollable Textbox </h2>

This repository contains a custom Streamlit component, that allows users to create scrollable textboxes of a defined height, to display long pieces of text on a Streamlit app while maintaining a desired layout.

<br>
To install the component, run the following command:

      pip install streamlit-scrollable-textbox

<br>
Importing and using the package in your Python project can be done as so:

      import streamlit-scrollable-textbox as stx

      stx.scrollableTextbox('My very long text.')

<br>
The parameters of the scrollableTextbox function are:

- text (str): The text to be displayed. Line breaks and new lines can be added by including "\n" in the string. 
- height (int): The height of the scrollable area, in pixels. Default value is 100 px.
- border (bool): Define whether the scrollable area should have a border or not.

<br><br>
<img src="https://user-images.githubusercontent.com/108201791/198837373-45be2528-01b3-484d-b91d-2c1111515593.gif" style="width:50em">
