import streamlit as st
st.header("type yes or no")
a=st.text_input("yes or no")
if len(a)!=0:
    if a=="yes":
        st.write("suriya "*100)
    elif a=="no":
        st.write("out")
    else:
        st.write("enter right input yes or no")
