import numpy as np
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import joblib
from PIL import Image


st.set_page_config(
        layout="wide",
        page_title= "Optimal Antidepressants Dosage Based On The Research",
        page_icon="🧠")
st.title("🧠 Optimal Antidepressants Dosage Based On The Research")


styl = """
<style>

.stApp {
/* background-image: url("https://www.bioaster.org/composants/uploads/2022/02/Diagnostics-1-1024x1024.jpg") !important; */
background-size: cover;
background: none;
h1
{
font-size: 32px;
}
button
{
    font-size: 24px;
    padding: 8px 25px;
    margin: 11px 0;
    background: #fff !important;
    color: #0274be !important;
}
code
{
background: none;
}
p
{
font-size: 17px;
background: #5379a7;
font-weight: 900;

}
button:hover, button:active, button:focus {
    color: #5379a7 !important;
}
.step-up,.step-down
{
display: none;
}
</style>
"""


st.markdown(styl, unsafe_allow_html=True)









# Load the model from the file
xgb_model = joblib.load('xgb_r.pkl')
gender_dict = {'Male': 1, 'Female': 2}
adpain_dict = {'NOT AT ALL':1,'A LITTLE BIT':2,'MODERATELY':3,'QUITE A BIT':4,'EXTREMELY':5}
region_dict = {'NORTHEAST':1,'MIDWEST':2,'SOUTH':3,'WEST':4}
race_dict = {'HISPANIC':1,'NON-HISPANIC WHITE ONLY':2,'NON-HISPANIC BLACK ONLY':3,
'NON-HISPANIC ASIAN ONLY':4,'NON-HISPANIC OTHER RACE OR MULTIPLE RACE':5}
marry_dict = {'MARRIED':1,'WIDOWED':2,'DIVORCED':3,'SEPARATED':4,'NEVER MARRIED':5, 
'UNDER AGE 16 - INAPPLICABLE':6}
cancer_dict = {'YES':1,'NO':2}
drug_dict= {'Amitriptyline':0,'Citalopram':3,'Escitalopram':9,'Fluoxetine':10,'Mirtazapine':13,'Nortriptyline':15,'Paroxetine':16,
           'Sertraline':18,'Trazodone':19,'Venlafaxine':21,'Vilazodone':22,'Vortioxetine':23,'Antipsychotic':26}

durationcat_dict = {'1 YEAR':1,'2 TO 4 YEARS':2, 'MORE THAN 5 YEARS':3}

agecat_dict = {'18-29':1, '30-44':2, '40-49':3,'50-59':4,'60 or above':5}
diabetes_dict = {'YES':1,'NO':0}
arthritis_dict = {'YES':1,'NO':0}

col1, col2, col3 = st.columns((1,1,1))

with col1:

  gender = st.selectbox('Gender', ('Male', 'Female'))
  adpain = st.selectbox("Pain interfered with normal work",
            ('NOT AT ALL','A LITTLE BIT','MODERATELY','QUITE A BIT','EXTREMELY'))
  region = st.selectbox("Region",('NORTHEAST','MIDWEST','SOUTH','WEST'))
  race = st.selectbox('RACE/ETHNICITY', ('HISPANIC','NON-HISPANIC WHITE ONLY','NON-HISPANIC BLACK ONLY',
  'NON-HISPANIC ASIAN ONLY','NON-HISPANIC OTHER RACE OR MULTIPLE RACE'))



with col2:

  durationcat = st.selectbox('Duration', ('1 YEAR','2 TO 4 YEARS', 'MORE THAN 5 YEARS'))
  agecat = st.selectbox('Age(years)', ('18-29', '30-44', '40-49','50-59','60 or above'))
  cancer = st.selectbox('Cancer Diagnosis', ('YES','NO'))
  diabetes = st.selectbox('DIABETES DIAGNOSIS', ('YES','NO'))


with col3:
  arthritis = st.selectbox('ARTHRITIS DIAGNOSIS', ('YES','NO'))
  drug = st.selectbox('Drug Category', (['Amitriptyline', 'Citalopram', 'Escitalopram', 'Fluoxetine', 'Mirtazapine', 
                                         'Nortriptyline', 'Paroxetine', 'Sertraline', 'Trazodone', 'Venlafaxine', 'Vilazodone', 'Vortioxetine', 'Antipsychotic']
))
  marry = st.selectbox('MARITAL STATUS', ('MARRIED','WIDOWED','DIVORCED','SEPARATED','NEVER MARRIED', 
  'UNDER AGE 16 - INAPPLICABLE'))
  adbmi = st.number_input('Body Mass Index',max_value=100, value=25)

predictions = xgb_model.predict(np.array([[gender_dict[gender],adpain_dict[adpain],region_dict[region],
  race_dict[race],marry_dict[marry],cancer_dict[cancer],drug_dict[drug],durationcat_dict[durationcat],
  agecat_dict[agecat],diabetes_dict[diabetes],arthritis_dict[arthritis],adbmi]]))

col4,col5,col6 = st.columns((1,1,1))
with col4:
   st.write("")
with col5:
   
  if st.button('Predict'):
      st.write("The dosage amount is: ", predictions[0].round(2), "mg/day")
  else:
      st.write("To get optimal dosage please fill all inputs and click on Predict button.")
with col6:
  st.write("")

