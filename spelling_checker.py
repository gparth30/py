from textblob import TextBlob
line=input("Enter the word")

check=TextBlob(line).correct()
print("Incorrect word=>",line)
print("Corrected Word=>",check)