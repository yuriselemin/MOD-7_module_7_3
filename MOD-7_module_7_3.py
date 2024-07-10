import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        words = []
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower().strip()
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words.extend(line.split())
                    all_words[file_name] = words

        return all_words


    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}  # Индексация начинается с 1

        return None


    def count(self, word):
        counts = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                counts[name] = words.count(word)

        return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
