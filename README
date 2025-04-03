# AI-Based Email Spam Filter

This repository contains a Python implementation of a Naïve Bayes Classifier for email spam filtering. It processes email datasets, builds bag-of-words representations, and classifies new emails as either "spam" or "ham" (non-spam).

## Features

* **Bag-of-Words Representation:** Converts email text into a numerical representation for analysis.
* **Naïve Bayes Classification:** Implements the Naïve Bayes algorithm for spam detection.
* **Laplace Smoothing:** Handles zero-frequency problems with Laplace smoothing (additive smoothing).
* **File-Based Processing:** Reads email data from specified folders.
* **Output to File:** Writes classification results to a `classify.out` text file.
* **GUI-Based Folder Selection:** Uses `tkinter` for easy folder selection.
* **Displays dictionary sizes and total word counts:** shows the statistics of the processed data.

## Getting Started

### Prerequisites

* Python 3.x
* `tkinter` (usually included with Python)

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/your-username/AI-Based-Email-Spam-Filter.git](https://www.google.com/search?q=https://github.com/your-username/AI-Based-Email-Spam-Filter.git)
    cd AI-Based-Email-Spam-Filter
    ```

### Usage

1.  Prepare your email dataset:
    * Create a parent folder containing three subfolders: `spam`, `ham`, and `classify`.
    * Place spam emails in the `spam` folder, ham emails in the `ham` folder, and emails to be classified in the `classify` folder (one email per file).

2.  Run the Python script:

    ```bash
    python your_script_name.py
    ```

    * The script will open a file dialog, allowing you to select the parent folder containing your email datasets.
    * You will be prompted to enter the smoothing factor `k`.
    * The classification results will be written to `classify.out`.

### Output Format (`classify.out`)

The `classify.out` file will contain the following information:

SPAM
Total Words: [spam_total_words]
Dictionary Size: [spam_unique_words]

HAM
Total Words: [ham_total_words]
Dictionary Size: [ham_unique_words]

k = [smoothing_factor]

[filename1]  [classification1]  [probability1]
[filename2]  [classification2]  [probability2]
...

* `[spam_total_words]` and `[spam_unique_words]` represent the total number of words and unique words in the spam dataset, respectively.
* `[ham_total_words]` and `[ham_unique_words]` represent the total number of words and unique words in the ham dataset, respectively.
* `[smoothing_factor]` is the value of `k` you entered.
* `[filename]` is the name of the file being classified.
* `[classification]` is either "Spam" or "Ham".
* `[probability]` is the calculated probability of the email being spam or ham.

### Example Dataset Structure
parent_folder/
├── spam/
│   ├── spam_email1.txt
│   ├── spam_email2.txt
│   └── ...
├── ham/
│   ├── ham_email1.txt
│   ├── ham_email2.txt
│   └── ...
└── classify/
├── classify_email1.txt
├── classify_email2.txt
└── ...

### Code Explanation

* `read_folder(folder_path)`: Reads emails from a folder, tokenizes the text, cleans the tokens, and returns the vocabulary and word frequencies.
* `calculate_probabilities(bow_spam, bow_ham, classify_folder, smoothing_factor)`: Calculates the Naïve Bayes probabilities for each email in the classify folder and determines whether each email is spam or ham.
* `select_folder()`: Uses `tkinter` to allow the user to select the parent folder, calls the other functions, and writes the results to `classify.out`.

### Note

* The script uses `encoding='latin-1'` when reading the email files. This encoding might need to be adjusted depending on the character encoding of your dataset.
* The regex `[^a-zA-Z]` is used to clean the words. If you want to include other characters, you should modify this regex.
* The smoothing factor `k` can significantly impact the performance of the classifier. Experiment with different values to find the optimal setting for your dataset.