import streamlit as st
st.header("baby")
a=st.text_input("type yes")
if len(a)!=0:
    if a=="yes":
        st.write("love you abi"*1000)
    else:
        st.write("enter right input yes or no")
        
