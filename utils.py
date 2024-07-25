#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/24 上午11:31
# @Project  : streamlit_page
# @File     : utils.py

import streamlit as st

class_label_dict = {
    "AI": "AI",
}


def show_text_total(content):
    for cont in content:
        if cont[:4] == "http":
            st.image(cont)
        else:
            st.write(cont)


def show_text_only(content):
    for cont in content:
        if cont[:4] == "http":
            continue
        else:
            st.write(cont)
