import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
books = pd.read_csv('book-recommendation-dataset/Books.csv', low_memory=False)

# Load the DataFrame from the pickle file
pt = pd.read_pickle("pt.pickle")

from sklearn.metrics.pairwise import cosine_similarity
similarity_scores = cosine_similarity(pt)
books_list = pt.index

def recommend(book_name):
    matches = [title for title in pt.index if book_name.lower() in title.lower()]
    if not matches:
        st.error("Book not found in the dataset. Please select another book.")
        return []
    index = np.where(pt.index == matches[0])[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data



st.header(" :blue[BookSmash]")
st.write("###")
col1,col2,col3,col4 = st.columns(4)
with col1:
        st.image("http://images.amazon.com/images/P/059035342X.01.MZZZZZZZ.jpg")
with col2:
        st.image("http://images.amazon.com/images/P/0812543254.01.MZZZZZZZ.jpg")
with col3:
        st.image("http://images.amazon.com/images/P/0553381687.01.MZZZZZZZ.jpg")
with col4:
        st.image("http://images.amazon.com/images/P/0140445285.01.MZZZZZZZ.jpg")

st.write(""" <p> Welcome to <b style="color:blue">BookSmash</b> for quick and free books recommendations! </p>""",unsafe_allow_html=True)
st.write("##")
my_expander = st.expander("Tap to Select a Book 📚")
selectvalue = my_expander.selectbox("Select a Book", books_list, index=0)
print(selectvalue)
if my_expander.button("Recommend"):
    st.text("Here are the Recommendations..")
    st.write("#")
    L = recommend(selectvalue)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.text(L[0][0])
        st.image(L[0][2])
    with col2:
        st.text(L[1][0])
        st.image(L[1][2])
    with col3:
        st.text(L[2][0])
        st.image(L[2][2])
    with col4:
        st.text(L[3][0])
        st.image(L[3][2])

