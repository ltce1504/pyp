def print_words_of_length(file_path, word_length):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            text = file.read()

        words = text.split()

        words_of_length = [word for word in words if len(word) == word_length]

        if words_of_length:
            print(f"Words with {word_length} letters: ")
            for word in words_of_length:
                print(word)
        else:
            print(f"No words of length {word_length} found.")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occured : {e}")

file_path = "sample.txt"
word_length = 4
print_words_of_length(file_path, word_length)