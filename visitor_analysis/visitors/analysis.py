import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def gender_analysis(df_csv):
    print(df_csv.head())
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
    print(df_csv["age"])
    plt.figure()
    sns.set_palette("pastel")
    age = sns.displot(df_csv["age"])
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
    plt.figure()
    sns.set_palette("pastel")
    age = sns.displot(df_csv["time"])
    plt.title("Time distribution", fontweight='bold')
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    time = urllib.parse.quote(string)
    buf.close()
    return time
    
