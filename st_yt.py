import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Monte-Carlo",page_icon="⚙️")

o,n=st.select_slider("Nombre d'éssais ",options=[10**k for k in range(1,7)],value=(10,10**6))

data=np.random.binomial(1,0.12,size=n)
st.write("fréquence observée avec "+str(n)+" éssais : ")
st.title(data.mean())

Launch=st.button("Simuler la comparaison")
if Launch:
    fig=plt.figure()
    k=o
    ke=round(np.log10(k))
    while k<=n:
        dat=np.random.binomial(1,0.12,size=(k,100)).mean(axis=0)
        plt.plot([ke]*100,dat,"ko",markersize=2)
        k*=10
        ke+=1
    plt.plot([0,ke+1],[0.12,0.12],"r--")
    st.pyplot(fig)