import streamlit as st
import random

def lanzar_moneda():
    return random.choice(['Cara', 'Cruz'])

def main():
    st.title('Simulador de Lanzamiento de Moneda')

    cantidad_lanzamientos = st.number_input('Cantidad de lanzamientos', min_value=1, value=1, step=1)

    if st.button('Lanzar'):
        resultados = [lanzar_moneda() for _ in range(cantidad_lanzamientos)]
        st.write('Resultados:')
        for idx, resultado in enumerate(resultados):
            st.write(f'Lanzamiento {idx + 1}: {resultado}')

if __name__ == '__main__':
    main()
