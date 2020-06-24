import pandas as pd
import urllib.parse

df = pd.read_csv('email_gen.csv')

rows = len(df.index)
mail = "mailto:"

for i in range(rows):
    recipient = df['recipient'][i]
    subject = df['subject'][i]
    text = df['text'][i]
    #replace spaces, newlines, and escaped percent signs in body
    url = mail + mail + recipient + "?" + "&subject=" + subject.replace(" ", "%20") + "&body=" + urllib.parse.quote(text)
    print(url)