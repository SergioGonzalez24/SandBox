import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('App de prueba')

y = st.number_input("Escribe la tasa de interés nominal (%):")
A = st.number_input("Escribe la cantidad que ahorrarás ($):")
T = st.number_input("Escribe cuántos meses quieres ver: ", step=1)

tasas = []
for i in range(int(T)+1):
    tasa = st.number_input(f"Tasa de interés para el mes {i} (%):", key=f"tasa_{i}")
    tasas.append(tasa)

z = np.arange(T+1)
r_d = A * (1 + np.array(tasas)/(12*100))**z
r_c = A * np.exp(np.array(tasas)*z/(12*100))

new_dict = {"Mes": z,
            "Retorno Discreto": r_d,
            "Retorno Continuo": r_c}
df = pd.DataFrame(new_dict)
df.columns = new_dict.keys()

st.dataframe(df)

st.write(f"En {T} meses tendrás $ {r_c[-1]}")

# Gráfico
plt.plot(z, r_c)
plt.title('Crecimiento de la inversión a lo largo de los meses')
plt.xlabel('Mes')
plt.ylabel('Valor de la inversión ($)')
st.pyplot()