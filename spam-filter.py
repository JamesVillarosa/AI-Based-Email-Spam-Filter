import tkinter as tk                                                        # Importing for GUI
import os                                                                   # For writing and reading file
import re                                                                   # For regular expression
from tkinter import filedialog 

def read_folder(folder_path):
    vocabulary = []                                                         # Array for all words
    words_frequency = {}                                                    # Dictionary for unique words and their frequency

    dir_list = os.listdir(folder_path)                                      # Getting all file inside the folder
    for file_name in dir_list:                                              # Traversing all file inside folder
        file_path = os.path.join(folder_path, file_name)                    # Constructing the file path               

        if os.path.isfile(file_path):                                       # Check if file path exist
            with open(file_path, 'r', encoding='latin-1') as f:             # Read the file in latin-1
                tokenize = f.read().split()                                 # Read the content of the file and splitting the words by white spaces
                regex = re.compile('[^a-zA-Z]')                             # Initializing regex for small and big alphabet only

                for i in tokenize:                                          # We will clean the tokenize words
                    clean = regex.sub('', i).lower()                        # Removing the non alphabet
                    if clean:
                        vocabulary.append(clean)                            # If word exist, append in vocabulary


    unique_words = set(vocabulary)                                          # Get rid of the duplicates
    for word in unique_words:
        words_frequency[word] = vocabulary.count(word)                      # Traversing the unique words and appending the words in dictionary together with its frequency

    return vocabulary, words_frequency                                      # Return the vocubularu and the words and their frequency



def calculate_probabilities(bow_spam, bow_ham, classify_folder, smoothing_factor):
    classify_files = os.listdir(classify_folder)                            # List all files in the classification folder

                                                                            # Get total word counts and unique word counts for spam and ham
    spam_total_words = len(bow_spam[0])                                     # Total words in spam
    ham_total_words = len(bow_ham[0])                                       # Total words in ham    
    spam_unique_words = len(bow_spam[1])                                    # Unique words in spam
    ham_unique_words = len(bow_ham[1])                                      # Unique words in ham

    spam_word_probabilities = {}                                            # Dictionaries to store word probabilities
    ham_word_probabilities = {}

    for word in bow_spam[1]:                                                # Calculate probabilities for words in spam
        word_count = bow_spam[1].get(word, 0)                               # Get count of the word in spam
        spam_word_probabilities[word] = (word_count + smoothing_factor) / (spam_total_words + smoothing_factor * spam_unique_words)


                                                                            # Calculate probabilities for words in ham
    for word in bow_ham[1]:
        word_count = bow_ham[1].get(word, 0)                                # Get count of the word in ham
        ham_word_probabilities[word] = (word_count + smoothing_factor) / (ham_total_words + smoothing_factor * ham_unique_words)


    output_lines = []                                                       # List to store the classification results


    for file_name in classify_files:                                        # Classify each file in the classification folder

        file_path = os.path.join(classify_folder, file_name)                # Construct the file path

        if os.path.isfile(file_path):                                       # Check if it's a valid file
            with open(file_path, 'r', encoding='latin-1') as f:

                content = f.read().split()                                  # Read and clean the content of the file
                regex = re.compile('[^a-zA-Z]')                             # Regex to filter out non-alphabetic characters
                clean_words = [regex.sub('', token).lower() for token in content if regex.sub('', token)]

            spam_prob = 1                                                   # Initialize probabilities for spam and ham
            ham_prob = 1


            for word in clean_words:                                        # Calculate the probabilities for the words in the cleaned content

                                                                            # Get the probability of the word being in spam or ham
                spam_prob *= spam_word_probabilities.get(word, smoothing_factor / (spam_total_words + smoothing_factor * spam_unique_words))
                ham_prob *= ham_word_probabilities.get(word, smoothing_factor / (ham_total_words + smoothing_factor * ham_unique_words))


            if spam_prob > ham_prob:                                        # Determine if the file is classified as Spam or Ham
                classification = "Spam"
                probability = spam_prob
            else:
                classification = "Ham"
                probability = ham_prob

    
            output_lines.append(f"{file_name}\t{classification}\t{probability}")    # Append the result to the output lines


    return output_lines, spam_total_words, spam_unique_words, ham_total_words, ham_unique_words     # Return the classification results and word counts



def select_folder():
    root = tk.Tk()                                                          # Opening file manager for user to choose file
    root.withdraw()                                                         # Hide the root window

    parent_folder = filedialog.askdirectory()                               # Getting directory

    spam_folder = os.path.join(parent_folder, 'spam')
    ham_folder = os.path.join(parent_folder, 'ham')                         # Set paths for spam, ham, and classify folders
    classify_folder = os.path.join(parent_folder, 'classify')

    bow_spam = read_folder(spam_folder)                                     # Gets all words from the spam folder                                  
    bow_ham = read_folder(ham_folder)                                       # Gets all words from the ham folder    

    k = float(input("Enter the value of smoothing factor (k): "))           # Ask for k

                                                                            # Call for calculate probabilities with the following variable need
    classify_output, spam_total_words, spam_unique_words, ham_total_words, ham_unique_words = calculate_probabilities(bow_spam, bow_ham, classify_folder, k)

    with open("classify.out", "w") as f:                                    # Write the result in classify.out 
        f.write("SPAM\n")
        f.write(f"Total Words: {spam_total_words}\n")                       # Write the spam's total words and dictionary size
        f.write(f"Dictionary Size: {spam_unique_words}\n\n")
        f.write("HAM\n")
        f.write(f"Total Words: {ham_total_words}\n")                        # Write the ham's total words and dictionary size
        f.write(f"Dictionary Size: {ham_unique_words}\n\n")

        f.write(f"k = {k}\n\n")                                             # Write the inputted k

        for line in classify_output:                                        # Write each classification result (spam or ham) to the file
            f.write(line + "\n")

    print("Output Written.")                                                # Indicator that program is finished



select_folder()