#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# In[ ]:


df = pd.read_excel('Input.xlsx')
df


# In[ ]:


Links_1=df.URL


# In[ ]:


List_1= Links_1.tolist()
List_1


# #  Data Scrapped from website given into the input.xlsx and Saved to directory       with Folder Name Extract1.

# In[ ]:


import requests
from bs4 import BeautifulSoup

for url in List_1:
    # Make an HTTP request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        div_content = soup.find('div', class_="td-post-content tagdiv-type")
        
        # Find the specific HTML element
        
        if div_content:
            # Extract text content from the specific element
            text_content = div_content.get_text()
        else:
            # If the specific element is not found, use a fallback element
            div_content = soup.find('div', class_="tdb-block-inner td-fix-index")
            if div_content:
                # Extract text content from the fallback element
                text_content = div_content.get_text()
            else:
                print(f"No 'td-post-content tagdiv-type' div found on {url}")
                continue  # Skip to the next URL if no content found
        
            # Extract URL ID from the URL
        url_id = url.split('/')[-2].replace('.html', '')
    
    # Specify the file path for saving the text file
        file_path = f"C:/Users/prakh/OneDrive/Desktop/BLACKASSIGNMENT/Extract1/{url_id}.txt"
  
    # Write the text content to a text file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        print(f"Text content extracted from {url} and saved to {file_path}")
    else:
        print(f"Failed to fetch URL: {url}")


# # Stop words brought from Directory

# In[ ]:


import os

# Directory path
directory = 'C:/Users/prakh/OneDrive/Desktop/BLACKASSIGNMENT/stopword/'

# List to store file paths
file_paths_2 = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(directory, filename)):
        # Optionally, you can filter files based on their extension or other criteria
        # For example, to select only text files:
        if filename.endswith('.txt'):
            file_paths_2.append(os.path.join(directory, filename))


# # Stop words stored in the form List in Variable A 

# In[ ]:


A = []

for file_path in file_paths_2:
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    A.append(lines)
    
Stop_Words = []
for sublist in A:
    Stop_Words.extend(sublist)


# In[ ]:





# #  Data Again brought from directory 

# In[ ]:


import os

# Directory path
directory = 'C:/Users/prakh/OneDrive/Desktop/BLACKASSIGNMENT/Extract1/'

# List to store file paths
file_paths = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(directory, filename)):
        # Optionally, you can filter files based on their extension or other criteria
        # For example, to select only text files:
        if filename.endswith('.txt'):
            file_paths.append(os.path.join(directory, filename))

# Print the list of file paths
#print(file_paths)


# # StopWords Have been Removed from original Extracted Text 

# In[ ]:


j=0
for i in range(len(file_paths)):
    with open(file_paths[i], 'r', encoding='utf-8') as f:
        Context = f.read()
        
    words_to_remove = A  

    # Split the text into words
    words =  Context.split()

    # Filter out the words to remove
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a sentence
    cleaned_text = ' '.join(filtered_words)
    j=j+1
    #print(cleaned_text)
    file_path_1 = file_paths[i]
    base_directory = 'C:/Users/prakh/OneDrive/Desktop/BLACKASSIGNMENT/Extract1/'

# Get the relative path from the base directory to the file
    url_id = os.path.relpath(file_path_1, base_directory)


# # Positive and Negative  words text format was  converted into List with variables and also removed common words present in the stopword and positive  and Negative word. Finally converted from List to Dictionary.

# In[ ]:


file_path = 'positive-words.txt'

# Read the content of the file
with open(file_path, 'r') as f:
    context = f.read()

# Split the content into a list using newline characters as the delimiter
Positive = context.split('\n')

Positive1 =Positive
Stop_Words1 = Stop_Words

new_Positive1= [item for item in Positive1 if item not in Stop_Words1]


# In[ ]:


file_path = 'negative-words.txt'

# Read the content of the file
with open(file_path, 'r') as f:
    context = f.read()

# Split the content into a list using newline characters as the delimiter
Negative = context.split('\n')

Negative1 =Negative
Stop_Words1 = Stop_Words

new_Negative1= [item for item in Negative1 if item not in Stop_Words1]


# # cleaned  file brought from Directory

# In[ ]:


import os

# Directory path
directory = 'C:/Users/prakh/OneDrive/Desktop/BLACKASSIGNMENT/Text_Clean/'

# List to store file paths
file_paths_3= []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(directory, filename)):
        # Optionally, you can filter files based on their extension or other criteria
        # For example, to select only text files:
        if filename.endswith('.txt'):
            file_paths_3.append(os.path.join(directory, filename))


