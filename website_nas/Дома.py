import streamlit as st
from streamlit_lottie import st_lottie
import json
st.set_page_config(layout="wide")
from PIL import Image
import os

def load_lottie_file(filename):
    # Get the absolute path to the root of the project
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)  # Construct the path

    # Debug output (optional)
    print("Looking for JSON file at:", filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

animation = load_lottie_file("teach.json")

title = """ <div style='text-align:center'><h2>STEMfinity</h2></div>"""


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(title,unsafe_allow_html=True)
        st.write("")
        st.write("Добредојдовте на нашата веб-страница! Тука ќе најдете професионална и персонализирана поддршка за да ги совладате и најсложените теми од предметите математика, програмирање и физика. Без разлика дали сте почетник или сакате да го продлабочите вашето знаење, ние сме тука да ви помогнеме со индивидуален пристап, флексибилно време и јасно објаснување на материјалот. Започнете го вашето патување кон успехот со нас денес!")
        st.write("")
        st.page_link("pages/Инструкторите.py", label = "За нас")
    with right_column:
        st.lottie(animation, height=500)


st.write("")
st.write("")
st.write("")


with st.expander("Летен Курс 2025 15.08 - 23.08"):
    st.write("ПРИДРУЖЕТЕ СЕ НА ПОДГОТОВКИ ЗА НАТПРЕВАР")
    st.write("Подготвени за авантура во светот на знаењето? Придружете ни се на нашиот онлајн камп каде што математиката и физиката стануваат вистинска игра на умот! Овој камп е наменет за сите млади јунаци кои сакаат да се подготват за натпревари, да ги острат своите вештини и да се забавуваат додека учат. Со интересни предизвици, забавни задачи и ментори кои знаат како да ја разбудат љубопитноста, ова е местото каде што знаењето расте, а талентот блеска. Вклучи се и подготви се да победуваш.")
    st.write("Како да се пријавите: Пополнете ја google формата достапна подолу.")
    st.write("Цена: 3000 денари")
    st.link_button("Пријави се", "https://docs.google.com/forms/d/1404IGV6f01mU3KwJpWNsQvExNm1m1ji0R72T5lZqtd4/viewform?pli=1&edit_requested=true&fbclid=PAQ0xDSwLmKdBleHRuA2FlbQIxMAABp9aZnOnms0UMwGFMDwMSq4nddDFDidQuiMNqL_k-9cyaTeKsqD_g0qq2hp93_aem_maJV7NbIu0W57LkmPxs9tw")



st.write("")
st.write("")
st.write("")


st.write("Приватни часови")
with st.expander("Матматика од 1 до 9 одделение"):
    st.write("Цена: 500 денари")
    st.write("Како да се пријавите: Едноставно напишете ни порака преку формата за контакт подолу. Потребно ни е Вашето име и презиме, за кој час сте заинтересирани Вие или вашето дете, како и кое одделение сте Вие или вашето дете.")

with st.expander("Програмирање почетнички часови во Python"):
    st.write("Цена: 500 денари")
    st.write("Како да се пријавите: Едноставно напишете ни порака преку формата за контакт подолу. Потребно ни е Вашето име и презиме, за кој час сте заинтересирани Вие или вашето дете, како и кое одделение или година сте Вие или вашето дете.")

with st.expander("Програмирање почетнички часови во C++"):
    st.write("Цена: 500 денари")
    st.write("Како да се пријавите: Едноставно напишете ни порака преку формата за контакт подолу. Потребно ни е Вашето име и презиме, за кој час сте заинтересирани Вие или вашето дете, како и кое одделение или година сте Вие или вашето дете.")

with st.expander("Физика за 7 и 8 одделение"):
    st.write("Цена: 500 денари")
    st.write("Како да се пријавите: Едноставно напишете ни порака преку формата за контакт подолу. Потребно ни е Вашето име и презиме, за кој час сте заинтересирани Вие или вашето дете, како и кое одделение сте Вие или вашето дете.")






st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

form = """
    <style>
    body {
        background-color: #0b1d3a;
        color: white;
    }

    .contact-form {
        max-width: 600px;
        margin: 0 auto;
        padding: 30px;
        background-color: #FFD2D2;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        font-family: Arial, sans-serif;
        color: white;
        box-sizing: border-box;
    }

    .contact-heading {
        text-align: center;
        color: white;
        font-size: 28px;
        margin-bottom: 20px;
        font-weight: bold;
        font-family: Arial, sans-serif;
    }

    .contact-form input[type="text"],
    .contact-form input[type="email"],
    .contact-form textarea {
        width: 100%;
        padding: 12px;
        margin-top: 8px;
        margin-bottom: 16px;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box;
        font-size: 16px;
        background-color: #FD7F7F;
        color: white;
    }

    .contact-form input::placeholder,
    .contact-form textarea::placeholder {
        color: #c4c4c4;
    }

    .contact-form textarea {
        height: 150px;
        resize: vertical;
    }

    .contact-form button {
        background-color: #4c9fd6;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }

    .contact-form button:hover {
        background-color: #3b86b8;
    }
    </style>

    <p class="contact-heading">Контактирајте не</p>

    <form class="contact-form" action="https://formsubmit.co/stem.finity.org@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
"""

with st.container():
    left, right = st.columns(2)
    with left:
        st.markdown(form, unsafe_allow_html=True)
    with right:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("Оваа веб страна е направена од страна на инстукторите во STEMfinity (повеќе информации на нашата 'За нас страница'), со помош на програмскиот јазик Python.")
