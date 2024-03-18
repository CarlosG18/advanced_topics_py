import streamlit as st
import pandas as pd

#adicionar texto
st.text('Minha pomba!!')

#widgets
# slider
x_slider = st.slider('x')
st.text(f"valor de x = {x_slider}")

st.write("você é corno?")
button = st.button("ok")
st.write(button)

st.selectbox("o que voce prefere", ["mulher", "homem"])

st.text_input("digite seu nome", key="nome")

if st.session_state.nome == "carlos":
    st.write("você é carlos!")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.button(
    'How would you like to be contacted?')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'