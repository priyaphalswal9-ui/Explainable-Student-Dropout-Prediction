def predict_dropout(model, input_encoded):
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]
    return prediction, probability