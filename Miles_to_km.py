import streamlit as st

st.set_page_config(
    page_title="Miles to KM Converter",
    page_icon="🚘",
    layout="centered"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#E3F2FD,#FFFFFF);
}

/* Title */
h1{
    text-align:center;
    color:#1565C0;
    font-size:45px;
    font-weight:700;
}

/* Number Input */
.stNumberInput input{
    border-radius:12px;
    border:2px solid #1565C0;
    font-size:18px;
}

/* Button */
div.stButton > button{
    width:100%;
    height:55px;
    background:#1565C0;
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    transition:0.3s;
}

div.stButton > button:hover{
    background:#0D47A1;
    color:white;
}

/* Result Card */
.result-card{
    background:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    margin-top:20px;
}

.result-value{
    color:#1565C0;
    font-size:35px;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)


st.title("🚘 Miles to Kilometer Converter")

st.markdown(
    "<h4 style='text-align:center;color:gray;'>Convert Miles into Kilometers Instantly</h4>",
    unsafe_allow_html=True
)

st.write("")


miles = st.number_input(
    "📍 Enter Distance (Miles)",
    min_value=0.0,
    step=0.1,
    format="%.2f"
)


if st.button("Convert"):

    km = miles * 1.60934

    st.markdown(f"""
    <div class="result-card">
        <h3>Conversion Result</h3>
        <div class="result-value">
            {km:.2f} Km
        </div>
        <br>
        <b>{miles:.2f} Miles = {km:.2f} Kilometers</b>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

st.markdown(
    "<div class='footer'>Made by <b>Deepak</b> using Python & Streamlit</div>",
    unsafe_allow_html=True
)