import pickle
import pandas as pd

# IMPORTING THE ML MODEL
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

# TEMP EXAMPLE
MODEL_VERSION = '1.0.0'

# getting output class labels from model (for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(userinput: dict):
    df = pd.DataFrame([userinput])
    predicted_class = model.predict(df)[0]

    # getting probablitites for all three classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    #mapping porbability to classname
    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities":class_probs
    }