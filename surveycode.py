import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime

# File to store survey data


def get_info(answers, user_name):
    csv_file = 'survey_data.csv'
    excel_file = 'survey_data.xlsx'

    responses = {"user": user_name,
    "timestamp": datetime.now().isoformat(),
    "Strong_Password": int(answers[0]),
    "First_Time_User": int(answers[1]),
    "Likelihood_Reuse": int(answers[2]),
    "Likelihood_Recommend": int(answers[3]),
    "Additional_Comments": answers[4]}

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

        #Summary Statistics
    total_responses = len(df_combined)
    strong_yes = np.sum(df_combined["Strong_Password"] == 1)
    first_time_yes = np.sum(df_combined["First_Time_User"] == 1)

    avg_likelihood_reuse = pd.to_numeric(df_combined["Likelihood_Reuse"], errors='coerce').mean()
    avg_likelihood_recommend = pd.to_numeric(df_combined["Likelihood_Recommend"], errors='coerce').mean()

      # Output the Stats
    print(" Survey Summary Statistics ---")
    print( f"Total people who completed the survey: {total_responses}")
    print( f"Number of users who found the password strong: {strong_yes} ({(strong_yes/total_responses)*100:.2f}%)")
    print( f"Number of first-time users: {first_time_yes} ({(first_time_yes/total_responses)*100:.2f}%)")
    print( f"Average likelihood of reusing the password generator: {avg_likelihood_reuse:.2f} / 5")
    print( f"Average likelihood of recommending the password generator: {avg_likelihood_recommend:.2f} / 5")
    print("\nAdditional Comments:")

    #  Normalize Answers
    df_combined["Strong_Password"] = df_combined["Strong_Password"].map({1: 'Strong', 0: 'Weak'})
    df_combined["First_Time_User"] = df_combined["First_Time_User"].map({1: 'First Time', 0: 'Returning'})
    return df_combined

def show_graph(df):
    fig = plt.figure(figsize=(10, 5))
    fig.canvas.manager.set_window_title('User Responses')
    plt.subplot(1, 2, 1)
    strong_counts = df["Strong_Password"].value_counts()
    strong_counts.plot(kind='bar', color=['lightgreen'])
    plt.title("Strong Password Responses")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    for index, value in enumerate(strong_counts):
        plt.text(index, value + 0.1, str(value), ha='center', va='bottom')

    # --- First Time User Pie Chart ---
    plt.subplot(1, 2, 2)
    first_time_counts = df["First_Time_User"].value_counts()
    first_time_counts.plot(kind='bar', color=['blue'])
    plt.title("First Time User Responses")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    for index, value in enumerate(first_time_counts):
        plt.text(index, value + 0.1, str(value), ha='center', va='bottom')

    # Adjust layout and show plot
    plt.show()






