import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def gender_analysis(df_csv):
    plt.figure()
    sns.set_palette("pastel")
    gender = plt.pie(df_csv["gender"].value_counts(), labels = ["Female", "Male"], autopct = "%1.1f%%")
    plt.title('Gender Ratio', fontweight='bold')
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    gender = urllib.parse.quote(string)
    buf.close()
    return gender


def age_analysis(df_csv):
    plt.figure()
    sns.set_palette("pastel")
    age = sns.displot(df_csv["age"], color='#8CBD97')
    plt.title("Age distribution", fontweight='bold')
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    age = urllib.parse.quote(string)
    buf.close()
    return age


def time_analysis(df_csv):
    df_csv["hour"] = df_csv["time"].astype(str).str[:2]
    df_csv["hour"] = df_csv["hour"].astype(int)
    plt.figure()
    sns.set_palette("pastel")
    time = sns.histplot(df_csv["hour"], color='pink')
    time.set_xticks(range(24))
    time.set_xticklabels([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    plt.title("Time distribution", fontweight='bold')
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    time = urllib.parse.quote(string)
    buf.close()
    return time
    
