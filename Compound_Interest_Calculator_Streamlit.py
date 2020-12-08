"""
Created on Tue Dec  8 01:34:29 2020
@author: ISH KAPOOR
"""
import streamlit as st
import pandas as pd
from PIL import Image

Year_List = [2, 3, 4, 5, 6, 7, 8, 9, 10]
isNotHome = True

st.write("""
# Interest Calculator!
         """)

st.sidebar.header("User Input Values")
menu = [
    "Home", "Simple Interest Calculator", "Compound Interest Calculator",
    "About"
]
choice = st.sidebar.selectbox("Menu:", menu)


def user_input_features():

    min_Int_Rate_value = 6.0
    max_Int_Rate_value = 42.0
    default_Int_Rate_value = 10.0
    default_Principal_value = 10000
    default_Year_value = 2  # This is the index value of Year_List, i.e. Year_List[2] = 4

    Int_Rate = st.sidebar.slider('Interest Rate (in %)', min_Int_Rate_value,
                                 max_Int_Rate_value, default_Int_Rate_value)

    Principal = st.sidebar.text_input('Select Input Principal Amount',
                                      default_Principal_value)

    No_Of_Years = st.sidebar.selectbox('Select No. of Years', Year_List,
                                       default_Year_value)

    data = {
        'Int_Rate': Int_Rate,
        'Principal': Principal,
        'No_Of_Years': No_Of_Years,
    }

    features = pd.DataFrame(data, index=[0])

    return features


def Compound_Interest(Principal, Int_Rate, No_Of_Years):

    comp = 1.0
    # Compound_Interest = Principal * ((1 + (Int_Rate/n)) ** (n*No_Of_Years))

    for i in range(
            0, int(No_Of_Years)
    ):  # This for loop is same as comp = (1 + Int_Rate/100) ** No_Of_Years
        comp = comp * (1 + Int_Rate / 100)
    comp = float(Principal) * (comp - 1)

    comp_text = str("Compund Interest is " + str("%.3f" % comp))
    st.write(comp_text)
    data_1 = {'Computed_Compound_Interest': comp_text}
    result = pd.DataFrame(data_1, index=[0])

    return result


def Simple_Interest(Principal, Int_Rate, No_Of_Years):

    simp = 1.0
    # Simple_Interest = Principal * (1 + (Int_Rate * No_Of_Years))

    simp = float(Principal) * float(Int_Rate) * No_Of_Years * 0.01

    simp_text = str("Simple Interest is " + str("%.3f" % simp))
    st.write(simp_text)
    data_1 = {'Computed_Simple_Interest': simp_text}
    result = pd.DataFrame(data_1, index=[0])

    return result


df = user_input_features()

if choice == "Home":
    image = Image.open('Simple Interest Compound Interest Formula.jpg')
    st.image(image, use_column_width=True)
    isNotHome = False

elif choice == "Compound Interest Calculator":
    st.subheader('User enetered parameters for Rate, Principal amount and ')
    st.write(df)
    st.subheader('The calcuated compound interest is:')
    df_1 = Compound_Interest(df.Principal, df.Int_Rate, df.No_Of_Years)
    st.write(df_1)
    isNotHome = True

elif choice == "Simple Interest Calculator":
    st.subheader('User enetered parameters for Rate, Principal amount and ')
    st.write(df)
    st.subheader('The calcuated simple interest is:')
    df_2 = Simple_Interest(df.Principal, df.Int_Rate, df.No_Of_Years)
    st.write(df_2)
    isNotHome = True

else:
    st.write('Enjoy!')
    isNotHome = False
