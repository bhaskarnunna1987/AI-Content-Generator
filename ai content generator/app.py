import streamlit as st

st.title("AI Content Generator")

topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Casual", "Motivational"]
)

content_type = st.selectbox(
    "Select Content Type",
    ["Blog Post", "Social Media Caption"]
)

def generate_content(topic, tone, content_type):

    if content_type == "Blog Post":
        content = f"""
# {topic}

{topic} is an important subject in today's world.

This blog discusses the key concepts, benefits, and practical applications of {topic}.

By understanding {topic}, individuals can improve their knowledge and stay updated with modern trends.

In conclusion, {topic} continues to play a significant role in personal and professional growth.
"""
    else:
        content = f"""
🚀 {topic} is changing the game!

Stay informed, stay inspired, and keep learning.

#{topic.replace(' ','')} #AI #Technology
"""

    return content

if st.button("Generate Content"):

    if topic.strip() == "":
        st.error("Please enter a topic.")

    else:
        output = generate_content(topic, tone, content_type)

        st.subheader("Generated Content")
        st.write(output)

        word_count = len(output.split())
        char_count = len(output)

        st.write(f"Words: {word_count}")
        st.write(f"Characters: {char_count}")