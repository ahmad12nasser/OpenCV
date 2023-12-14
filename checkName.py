import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from sklearn.model_selection import train_test_split
from nltk.classify import accuracy

nltk.download('names')

def extract_features(word):
    return {'last_letter': word[-1]}

def load_and_preprocess_data():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                     [(name, 'female') for name in names.words('female.txt')])
    train_set, test_set = train_test_split(labeled_names, test_size=0.2, random_state=42)
    return train_set, test_set

def train_classifier(train_set):
    train_features = [(extract_features(name), gender) for (name, gender) in train_set]
    classifier = NaiveBayesClassifier.train(train_features)
    return classifier
def classify_name(classifier, name):
    return classifier.classify(extract_features(name))
def main():
    train_set, test_set = load_and_preprocess_data()
    classifier = train_classifier(train_set)
    accuracy_percentage = accuracy(classifier, [(extract_features(name), gender) for (name, gender) in test_set])
    print(f"Classifier Accuracy: {accuracy_percentage * 100:.2f}%")
    input_name = input("Enter a name: ")

    classification = classifier.classify(extract_features(input_name))

    print(f"The name '{input_name}' is predicted to be '{classification}'.")

    while True:
        input_name = input("Enter a name: ")

        classification = classify_name(classifier, input_name)

        print(f"The name '{input_name}' is predicted to be '{classification}'.")

        user_input = input("Do you want to continue? (yes/no): ").lower()

        if user_input != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
