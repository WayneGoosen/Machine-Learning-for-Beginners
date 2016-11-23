from sklearn import tree
import string

def contains_special_char(str):
    return any(char for char in str if char in string.punctuation)

def contains_digits(str):
    return any(char.isdigit() for char in str)

def contains_upper_case_char(str):
    return any(char for char in str if char.isupper())

def create_password_feature_set(password):
    length_feature = 1 if len(password) > 8 else 0
    upper_case_feature = 1 if contains_upper_case_char(password) else 0
    digits_feature = 1 if contains_digits(password) else 0
    special_char_feature = 1 if contains_special_char(password) else 0
    
    return [length_feature, 
            upper_case_feature, 
            digits_feature, 
            special_char_feature]

def get_labels_and_features(datalocation):
    labels = []
    features = []
    with open(datalocation) as datafile:
        for line in datafile.readlines() :
            line_items = line.strip('\n').split('|')
            features.append(create_password_feature_set(line_items[0]))
            labels.append(line_items[1])

    return labels, features

training_labels, training_features = get_labels_and_features(r"./Dataset/training.data")

# The classifier is a simple decision tree.
clf = tree.DecisionTreeClassifier()

# Training the classifier with the password features and their labels.
clf = clf.fit(training_features, training_labels)

test_labels, test_features = get_labels_and_features(r"./Dataset/testing.data")
    
# Predict labels for passwords.
prediction_labels = clf.predict(test_features)

# Calculate total correct predictions.
correct_count = 0
for test_label, prediction_label in zip(test_labels, prediction_labels):
    if test_label == prediction_label:
        correct_count = correct_count + 1

print "Prediction Acccuracy : " + str((float(correct_count) / len(prediction_labels)) * 100)

