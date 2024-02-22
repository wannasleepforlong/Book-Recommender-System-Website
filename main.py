import pandas as pd
import numpy as np
import pandas as pd
books = pd.read_csv('book-recommendation-dataset/Books.csv',low_memory=False)

# Load the DataFrame from the pickle file
pt = pd.read_pickle("pt.pickle")

from sklearn.metrics.pairwise import cosine_similarity
similarity_scores = cosine_similarity(pt)

def recommend(book_name):
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    
    return data





