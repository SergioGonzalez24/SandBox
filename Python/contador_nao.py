import streamlit as st

st.title('Cuantas veces habla Nao')


def check(n, y, t, r, g, s):
    if n > y:
        st.write("Nao ha hablado más de lo que debería, Yuno Pierde")
    elif n > t:
        st.write("Nao ha hablado más de lo que debería, Tony Pierde")
    elif n > r:
        st.write("Nao ha hablado más de lo que debería, Regio Pierde")
    elif n > g:
        st.write("Nao ha hablado más de lo que debería, Gala Pierde")
    elif n > s:
        st.write("Nao ha hablado más de lo que debería, Sergio Pierde")


n = st.number_input("Numero de naomi que ha hablado")
y = st.number_input("Escribe cuantas veces va a hablar Nao (Yuno):")
t = st.number_input("Escribe cuantas veces va a habla Nao (Tony):")
r = st.number_input("Escribe cuantas veces va a  habla Nao (Regio):")
g = st.number_input("Escribe cuantas veces va a habla Nao (Gala):")
s = st.number_input("Escribe cuantas veces va a habla Nao (Sergio):")
n = 0

while n != y or n != t or n != r or n != g or n != s:
    check(n, y, t, r, g, s)
    if n == y or n == t or n == r or n == g or n == s:
        st.write("Nao ha hablado lo que debería, alguien gana")
        break
    else:
        continue
