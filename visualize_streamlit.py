import streamlit as st
import matplotlib.pyplot as plt

scores = [80, 90, 75, 88]
average = sum(scores) / len(scores)

st.title("Score Visualization")
st.write(f"Average score: {average}")

fig, ax = plt.subplots()
ax.bar(range(1, len(scores)+1), scores)
ax.set_xlabel('Student')
ax.set_ylabel('Score')
ax.set_title('Scores Bar Chart')
st.pyplot(fig)