# # All textual analysis( positive_score, negative_score, polarity_score, subjectivity_score,Average_Sentence_Length,percentage_complex_words,num_complex_words,average_word_length,Personal_Pronoun_1,average_words,totalWords_4,Context_Length,Syllable_Count_Per_Word,Fog_Index)  have been done from below Code.

# In[ ]:


import csv
import nltk
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
import string


# Make sure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

Personal_Pronoun= ['I', 'we','my','ours','us']

# Initialize lists to store the results
results = []

# Iterate over each file path
for i, file_path in enumerate(file_paths_3):
    with open(file_path, 'r', encoding='utf-8') as f:
        context = f.read()

    # Get the total number of words after cleaning
    total_words_after_cleaning = len(context)
        
    # Tokenize the text into words
    tokens = word_tokenize(context)

    # Initialize counter variables
    positive_score = 0
    negative_score = 0
    Personal_Pronoun_1 = 0

    # Iterate over each element in list Z (Positive Dictionary)
    for element in new_Positive1:
        # Count the occurrences of the element in list tokens and add it to the positive score
        positive_score += tokens.count(element)

    # Iterate over each element in list Z (Negative Dictionary)
    for element in new_Negative1:
        # Count the occurrences of the element in list tokens and add it to the negative score
        negative_score += tokens.count(element)

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    # Calculate Subjectivity Score
    subjectivity_score = (positive_score + negative_score) / (total_words_after_cleaning + 0.000001)
    
    word1 = word_tokenize(context)
    sentences = sent_tokenize(context)
    the_number_of_words = len(word1)
    the_number_of_sentences = len(sentences)
    if the_number_of_sentences != 0:
        Average_Sentence_Length = the_number_of_words / the_number_of_sentences
    else:     
        Average_Sentence_Length = 0
    
    words = context.split()
    num_complex_words = 0
    syllable_threshold = 2

    for word in words:
        syllables = syllapy.count(word)
        if syllables >syllable_threshold:
            num_complex_words += 1
    
    total_words = len(words)
    if total_words != 0:
        percentage_complex_words = (num_complex_words / total_words) * 100
    else:    
        percentage_complex_words =0
        
    words_2 = re.findall(r'\b[a-zA-Z]+\b',context)
    total_words_2 = len(words_2)
    if total_words_2 == 0:
        average_word_length = 0
    else:
        total_characters = sum(len(word) for word in words_2)
        average_word_length = total_characters / total_words_2
        
    Fog_Index = 0.4 * (Average_Sentence_Length + percentage_complex_words)    
        
        
    for element in Personal_Pronoun:
        # Count the occurrences of the element in list tokens and add it to the negative score
        Personal_Pronoun_1 += tokens.count(element)
        
        
    sentences_1 = sent_tokenize(context)

    total_words = sum(len(word_tokenize(sentence)) for sentence in sentences_1)
    total_sentences_1 = len(sentences_1)
    if total_sentences_1 > 0:
        average_words = total_words / total_sentences_1
    else:
        average_words = 0  
        
        
      
    words = nltk.word_tokenize(context)
    punctuations = set(string.punctuation)
    cleaned_words = [word for word in words if word.lower() not in stopwords.words('english') and word not in punctuations]
    totalWords_4 = len(cleaned_words)
    Context_Length = len(context) 
    
    
    Syllable_Count_Per_Word = 0

    for word in context.split():
        vowels = "aeiouAEIOU"
        syllable_count = 0
        previous_char_vowel = False
        if word.endswith(("es", "ed")):
            continue
        for char in word:
            if char in vowels:
                if not previous_char_vowel:
                    syllable_count += 1
                previous_char_vowel = True
            else:
                previous_char_vowel = False
        if len(word) == 1 and word.lower() != 'a':
            syllable_count = 0
        Syllable_Count_Per_Word += max(0, syllable_count)


    

    # Append results to the list
    results.append([i, file_path, positive_score, negative_score, polarity_score, subjectivity_score,Average_Sentence_Length,percentage_complex_words,num_complex_words,average_word_length,Personal_Pronoun_1,average_words,totalWords_4,Context_Length,Syllable_Count_Per_Word,Fog_Index])

# Write results to a CSV file
csv_filename = 'sentiment1.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(['Index', 'File Path', 'Positive Score', 'Negative Score', 'Polarity Score', 'Subjectivity Score','Average_Sentence_Length','percentage_complex_words','num_complex_words','average_word_length','Personal_Pronoun_1','average_words','totalWords_4','Context_Length','Syllable_Count_Per_Word','Fog_Index'])
    # Write rows
    writer.writerows(results)

print(f"Results saved to {csv_filename}")


# # all textual analysis operations have been performed on clean text( clean text is recived after removing stopwords from Extracted text from Blackcoffer website).

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




