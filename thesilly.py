import streamlit as st
import numpy as np 
import pandas as pd 
import time 


st.title("GetSpaced: Explore with Math")
st.button("Cool AI Stuff if your bored", type="primary") 
if st.button('Click me!'): 
    st.write("Go to the next screen!")
else: 
    st.write("Okay bye!")
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

print("H")
status_text.text('Done!')
st.balloons()
