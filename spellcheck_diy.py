import pandas as pd

#csv_path = '/Users/kajpeterson/Boggle/en_diy_lower.csv'
df = pd.read_csv("en_diy_lower.csv")
while True:
    word = input("Word to check:").lower()
    if word in df.values:
        print("True")
    else:
        print("Nope")
    if word == "q":
        break

# THIS SUCCESSFULLY CHECKS WORDS AGAINST EN
# but En is cut in half... why?!!!!
