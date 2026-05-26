import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("Student Performance UI Dashboard")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Academic Features")
    hours_studied = st.slider("Weekly Study Hours", 0, 100, 24, help="Hours studied per week")
    attendance = st.slider("Attendance (%)", 75, 100, 85)
    previous_scores = st.slider("Previous Scores", 0, 100, 80)
    tutoring_sessions = st.slider("Tutoring Sessions", 0, 10, 3)
    physical_activity = st.slider("Physical Activity (Hours)", 0, 8, 4)

with col2:
    st.subheader("👥 Social & Environment")
    gender = st.selectbox("Gender", ["Male", "Female"]) # GENDER Enum
    access_to_resources = st.selectbox("Access to Resources", ["High", "Medium", "Low"]) # Resource Enum
    parental_involvement = st.selectbox("Parental Involvement", ["High", "Medium", "Low"]) # Involvement Enum
    parental_education_level = st.selectbox("Parent's Education", ["HighSchool", "College", "Postgraduate"])
    internet_access = st.selectbox("Internet Access", ["Yes", "No"])

with col3:
    st.subheader("🎯 Personal & Lifestyle")
    sleep_hours = st.number_input("Weekly Sleep Hours", min_value=0, value=42)
    extracurricular_activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    motivation_level = st.selectbox("Motivation Level", ["High", "Medium", "Low"])
    family_income = st.selectbox("Family Income", ["High", "Medium", "Low"])
    teacher_quality = st.selectbox("Teacher Quality", ["High", "Medium", "Low"])
    school_type = st.selectbox("School Type", ["Public", "Private"])
    peer_influence = st.selectbox("Peer Influence", ["Positive", "Neutral", "Negative"])
    learning_disabilities = st.selectbox("Learning Disabilities", ["Yes", "No"])
    distance_from_home = st.selectbox("Distance From Home", ["Near", "Moderate", "Far"])


st.markdown("---")

if st.button("🚀 Predict Performance Score", use_container_width=True):
    payload = {
        "Hours_Studied": hours_studied,
        "Sleep_Hours": sleep_hours,
        "Gender": gender,
        "Access_to_Resources": access_to_resources,
        "Attendance": attendance,
        "Parental_Involvement": parental_involvement,
        "Extracurricular_Activities": extracurricular_activities,
        "Previous_Scores": previous_scores,
        "Motivation_Level": motivation_level,
        "Internet_Access": internet_access,
        "Tutoring_Sessions": tutoring_sessions,
        "Family_Income": family_income,
        "Teacher_Quality": teacher_quality,
        "School_Type": school_type,
        "Peer_Influence": peer_influence,
        "Physical_Activity": physical_activity,
        "Learning_Disabilities": learning_disabilities,
        "Parental_Education_Level": parental_education_level,
        "Distance_from_Home": distance_from_home
    }

    api_url = "https://student-performance-project-1.onrender.com/predict"

    with st.spinner("Calculating performance score via API..."):
        try:
            response = requests.post(api_url, json=payload)

            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.text)

            if response.status_code in [200, 201]:
                result = response.json()

                predicted_score = result["Predicted_Mark"][0]
                final_score = round(predicted_score, 2)

                st.success(f"🎯 Predicted Student Performance Score: **{final_score}**")

            else:
                st.error(f"❌ Error {response.status_code}")

        except Exception as e:
            st.error(f"REAL ERROR: {e}")
