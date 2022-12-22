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
    sns.set_palette("pastel")
    plt.pie(df_csv["gender"].value_counts(), labels = ["Female", "Male"], autopct = "%1.1f%%")
    plt.title('Gender Ratio')
    buf = io.BytesIO()
    plt.savefig(buf, format = 'png', bbox_inches='tight')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    gender = urllib.parse.quote(string)
    return gender
    
