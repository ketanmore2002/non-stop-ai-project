import streamlit as st
import newspaper

def extract_article_info(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    return {
        "Title": article.title,
        "Publish Date": article.publish_date,
        "Text": article.summary,
        "keywords":", ".join(article.keywords),
    }

def main():
    st.title("Article Information Extractor (washingtonpost.com)")

    article_url = st.text_input("Enter the link of the article:")

    if st.button("Submit"):
        if article_url:
            article_info = extract_article_info(article_url)

            st.subheader("Article Information:")
            st.write(f"**Title:** {article_info['Title']}")
            st.write(f"**Publish Date:** {article_info['Publish Date']}")
            st.subheader("Article Text Summary:")
            st.write(article_info['Text'])
            st.subheader("Keywords:")
            st.write(article_info['keywords'])
        else:
            st.warning("Please enter the link of the article.")

if __name__ == "__main__":
    main()
