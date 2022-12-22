from deepface import DeepFace
demography = DeepFace.analyze("img4.jpg", actions = ['age', 'gender'])
print("Age: ", demography["age"])
print("Gender: ", demography["gender"])