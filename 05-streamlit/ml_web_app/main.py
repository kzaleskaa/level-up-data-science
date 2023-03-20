import pandas as pd
import streamlit as st
from sklearn import datasets

st.title("Streamlit example")

st.write("""
  # Explore different classifier
  Choose the best one
""")

# sidebar
st.sidebar.write("**Options**")
chosen_dataset = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Dataset"))
classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))

# datasets
def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    # return X, y 
    return (data.data, data.target)

X, y = get_dataset(chosen_dataset)
st.write(f"Shape of dataset: {X.shape}")
st.write(f"Number of classes: {len(pd.unique(y))}")

# classifier method
def add_method_parameters(method_name):
    params = {}
    if method_name == "KNN":
        params["K"] = st.sidebar.slider("K", 1, 15)
    elif method_name == "SVM":
        params["C"] = st.sidebar.slider("C", 0.01, 10.0)
    else:
        params["max_depth"] = st.sidebar.slider("max_depth", 2, 15)
        params["n_estimators"] = st.sidebar.slider("n_estimators", 1, 100)

    return params

classifier_params = add_method_parameters(classifier_name)
