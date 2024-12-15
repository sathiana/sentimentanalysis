from textblob import TextBlob
text =  "I think jayagopi is excellent person, he is very happy person in general"
analysis = TextBlob(text)
polarity = analysis.sentiment.polarity
if polarity > 0:
    print("The text is positive")
elif polarity == 0:
    print("The text is Neutral")
else:
    print("The text is negative")