import requests
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Meme Clock", page_icon=":joy_cat:", layout="wide")

lottie_happy = "https://media1.tenor.com/m/nbL93v_tG40AAAAC/dfv-gme.gif"
img_LinkedIn =  Image.open("images/LinkedIn profile.png")
img_website_skills = Image.open("images/skills snippet.png")

with st.container():
    st.subheader("Any meme Ideas in that head of yours :question:")
    st.title("You think :exclamation: we make :exclamation:")
    st.write("Memes are life, we can not live without being happy. Make someone smile today.")
    st.write("[Learn More >](https://en.wikipedia.org/wiki/Internet_meme)")

with st.container():
    st.write("---")
    st.header("Memeology")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
             You can find our privacy policy at https://streamlit.io/privacy-policy

            Summary:
            - This open source library collects usage statistics.
            - We cannot see and do not store information contained inside Streamlit apps,
                such as text, charts, images, etc.
            - Telemetry data is stored in servers in the United States.
            - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
                creating that file if necessary:

                [browser]
                gatherUsageStats = false
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com)")
    with right_column:
        st.image(lottie_happy, width=700)

with st.container():
    st.write("---")
    st.header("Form Entries")
    st.write("#####")
    form, table = st.columns((1, 2))

    with form:
        with st.form("fix_data"):
            fn = st.text_input('First Name', placeholder='What\'s your first name?')
            sn = st.text_input('Second Name', placeholder='What\'s your second name?')
            age = st.number_input('Phone age', 0)
            pt = st.selectbox('Phone type', ['Samsung', 'iPhone', 'Redmi', 'Nothing', 'htc', 'Realmi', 'Huawei', 'Microsoft'], placeholder='Select one', index=None)
            ask = st.selectbox('Fix ask', ['Trade in', 'Get a new one', 'Get protector', 'Fix broken camera', 'Fix broken screen', 'Fix broken back', 'Fix battery issue', 'Fix charging port'], placeholder='Select one', index=None)
            st.form_submit_button('Submit my request')

    with table:
        # st.cache_data
        df = st.dataframe(
            {
                "First Name": [fn],
                "second Name": [sn],
                "age": [age],
                "Phone type": [pt],
                "Ask": [ask]
            }
        )
    # st.session_state(table)
    
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_LinkedIn)
    with text_column:
        st.subheader("Do a website in python using streamlit")
        st.write(
            """
            Learning how to do a website using:
                \n1. Python
                \n2. Lottie files
                \n3. Streamlit
            \nTo be pushed to github and on to the next python adventure.
            """
        )
        st.markdown("[Check out the page...](https://www.linkedin.com/in/reyhana-cherop-77a584156/)")
    
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_website_skills)
    with text_column:
        st.subheader("Showcase the section of my resume where I will add python as a skill")
        st.write(
            """
            After I have pushed some work and learnt the ins and outs of python, I will add the programming language python as a skill.
            I will add it to the section in the image on my portfolio.
            \nMy goal is to:
                \n1. Do a couple more projects in python.
                \n2. Do a scripting project in python.
                \n3. Learn another framework.
            """
        )
        st.markdown("[Check out my portfolio...](https://reyhanacynthia.wixsite.com/portfolio)")

with st.container():
    st.write("---")