 

# Article Information Extractor (washingtonpost.com)

**Objective:**
Create a user-friendly application using Streamlit that allows users to input a link to an article. Upon clicking the submit button, the application extracts information from the provided article link and displays relevant details.

**Key Features:**
1. **User Interface:**
   - Simple and intuitive interface.
   - Input bar for users to enter the link of an article.
   - Submit button to trigger information extraction.

2. **Information Extraction:**
   - Utilizes the `newspaper3k` library to download and parse the article.
   - Extracts information such as the article title, keywords, publish date, and text summary.

3. **Output Display:**
   - Displays extracted information on the application interface.
   - Provides details about the article, including title, authors, and publish date.
   - Displays the full text of the article for user convenience.

**Workflow:**
1. User opens the desktop application with the help of Streamlit.
2. A user-friendly interface prompts the user to input the link to an article.
3. The user clicks the submit button to trigger the information extraction process.
4. Extracted information, including the article details and text, is displayed on the application interface.

**Technologies Used:**
- Python
- Streamlit
- newspaper3k
- logistic regression



## Installation

Step 1 : Installing Dependencies

```bash
   pip3 install -r requirements.txt
```

Step 2 : Streamlit Command to Run application in browser

```bash
   streamlit run app.py
```


## Screenshots

![App Screenshot](https://github.com/ketanmore2002/non-stop-ai-project/blob/main/image/Screenshot%202023-11-23%20at%203.51.02%20AM.png?raw=true)


![App Screenshot](https://github.com/ketanmore2002/non-stop-ai-project/blob/main/image/Screenshot%202023-11-23%20at%203.52.32%20AM.png?raw=true)

![App Screenshot](https://github.com/ketanmore2002/non-stop-ai-project/blob/main/image/Screenshot%202023-11-23%20at%203.52.52%20AM.png?raw=true)
## Files Structure

The **articles.csv** file contains all the scraped articles. 
**model.joblib** is model obtained from the project.
**app.py** contains code for running the streamlit application.
**non-stop-io.ipynb** is jupyter notebook used for working with **logistic regression** model and **newspaper3k**.
**Scraped datasets** folder contains raw unprocessed data. **report of the test evaluation.csv** file contains information obtained through grid search cv. ***env** folder shall be ignored/deleted*.
