import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analysis(df):
    print(df.head())
    sns.set_palette("pastel")

    plt.pie(df["age"].value_counts(), labels = ["", ""], autopct = "%1.1f%%")
    plt.show()
