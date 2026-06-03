import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Oil Price Impact Calculator", layout="centered")

st.title("USA Oil Price Impact Calculator")
st.caption("Current changes compared to January 2020 baselines")

col1, col2 = st.columns(2)

with col1:
    transportation = st.number_input("Transportation Price Index", min_value=0.0, value=208.284, step=0.001, format="%.2f")
    health = st.number_input("Health Care Price Index", min_value=0.0, value=511.458, step=0.001, format="%.2f")

with col2:
    food = st.number_input("Food Price Index", min_value=0.0, value=261.272, step=0.001, format="%.2f")
    pollution = st.number_input("Air Quality Index", min_value=0.0, value=37.5, step=0.001, format="%.2f")

if st.button("Calculate changes", type="primary"):

    # --- your original formulas ---
    Ptransportation = round(((transportation - 208.284) / 208.284) * 100, 2)
    Pfood           = round(((food - 261.272)           / 261.272) * 100, 2)
    Ppollution      = round(((pollution - 37.5)         / 37.5)    * 100, 2)
    Phealth         = round(((health - 511.458)         / 511.458) * 100, 2)

    # --- stat cards ---
    st.divider()
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Transportation", f"{'+' if Ptransportation > 0 else ''}{Ptransportation}%")
    m2.metric("Food",           f"{'+' if Pfood > 0 else ''}{Pfood}%")
    m3.metric("Health Care",    f"{'+' if Phealth > 0 else ''}{Phealth}%")
    m4.metric("Air Pollution",    f"{'+' if Ppollution > 0 else ''}{Ppollution}%")

    # --- your original chart code ---
    categories = ['Transportation \nPrice Index', 'Food \nPrice Index', 'Air Quality \nIndex', 'Health Care \nPrice Index']
    values     = [Ptransportation, Pfood, Ppollution, Phealth]
    custom_colors = ['firebrick', 'gold', 'forestgreen', 'lightskyblue']

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=custom_colors)
    ax.set_title('Current Changes Due to Rising Oil Prices Compared to January 2020 Baselines')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Percentage Change')

    st.pyplot(fig)

    Tchange = abs(Ptransportation) + abs(Phealth) + abs(Pfood) + abs(Ppollution)

    if Tchange > 0:
        Pietransportation = (abs(Ptransportation) / Tchange) * 100
        Piehealth         = (abs(Phealth)         / Tchange) * 100
        Piefood           = (abs(Pfood)            / Tchange) * 100
        Piepollution      = (abs(Ppollution)       / Tchange) * 100
    
        sizes  = [Pietransportation, Piefood, Piepollution,Piehealth]
        labels = ['Transportation', 'Food', 'Air Quality', 'Health']
    
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%',color=custom_colors)
        ax2.set_title('Share of Total Change by Sector')
        st.pyplot(fig2)
