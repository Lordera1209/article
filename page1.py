#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/24 上午11:27
# @Project  : streamlit_page
# @File     : page1.py

import streamlit as st
from streamlit_option_menu import option_menu
from article1 import sp0, sp1
from utils import class_label_dict
from utils import show_text_total, show_text_only


def page1(add_selectbox, selection):
    st.sidebar.title(f"{selection}导航栏")
    
    topN = st.sidebar.selectbox(
        "请选择Top N总数",
        ("1", "2", "3")
    )
    N = st.sidebar.selectbox(
        "请定位Top K篇文章",
        ("1", "2", "3")
    )
    module = st.sidebar.selectbox(
        "请选择是否显示图片",
        ("待选择", "有图模式", "无图模式")
    )
    
    main_menu1 = "待选择"
    main_menu2 = "全文"
    main_menu3 = "标题"
    main_menu4 = "副标题"
    main_menu5 = "正文"
    
    with st.sidebar:
        st.sidebar.header(":blue[请选择您希望的文章段落]")
        form = option_menu("文章形式", [main_menu1, main_menu2, main_menu3, main_menu4, main_menu5],
                           icons=["house", "cast"], menu_icon="cast", default_index=0)
    
    st.title(f"{selection}文章获取")
    st.divider()
    
    if "待选择" in [module, form]:
        st.subheader("请在侧边栏完成选择项")
    
    origin_url = add_selectbox + class_label_dict[selection]
    title_list, sub_title_list, suffix_list = sp0(origin_url, k=topN)
    
    if module == "有图模式":
        if form == "全文":
            st.header(title_list[int(N) - 1])
            st.subheader(sub_title_list[int(N) - 1])
            content_list = sp1(suffix_list[int(N) - 1])
            show_text_total(content_list)
        elif form == "标题":
            st.header(title_list[int(N) - 1])
        elif form == "副标题":
            st.subheader(sub_title_list[int(N) - 1])
        elif form == "正文":
            content_list = sp1(suffix_list[int(N) - 1])
            show_text_total(content_list)
        else:
            pass
    
    if module == "无图模式":
        if form == "全文":
            st.header(title_list[int(N) - 1])
            st.subheader(sub_title_list[int(N) - 1])
            content_list = sp1(suffix_list[int(N) - 1])
            show_text_only(content_list)
        elif form == "标题":
            st.header(title_list[int(N) - 1])
        elif form == "副标题":
            st.subheader(sub_title_list[int(N) - 1])
        elif form == "正文":
            content_list = sp1(suffix_list[int(N) - 1])
            show_text_only(content_list)
        else:
            pass
