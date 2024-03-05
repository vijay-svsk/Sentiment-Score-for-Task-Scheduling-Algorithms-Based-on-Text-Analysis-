import pandas as pd
import re
import matplotlib.pyplot as plt

file_path = "/content/gdrive/MyDrive"
df = pd.read_csv(file_path)

adjective_frequencies = {}
total_algorithms = len(df)

for algorithm, features in zip(df["Algorithms/Model"], df["Features"]):
    # Use regular expression to extract adjectives from the "Features" column
    adjectives = re.findall(r'\b\w+\b', features.lower())
    for adjective in adjectives:
        if adjective.isalpha() and len(adjective) > 1:  # Ensure that the word is an adjective
            adjective_frequencies[adjective] = adjective_frequencies.get(
                adjective, 0) + 1

# Calculating the priority of each adjective based on its frequency
adjective_priority = {}
for adjective, frequency in adjective_frequencies.items():
    priority = frequency / total_algorithms
    adjective_priority[adjective] = priority

# Calculating the priority scores for each algorithm by summing up the priority of adjectives used in its "Features"
algorithm_priority_scores = {}

for algorithm, features in zip(df["Algorithms/Model"], df["Features"]):
    priority_score = 0
    adjectives = re.findall(r'\b\w+\b', features.lower())
    for adjective in adjectives:
        if adjective.isalpha() and len(adjective) > 1:  # Ensure that the word is an adjective
            priority_score += adjective_priority.get(adjective, 0)
    algorithm_priority_scores[algorithm] = priority_score

# Identifying the algorithm with the highest priority score (the algorithm with the best features)
best_algorithm = max(algorithm_priority_scores,
                     key=algorithm_priority_scores.get)

# Printing the algorithm with the best features
print("Algorithm with the best features:")
print(best_algorithm)

# Preparing the data for visualization
algorithms = list(algorithm_priority_scores.keys())
priority_scores = list(algorithm_priority_scores.values())
# Creating a line plot to visualize the priority scores of algorithms
plt.plot(algorithms, priority_scores)
plt.xlabel("Algorithm")
plt.ylabel("Priority")
plt.xticks(rotation=90)
plt.show()
# Creating a bar plot to visualize the priority scores of algorithms
plt.bar(algorithms, priority_scores)
plt.xlabel("Algorithm")
plt.ylabel("Priority")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()