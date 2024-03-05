# Sentiment Score for Task Scheduling Algorithms Based on Text Analysis

Welcome to the Sentiment Score for Task Scheduling Algorithms project! This project involves analyzing task scheduling algorithms' descriptions and assigning sentiment scores based on text analysis. The sentiment analysis is performed using natural language processing techniques to evaluate the positivity of algorithm descriptions.

## Overview
The main objective of this project is to assign sentiment scores to task scheduling algorithms based on the language used to describe them. The sentiment analysis is conducted by analyzing the adjectives used in the descriptions of the algorithms. Priority scores are assigned to each algorithm based on the frequency and positivity of adjectives found in their descriptions.

## Prerequisites
- Python 3.x
- Pandas
- Matplotlib
- Regular Expressions (re)

## How to Use
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python 3.x installed and install the required dependencies using pip:
   ```
   pip install pandas matplotlib
   ```
3. **Prepare the Dataset**: Make sure you have the dataset containing algorithm descriptions ready for analysis.
4. **Run the Code**: Execute the provided Python script, ensuring to provide the correct file path to your dataset.
   ```python
   python sentiment_analysis.py
   ```
5. **Review Results**: The script will analyze the descriptions, assign sentiment scores to algorithms, and visualize the priority scores of the algorithms.

## Code Explanation
- The provided Python script reads the dataset containing algorithm descriptions.
- It extracts adjectives from the descriptions using regular expressions and calculates their frequencies.
- Adjectives' frequencies are used to calculate priority scores for each algorithm.
- The algorithm with the highest priority score is identified as having the best sentiment.
- Priority scores of algorithms are visualized using line and bar plots for easy interpretation.

## Enhancements
- **Documentation**: Add detailed comments and documentation to explain the code's functionality and purpose.
- **Error Handling**: Implement robust error handling mechanisms, especially when dealing with file operations and data parsing.
- **Optimization**: Optimize the code for better performance, especially when processing large datasets.
- **Modularization**: Consider breaking down the code into reusable functions for improved maintainability and readability.

Feel free to customize and extend this project based on your specific requirements and datasets!

## Contributors
- [Vijay Sai Kumar](https://github.com/vijay-svsk)
- [Sri Harsh](https://github.com/sriharsh-2003)
- [Kailash Varma](https://github.com/kailash123varma)

---
*Note: This project focuses on analyzing task scheduling algorithms' descriptions and assigning sentiment scores based on text analysis. Adjustments may be needed for different datasets or analysis objectives.*
