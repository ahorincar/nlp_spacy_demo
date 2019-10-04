import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from draw_words import DrawWords
from analyzer import Analyzer

if __name__ == '__main__':
    import sys
    url_string = input('Gimme a URL!\n')

    # Make request to retrieve the article.
    request = requests.get(url = url_string)
    soup = BeautifulSoup(request.text, features='html.parser')

    # Get all the text in between <p></p> tags.
    paragraphs = [p_tag.text for p_tag in soup.findAll('p')]

    # Do the NLP magic :D.
    analyzer = Analyzer(paragraphs)
    word_1, word_2, word_3 = analyzer.getRelevantWords()

    app = QtWidgets.QApplication(sys.argv)
    window = DrawWords(word_1, word_2, word_3)
    window.show()
    sys.exit(app.exec_())
