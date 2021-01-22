import os
from os import path
from pathlib import Path
# to generate wordcloud from text file
from wordcloud import WordCloud
# the matplotlib way:
import matplotlib.pyplot as plt
import datetime
# para garantir o request https do notebook da máquina cliente
import ssl
# importa a biblioteca natural language took kit
import nltk

# Directory and File manipulation
def deleteFileIfExist(path):
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file {} does not exist".format(path))

# Directory and File manipulation
def createNewEmptyFile(path):
    Path(path).touch()
    print('The file {} was created with sucess!'.format(path))

# String content manipulation
def removeTerminationCharacters(content):
    content = " ".join(str(content).split())
    return content

# String content manipulation
def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha(): 
            lista_palavras.append(token)
    return lista_palavras

# String content manipulation
def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

# File manipulation and DataFrame content
def appendContentsInTextFile(path_text_file, series_content):
    deleteFileIfExist(path_text_file)
    createNewEmptyFile(path_text_file)

    with open(path_text_file, 'a', encoding='utf-8') as my_file_contents:
        for content in list(series_content):
            if (content is not None) and (content != 'NaN') and (content != 'nan'):
                content = removeTerminationCharacters(content)
                my_file_contents.write(content)
    print('The {} has appended all abstract content with sucess!'.format(path_text_file))

# WordCloud manipulation
def generateWordcloudFromTextFile(path_text_file, file_name):
    # Read the whole text.
    text_content = open(path_text_file, encoding='utf-8').read()
    # Generate a word cloud image
    wordcloud = WordCloud(width = 1920, height = 1080, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(text_content)
    # Display the generated image:
    #wordcloud.generate_from_frequencies(frequencies=dictionaryOfFileFrequence)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    # Save the image in the img folder:
    path_images = "/Users/armandosoaressousa/git/tdmls/sms/images"
    file_Name_to_store = path_images + "/" + file_name + ".png"
    wordcloud.to_file(file_Name_to_store)

# NLP (Natural Language Processing)
def contentAnalysisFromTextFile(path_text_file, sizeWord=3):
    text_content = open(path_text_file, encoding='utf-8').read()
    print('Gera lista de tokens.')
    print('Faz a tokenizacao do conteudo artigos.')
    lista_tokens = nltk.tokenize.word_tokenize(text_content)

    print('Gera lista de palavras')
    lista_palavras = separa_palavras(lista_tokens)

    print('Normaliza todas as palavras para minusculas.')
    lista_normalizada = normalizacao(lista_palavras)

    print('Gera o conjunto de palavras unicas - vocabulario.')
    vocabulario = set(lista_normalizada)

    print('Calcula a frequencia da lista de palavras')
    frequencia = nltk.FreqDist(lista_normalizada)
    total_palavras = len(lista_normalizada)
    frequencia.most_common(100)
    print("Frequencia de palavras (mais de {} caracteres)".format(sizeWord))
    for each in frequencia.most_common(100):
        if len(each[0]) >= sizeWord:
            print(each)
    print(f"Número total de palavras é {len(lista_palavras)}")
    print(f"Número de palavras únicas é {len(vocabulario)}")

# NLP (Natural Language Processing)
def loadSupportTokenization():
    # cria um contexto para chamadas do request https do notebook da máquina cliente
    ssl._create_default_https_context = ssl._create_unverified_context

    print('Starting download punkt to suport tokeninzing...')
    # Punkt Sentence Tokenizer
    # This tokenizer divides a text into a list of sentences by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences.
    nltk.download('punkt')
    print('Download concluído.')
    print('Unzip concluído.')

def list_of_items(df_data, column_name):
    list_of_contents = []
    for item in list(df_data[column_name]):
        item = item.split(',')
        for subitem in item:
            subitem = ' '.join(subitem.split())
            list_of_contents.append(subitem)
    set_of_contents = set(list_of_contents)
    list_of_uniques_contents = list(set_of_contents)
    print("List of all {} {} : {}".format(len(list_of_contents), column_name, list_of_contents))
    print("")
    print("List of unique {} {} : {}".format( len(list_of_uniques_contents) , column_name, list_of_uniques_contents))
    return list_of_contents, list_of_uniques_contents

def show_bar_plot(group, count, subtitle, x_label=None, y_label=None):
    plt.bar(group,count)
    plt.title(subtitle)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def show_bar_plot_complete(my_dictionary, subtitle, x_label=None, y_label=None):
    group = []
    count = []
    for key, value in my_dictionary.items():
        group.append(key)
        count.append(value)
    show_bar_plot(group, count, subtitle, x_label, y_label)