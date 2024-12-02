import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('resources/survey_responses.csv')  # Load survey responses from CSV file

# Convert data into DataFrame
survey_responses = pd.DataFrame(data)

# Analysis
barrier_improvement_data = survey_responses.groupby('Significant_Barrier')['Improvement_Suggestions'].apply(lambda x: ', '.join(x.unique())).reset_index()
barrier_scores = survey_responses.groupby('Significant_Barrier').mean(numeric_only=True)

# Visualizations
# Plot 1: Age Group Distribution
age_groups = survey_responses['Age_Group'].value_counts()
age_groups.plot(kind='bar', figsize=(8, 6))
plt.title('Age Group Distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/age_group_distribution.png')

# Plot 2: Gender Distribution
gender_distribution = survey_responses['Gender'].value_counts()
gender_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(8, 6))
plt.title('Gender Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('images/gender_distribution.png')

# Plot 3: Assistive Device Usage
assistive_devices = survey_responses['Assistive_Device'].value_counts()
assistive_devices.plot(kind='bar', figsize=(8, 6), color='skyblue')
plt.title('Assistive Device Usage')
plt.xlabel('Uses Assistive Device')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/assistive_device_usage.png')

# Plot 4: Significant Barriers Identified
barrier_counts = survey_responses['Significant_Barrier'].value_counts()
barrier_counts.plot(kind='bar', figsize=(8, 6), color='orange')
plt.title('Significant Barriers Identified')
plt.xlabel('Barrier Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/significant_barriers.png')

# Plot 5: Interface Intuitiveness Scores
intuitiveness_scores = survey_responses['Interface_Intuitiveness']
intuitiveness_scores.plot(kind='hist', bins=5, edgecolor='black', alpha=0.7, figsize=(8, 6))
plt.title('Interface Intuitiveness Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('images/interface_intuitiveness_scores.png')

# Plot 6: Lighting Effect Scores
lighting_effect_scores = survey_responses['Lighting_Effect']
lighting_effect_scores.plot(kind='hist', bins=5, edgecolor='black', alpha=0.7, figsize=(8, 6), color='green')
plt.title('Lighting Effect on Usability Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('images/lighting_effect_scores.png')

# Plot 7: Average Usability Scores by Barrier
barrier_scores_plot = barrier_scores[['Physical_Ease_Standing', 'Physical_Ease_Seated',
                                      'Interface_Intuitiveness', 'Screen_Visibility', 
                                      'Lighting_Effect']]
barrier_scores_plot.plot(kind='bar', figsize=(10, 7))
plt.title('Average Usability Scores by Significant Barrier')
plt.ylabel('Average Score')
plt.xlabel('Significant Barrier')
plt.xticks(rotation=45)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()
plt.savefig('images/average_usability_scores_by_barrier.png')
