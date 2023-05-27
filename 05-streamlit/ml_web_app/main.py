import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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


# classifier
def get_classifier(clf_name, params):
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVM":
        clf = SVC(C=params["C"])
    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"], 
                                     max_depth=params["max_depth"], random_state=40)
        
    return clf

clf = get_classifier(classifier_name, classifier_params)

# classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
st.write(f"Classifier = {classifier_name}")
st.write(f"Accuracy = {acc}")

# plot
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()

st.pyplot(fig)
