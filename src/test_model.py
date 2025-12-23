#This test file is only for BERT's tests

import torch
import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import matthews_corrcoef

actuals = []
predictions = []

model_path = "models/Bert Model" #Loads the model
model = AutoModelForSequenceClassification.from_pretrained(model_path)

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased') #Loads the BERT tokenizer

#Recreate the test set
df = pd.read_csv("data/raw/bbc_data.csv")
df = df.rename(columns={'data': 'text', 'labels': 'category'})

train_df, temp_df = train_test_split(df, test_size=0.2, random_state=42) #Uses the same random state we used when training
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

print(f"\nTest set size: {len(test_df)} samples.")

def predict(text): #Prediction function
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    prediction = torch.argmax(probabilities).item()
    confidence = torch.max(probabilities).item() * 100

    return prediction, confidence


correct = 0 #Initializes the counters
total = len(test_df)

print(f"Running the test on {total} samples.")

label_map = { #Maps the numbers to readable categories
        0: "entertainment",
        1: "business",
        2: "sport",
        3: "politics",
        4: "tech"
    }
    

for i in range(total): #Loop through the entire test set
    text = test_df.iloc[i]['text']
    actual = test_df.iloc[i]['category']
    
    guess_idx, uselessconfidence = predict(text) #Get the prediction
    
    category_to_id = {v: k for k, v in label_map.items()}
    actual_idx = category_to_id[actual.lower()]
    
    actuals.append(actual_idx)
    predictions.append(guess_idx)
    
    
    
    
    
    if label_map[guess_idx].lower() == actual.lower():
        correct += 1
        
        
mcc_score = matthews_corrcoef(actuals, predictions)


accuracy = (correct / total) * 100 #Calculates the final score
print(f"\nFinal Results:")
print(f"Total Tested: {total}")
print(f"Correct Predictions: {correct}")
print(f"Final Accuracy: {accuracy:.2f}%")
print(f"Matthews Correlation Coefficient: {mcc_score:.4f}")



print("\nHere are some stress tests!") #Stress tests
live_headline = "The central bank raised interest rates to combat inflation today." #Find a news source outside of the data

guess, conf = predict(live_headline)
print(f"Headline: {live_headline}")
print(f"Prediction: {label_map[guess]} ({conf:.2f}% confidence)")

live_headline = "Bleepity bloopity blop! Blorg blorg blop." #Absolute gibberish to see how the model responds

guess, conf = predict(live_headline)
print(f"Headline: {live_headline}")
print(f"Prediction: {label_map[guess]} ({conf:.2f}% confidence)")

live_headline = "Ar ar ar ar ar ar ar ar." #Absolute gibberish to see how the model responds

guess, conf = predict(live_headline)
print(f"Headline: {live_headline}")
print(f"Prediction: {label_map[guess]} ({conf:.2f}% confidence)")



live_headline = "Football" #Football

guess, conf = predict(live_headline)
print(f"Headline: {live_headline}")
print(f"Prediction: {label_map[guess]} ({conf:.2f}% confidence)")