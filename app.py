import streamlit as st 
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("🫀 Heart Stroke Prediction")
st.markdown("Provide the following details")

# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# When Predict is clicked
if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")


# import streamlit as st
# import pandas as pd
# import joblib

# # ==========================================================
# # PAGE CONFIG
# # ==========================================================

# st.set_page_config(
#     page_title="Heart Stroke Prediction",
#     page_icon="🫀",
#     layout="wide"
# )


# # ==========================================================
# # CUSTOM CSS + HOSPITAL BACKGROUND
# # ==========================================================

# st.markdown("""
# <style>

# /* ---------------------------------------------------------
#    HOSPITAL BACKGROUND
# --------------------------------------------------------- */

# .stApp {
#     background-image:
#         linear-gradient(
#             rgba(5, 20, 35, 0.78),
#             rgba(5, 20, 35, 0.88)
#         ),
#         url("https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=2000&q=90");

#     background-size: cover;
#     background-position: center;
#     background-attachment: fixed;
# }


# /* ---------------------------------------------------------
#    MAIN CONTAINER
# --------------------------------------------------------- */

# .block-container {
#     max-width: 1150px;
#     padding-top: 2rem;
#     padding-bottom: 3rem;
# }


# /* ---------------------------------------------------------
#    TITLE
# --------------------------------------------------------- */

# .title-box {
#     text-align: center;
#     padding: 25px 20px 10px 20px;
# }

# .title-box h1 {
#     color: white;
#     font-size: 44px;
#     font-weight: 800;
#     margin-bottom: 5px;
#     text-shadow: 0px 3px 15px rgba(0,0,0,0.5);
# }

# .title-box p {
#     color: #dbeafe;
#     font-size: 17px;
#     margin-top: 0px;
# }


# /* ---------------------------------------------------------
#    HEART ICON
# --------------------------------------------------------- */

# .heart-icon {
#     font-size: 55px;
#     margin-bottom: -10px;
# }


# /* ---------------------------------------------------------
#    GLASS CARD
# --------------------------------------------------------- */

# .glass-card {
#     background: rgba(15, 30, 45, 0.78);
#     backdrop-filter: blur(14px);
#     -webkit-backdrop-filter: blur(14px);

#     border: 1px solid rgba(255,255,255,0.16);
#     border-radius: 22px;

#     padding: 25px;

#     margin-top: 20px;
#     margin-bottom: 20px;

#     box-shadow:
#         0 15px 40px rgba(0,0,0,0.35);
# }


# /* ---------------------------------------------------------
#    SECTION TITLE
# --------------------------------------------------------- */

# .section-title {
#     color: #ffffff;
#     font-size: 23px;
#     font-weight: 700;
#     margin-bottom: 15px;
# }

# .section-title span {
#     color: #60a5fa;
# }


# /* ---------------------------------------------------------
#    INPUT LABELS
# --------------------------------------------------------- */

# label {
#     color: #e5e7eb !important;
#     font-weight: 600 !important;
# }


# /* ---------------------------------------------------------
#    INPUT BOXES
# --------------------------------------------------------- */

# div[data-baseweb="select"] > div {
#     background-color: rgba(15, 23, 42, 0.88) !important;
#     border: 1px solid rgba(148,163,184,0.4) !important;
#     border-radius: 10px !important;
# }

# div[data-baseweb="input"] > div {
#     background-color: rgba(15, 23, 42, 0.88) !important;
#     border: 1px solid rgba(148,163,184,0.4) !important;
#     border-radius: 10px !important;
# }

# input {
#     color: white !important;
# }


# /* ---------------------------------------------------------
#    SLIDER
# --------------------------------------------------------- */

# .stSlider {
#     padding-top: 5px;
# }


# /* ---------------------------------------------------------
#    PREDICT BUTTON
# --------------------------------------------------------- */

# .stButton > button {

#     width: 100%;
#     height: 60px;

#     border-radius: 15px;
#     border: none;

#     background: linear-gradient(
#         135deg,
#         #2563eb,
#         #0ea5e9
#     );

#     color: white;

#     font-size: 20px;
#     font-weight: 700;

#     box-shadow:
#         0 8px 25px rgba(14,165,233,0.35);

#     transition: 0.3s;
# }

# .stButton > button:hover {

#     transform: translateY(-3px);

#     box-shadow:
#         0 12px 35px rgba(14,165,233,0.5);

#     background: linear-gradient(
#         135deg,
#         #1d4ed8,
#         #0284c7
#     );
# }


# /* ---------------------------------------------------------
#    RESULT BOX
# --------------------------------------------------------- */

# .result-high {

#     background: rgba(127, 29, 29, 0.75);

#     border: 1px solid rgba(248,113,113,0.5);

#     border-radius: 18px;

#     padding: 25px;

#     text-align: center;

#     margin-top: 25px;

#     color: #fecaca;

#     font-size: 25px;

#     font-weight: 700;

#     box-shadow:
#         0 10px 30px rgba(127,29,29,0.3);
# }


# .result-low {

#     background: rgba(20, 83, 45, 0.75);

#     border: 1px solid rgba(74,222,128,0.5);

#     border-radius: 18px;

#     padding: 25px;

#     text-align: center;

#     margin-top: 25px;

#     color: #bbf7d0;

#     font-size: 25px;

#     font-weight: 700;

#     box-shadow:
#         0 10px 30px rgba(20,83,45,0.3);
# }


