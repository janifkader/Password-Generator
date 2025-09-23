import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime

# File to store survey data
csv_file = 'survey_data.csv'
excel_file = 'survey_data.xlsx'

#Survey Setup
print(" Welcome to the Password Generator Survey! \n")

user_name = input(" Please enter your name or alias: ").strip()

# Survey Questions and Columns
questions = { " Was the password strong and secure? (Yes/No)": "Strong_Password",
              " Is this your first time using a password generator? (Yes/No)": "First_Time_User",
                " How likely are you to use this password generator again? (1-5)": "Likelihood_Reuse",
                " How likely are you to recommend this password generator to others? (1-5)": "Likelihood_Recommend",
                " Any additional comments or feedback?": "Additional_Comments" .
                }
# Ask User for Responses and Collect Data from user Response
response = {"user": user_name, 
"timestamp": datetime.now().isoformat()}
print ("Please answer the following survey questions ---\n")
responses = {}
for question, column in questions.items():
    response = input(question + " ").strip()
    responses[column] = response

# Convert responses to DataFrame
response_df = pd.DataFrame([responses])

#Load existing Data if file exists 
if os.path.exists(csv_file):
    df_existing = pd.read_csv(csv_file)
    df_combined = pd.concat([df_existing, response_df], ignore_index=True)
    else:
        df_combined = response_df
   
    # Save updated DataFrame to CSV file and Excel
    df_combined.to_csv(csv_file, index=False)
    df_combined.to_excel(excel_file, index=False)
    
    #Show summary
    print(" 👍 😄 Thank you! Your response has been recorded.\n")

    #Summary Statistics
    total_responses = len (df_combined)
    strong_yes = np.sum (df_combined ["Strong_Password"].str.lower() == "yes")
    first_time_yes = np.sum (df_combined ["First_Time_User"].str.lower() == "yes")
    
    avg_likelihood_reuse = pd.to_numeric (df_combined ["Likelihood_Reuse"], errors='coerce').mean()
    avg_likelihood_recommend = pd.to_numeric (df_combined ["Likelihood_Recommend"], errors='coerce').mean()
  
  # Output the Stats
   print(" Survey Summary Statistics ---")
   print( f"Total people who completed the survey: {total_responses}")
   print( f"Number of users who found the password strong: {strong_yes} ({(strong_yes/total_responses)*100:.2f}%)")
   print( f"Number of first-time users: {first_time_yes} ({(first_time_yes/total_responses)*100:.2f}%)")
   print( f"Average likelihood of reusing the password generator: {avg_likelihood_reuse:.2f} / 5")
   print( f"Average likelihood of recommending the password generator: {avg_likelihood_recommend:.2f} / 5")
   print("\nAdditional Comments:")

#  Normalize Answers 
df_combined[Strong_Password] = df_combined[Strong_Password].str.lower().map({'yes': 'Strong', 'no': 'Weal'})
df_combined[First_Time_User] = df_combined[First_Time_User].str.lower().map({'yes': 'First Time', 'no': 'Returning'})

#Handle Missing Values or Malforme Data 
df[Strong_Password].fillna('Unknown', inplace=True)
df[First_Time_User].fillna('Unknown', inplace=True)

# Set up subplots
plt.figure(figsize=(10, 5))

# --- Strong Password Pie Chart ---
plt.subplot(1, 2, 1)
strong_counts = df_combined["Strong_Password"].value_counts()counts_sp.plot(Kind='bar', color=['skyblue')
plt.title("Strong Password Responses")
plt.xlabel("Response")
plt.ylabel("Count")
plt.xticks(rotation=0)
for index , value in enumerate(strong_counts):
    plt.text(index, value + 0.1, str(value), ha='center', va='bottom')

# --- First Time User Pie Chart ---
plt.subplot(1, 2, 2)
first_time_counts = df_combined["First_Time_User"].value_counts()
first_time_counts.plot(kind='bar', color=['lightgreen'])
plt.title("First Time User Responses")
plt.xlabel("Response")
plt.ylabel("Count")
plt.xticks(rotation=0)
for index, value in enumerate(first_time_counts):
    plt.text(index, value + 0.1, str(value), ha='center', va='bottom')

# Adjust layout and show plot
plt.tight_layout()
plt.show()






