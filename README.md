# "The Differences Between Various Models in Processing Language"

Jack Brassil (SirCacto)
12/23/2025

This is an independent research project I decided to take on over winter break of 2025-2026. Essentially, I decided to train three different models and see the differences in how they behave. I trained a Logistic Regression model, an LSTM model, and a BERT model.

I used a BBC news dataset. Here's the link to where I got it from: https://www.kaggle.com/datasets/alfathterry/bbc-full-text-document-classification

Here's a citation to the dataset's original source:

Greene, D., & Cunningham, P. (2006). Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering.  *Proc. 23rd International Conference on Machine Learning (ICML’06)* , 377–384. [https://doi.org/10.1145/1143844.1143892](https://doi.org/10.1145/1143844.1143892)

In the Google Colab notebook, you can find training data for all three models. Additionally, you can find test code for the Logistic Regression and LSTM model. I tackled BERT first and initially wanted to test it locally, so the code for BERT''s tests is in test_model.py.

I've written a lovely report to go alongside all of this! The PDF can be found in the repository. It's the file "ML Project Report.pdf" in the "report" folder.

As I'm still relatively new to the world of machine learning, I apologize if I've made any missteps or gaps in my judgment. Additionally, while I believe I've cited anything correctly, please let me know if I've made any mistakes. I wouldn't be here without all of those helpful sources.

I've deployed the BERT model to Streamlit. Go ahead — try it out! Link: https://machinelearningnlpproject.streamlit.app/

I've also uploaded the BERT model to Hugging Face. This was mainly to store it in the cloud for the Streamlit website. If you want to check it out, here it is: https://huggingface.co/SirCacto/NLPBERTDec25

Thank you for checking out my project, and I hope you enjoy reading the report and playing around on the news classifier!
