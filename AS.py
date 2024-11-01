import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import nltk
from newspaper import Article

with st.sidebar:
    st.title("Article Summarizer.")
    st.markdown('''
        ## About:
        - this app takes Articles links to create summary about the article
        - this app is made using:
        - streamlite
        - nltk
        - newspaper
''')
    add_vertical_space(5)
    st.write("Made with ❤️ By Digendre Gendre")
REQUIRED_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    'maxent_treebank_pos_tagger',  # Required for NLTKTagger
    'movie_reviews',  # Required for NaiveBayesAnalyzer
    'wordnet',  # Required for lemmatization and Wordnet
    'stopwords'
]    
def main():
    
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each)
    print("Finished.")

    st.info("Copy URL of any Article and past it below to get summary of Article")
    st.header("Upload URL of your Article")
    url = st.text_input("",placeholder="Upload Article URL Here")
    if url:
        try:
            article = Article(url)

            article.download()
            article.parse()

            img = article.top_image
            st.image(img)

            title = article.title
            st.subheader(title)

            aurther = article.authors
            st.write(",".join(aurther))
            article.nlp()
            

            keywords = article.keywords
            st.subheader('Keywords:')
            st.write(', '.join(keywords))

            tab1, tab2= st.tabs(["Full Text", "Summary"])
            with tab1:
                txt = article.text
                txt = txt.replace('Advertisement', '')
                st.write(txt)
        
            with tab2:
                st.subheader('Summary')
                
                
                summary = article.summary
                summary = summary.replace('Advertisement', '')
                st.write(summary)
            st.balloons()    


        except:
            st.error("Wrong URL ")   
            

if __name__ == "__main__":
    main()                 

