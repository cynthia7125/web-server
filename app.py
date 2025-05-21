import streamlit as st
import re
from PIL import Image
from DB import create_users_table, insert_user, check_user_credentials


st.set_page_config(page_title="Meme Clock", page_icon=":joy_cat:", layout="wide")
create_users_table()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

def validate_name(uname, field_name="Name"):
    if not uname:
        return False, f"{field_name} is required"
    if len(uname) < 2:
        return False, f"{field_name} should be at least 2 characters long"
    return True, ""

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return False, "Email is required"
    if not re.match(pattern, email):
        return False, "Please enter a valid email address"
    return True, ""

def validate_password(pas):
    if not pas:
        return False, "Password is required"
    if len(pas) < 6:
        return False, "Password should be at least 6 characters long"
    return True, ""

if not st.session_state.logged_in:
    st.title("Welcome to Meme Clock :joy_cat:")
    st.subheader("Please Sign Up or Log In")

    login_tab, signup_tab = st.tabs(["Login", "Signup"])

    with signup_tab:
        with st.form("signup_form"):
            uname = st.text_input('Username', key="signup_username")
            email_s = st.text_input('Email', key="signup_email")
            pas_s = st.text_input('Password', type='password', key="signup_pass")
            submit_s = st.form_submit_button("Sign Up")

        if submit_s:
            valid_name, msg_name = validate_name(uname)
            valid_email, msg_email = validate_email(email_s)
            valid_pass, msg_pass = validate_password(pas_s)

            if not valid_name:
                st.error(msg_name)
            elif not valid_email:
                st.error(msg_email)
            elif not valid_pass:
                st.error(msg_pass)
            else:
                if insert_user(email_s, uname, pas_s):
                    st.session_state.logged_in = True
                    st.session_state.user = uname
                    st.success(f"Welcome, {uname}!")
                    st.rerun()
                else:
                    st.error("Email already registered. Please log in instead.")

    with login_tab:
        with st.form("login_form"):
            email_l = st.text_input('Email', key="login_email")
            uname_l = st.text_input('Username', key="login_username")
            pas_l = st.text_input('Password', type='password', key="login_pass")
            submit_l = st.form_submit_button("Log In")

        if submit_l:
            valid_email, msg_email = validate_email(email_l)
            valid_pass, msg_pass = validate_password(pas_l)

            if not valid_email:
                st.error(msg_email)
            elif not valid_pass:
                st.error(msg_pass)
            else:
                user = check_user_credentials(email_l, pas_l)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.success(f"Welcome back, {user}!")
                    st.rerun()
                else:
                    st.error("Invalid email or password.")

if st.session_state.logged_in:
    header_col1, header_col2 = st.columns([6, 1]) 

    with header_col1:
        st.markdown(f"### 👋 Welcome, {st.session_state.user}")

    with header_col2:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = ""
            st.success("You have been logged out.")
            st.rerun()


    lottie_happy = "https://media1.tenor.com/m/nbL93v_tG40AAAAC/dfv-gme.gif"
    img_LinkedIn = Image.open("images/LinkedIn profile.png")
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
                - If you'd like to opt out, add the following to ~/.streamlit/config.toml:

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
        form, table = st.columns((1, 2))

        with form:
            with st.form("fix_data"):
                fn = st.text_input('First Name')
                sn = st.text_input('Second Name')
                age = st.number_input('Phone age', 0)
                pt = st.selectbox('Phone type', ['Samsung', 'iPhone', 'Redmi', 'Nothing', 'htc', 'Realmi', 'Huawei', 'Microsoft'], index=None)
                ask = st.selectbox('Fix ask', ['Trade in', 'Get a new one', 'Get protector', 'Fix broken camera', 'Fix broken screen', 'Fix broken back', 'Fix battery issue', 'Fix charging port'], index=None)
                st.form_submit_button('Submit my request')

        with table:
            st.dataframe({
                "First Name": [fn],
                "Second Name": [sn],
                "Age": [age],
                "Phone Type": [pt],
                "Ask": [ask]
            })

    with st.container():
        st.write("---")
        st.header("My Projects")
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
            st.subheader("Showcase resume section for Python")
            st.write(
                """
                After doing projects, I'll:
                    \n1. Add Python to resume.
                    \n2. Complete scripting projects.
                    \n3. Learn a second framework.
                """
            )
            st.markdown("[Check out my portfolio...](https://reyhanacynthia.wixsite.com/portfolio)")

    with st.container():
        st.write("---")
