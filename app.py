#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/24 上午11:26
# @Project  : streamlit_page
# @File     : app.py

import streamlit as st
from streamlit_option_menu import option_menu

from page1 import page1


def main():
    st.set_page_config(page_title="AI文章", layout="wide")
    st.sidebar.title("导航栏")
    
    add_selectbox = st.sidebar.selectbox(
        "请选择您的网站",
        ("待选择", "https://www.36kr.com/information/")
    )
    
    main_menu1 = "待选择"
    main_menu2 = "AI"
    
    with st.sidebar:
        st.sidebar.header(":blue[请选择您希望的文章类别]")
        selection = option_menu("类别", [main_menu1, main_menu2],
                                icons=["house", "cast"], menu_icon="cast", default_index=0)
    
    st.markdown("<h1 style='text-align: center; color: black;'>文章提取器</h1>", unsafe_allow_html=True)
    
    if add_selectbox == "https://www.36kr.com/information/" and selection == "AI":
        page1(add_selectbox, selection)
    else:
        pass


if __name__ == "__main__":
    main()