# /* ---------------------------------------------------------
#    FOOTER
# --------------------------------------------------------- */

# .footer {

#     text-align: center;

#     color: #cbd5e1;

#     font-size: 14px;

#     margin-top: 30px;

#     padding: 15px;
# }

# .footer strong {
#     color: white;
# }

# </style>
# """, unsafe_allow_html=True)


# # ==========================================================
# # HEADER
# # ==========================================================

# st.markdown("""
# <div class="title-box">

#     <div class="heart-icon">🫀</div>

#     <h1>Heart Stroke Prediction</h1>

#     <p>
#         AI-Powered Heart Disease Risk Assessment System
#     </p>

# </div>
# """, unsafe_allow_html=True)


# # ==========================================================
# # LOAD MODEL
# # ==========================================================

# model = joblib.load("KNN_heart.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("columns.pkl")


# # ==========================================================
# # PATIENT INFORMATION CARD
# # ==========================================================

# st.markdown("""
# <div class="glass-card">

# <div class="section-title">
# 👤 <span>Patient Information</span>
# </div>

# </div>
# """, unsafe_allow_html=True)


# # ==========================================================
# # COLLECT USER INPUT
# # ==========================================================

# col1, col2 = st.columns(2)

# with col1:

#     age = st.slider(
#         "Age",
#         18,
#         100,
#         40
#     )

#     sex = st.selectbox(
#         "Sex",
#         ["M", "F"]
#     )

#     chest_pain = st.selectbox(
#         "Chest Pain Type",
#         ["ATA", "NAP", "TA", "ASY"]
#     )

#     resting_bp = st.number_input(
#         "Resting Blood Pressure (mm Hg)",
#         80,
#         200,
#         120
#     )

#     cholesterol = st.number_input(
#         "Cholesterol (mg/dL)",
#         100,
#         600,
#         200
#     )


# with col2:

#     fasting_bs = st.selectbox(
#         "Fasting Blood Sugar > 120 mg/dL",
#         [0, 1]
#     )

#     resting_ecg = st.selectbox(
#         "Resting ECG",
#         ["Normal", "ST", "LVH"]
#     )

#     max_hr = st.slider(
#         "Max Heart Rate",
#         60,
#         220,
#         150
#     )

#     exercise_angina = st.selectbox(
#         "Exercise-Induced Angina",
#         ["Y", "N"]
#     )

#     oldpeak = st.slider(
#         "Oldpeak (ST Depression)",
#         0.0,
#         6.0,
#         1.0
#     )


# # ==========================================================
# # ST SLOPE
# # ==========================================================

# st.markdown("""
# <div class="glass-card">

# <div class="section-title">
# ❤️ <span>Additional Cardiac Parameter</span>
# </div>

# </div>
# """, unsafe_allow_html=True)


# st_slope = st.selectbox(
#     "ST Slope",
#     ["Up", "Flat", "Down"]
# )


# # ==========================================================
# # PREDICT BUTTON
# # ==========================================================

# st.markdown("<br>", unsafe_allow_html=True)

# button_col1, button_col2, button_col3 = st.columns(
#     [1, 2, 1]
# )

# with button_col2:

#     if st.button("🔍  Predict Heart Disease Risk"):

#         # Create a raw input dictionary
#         raw_input = {
#             'Age': age,
#             'RestingBP': resting_bp,
#             'Cholesterol': cholesterol,
#             'FastingBS': fasting_bs,
#             'MaxHR': max_hr,
#             'Oldpeak': oldpeak,
#             'Sex_' + sex: 1,
#             'ChestPainType_' + chest_pain: 1,
#             'RestingECG_' + resting_ecg: 1,
#             'ExerciseAngina_' + exercise_angina: 1,
#             'ST_Slope_' + st_slope: 1
#         }

#         # Create input dataframe
#         input_df = pd.DataFrame([raw_input])

#         # Fill in missing columns with 0s
#         for col in expected_columns:
#             if col not in input_df.columns:
#                 input_df[col] = 0

#         # Reorder columns
#         input_df = input_df[expected_columns]

#         # Scale the input
#         scaled_input = scaler.transform(input_df)

#         # Make prediction
#         prediction = model.predict(scaled_input)[0]

#         # Show result
#         if prediction == 1:

#             st.markdown("""
#             <div class="result-high">

#                 ⚠️ High Risk of Heart Disease

#                 <div style="
#                     font-size:15px;
#                     font-weight:400;
#                     margin-top:10px;
#                     color:#fecaca;
#                 ">
#                     Please consult a qualified healthcare professional
#                     for further evaluation.
#                 </div>

#             </div>
#             """, unsafe_allow_html=True)

#         else:

#             st.markdown("""
#             <div class="result-low">

#                 ✅ Low Risk of Heart Disease

#                 <div style="
#                     font-size:15px;
#                     font-weight:400;
#                     margin-top:10px;
#                     color:#bbf7d0;
#                 ">
#                     The model predicts a lower estimated risk.
#                 </div>

#             </div>
#             """, unsafe_allow_html=True)


# # ==========================================================
# # FOOTER
# # ==========================================================

# st.markdown("""
# <div class="footer">

#     🫀 <strong>Heart Stroke Prediction System</strong>

#     <br><br>

#     Developed by <strong>Saurabh</strong>
#     | Machine Learning Project

#     <br><br>

#     ⚠️ This application is developed for educational purposes
#     and should not be used as a substitute for professional
#     medical diagnosis.

# </div>
# """, unsafe_allow_html=True)