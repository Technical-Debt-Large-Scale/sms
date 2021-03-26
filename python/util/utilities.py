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
import seaborn as sns
import pandas as pd
import math
from collections import Counter
from tabulate import tabulate

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

 # WordCloud manipulation
def generateWordcloudFromFrequencies(my_frequence, file_name):
    # Generate a word cloud image
    wordcloud = WordCloud(width = 1920, height = 1080, random_state=1, background_color='black', colormap='Set2', 
        collocations=False).generate_from_frequencies(my_frequence)
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
    list_of_contents.sort()
    list_of_uniques_contents.sort()
    print("List of all {} {} : {}".format(len(list_of_contents), column_name, list_of_contents))
    print("")
    print("List of unique {} {} : {}".format( len(list_of_uniques_contents) , column_name, list_of_uniques_contents))
    return list_of_contents, list_of_uniques_contents

def show_bar_plot(group, count, subtitle, x_label=None, y_label=None):
    ax = plt.bar(group,count)
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

def show_histogram(df_data, title, bins):
    ax = sns.distplot(df_data, bins=bins, kde=False)
    ax.set(title=title)
    # label each bar in histogram
    for p in ax.patches:
        height = p.get_height() # get the height of each bar
        # adding text to each bar
        ax.text(x = p.get_x()+(p.get_width()/2), y = height+0.2, s = '{:.0f}'.format(height), ha = 'center')

def convert_lists_in_dataframe(group, count):
    my_dict = {}
    my_dict['x'] = group
    my_dict['y'] = count
    my_df = pd.DataFrame.from_dict(my_dict)
    return my_df

def show_bar_plot_temp(group, count, subtitle, x, y):
    # plot vertical barplot
    sns.set(rc={'figure.figsize':(10,5)})
    df_data = convert_lists_in_dataframe(group, count)
    ax = sns.barplot(x=x, y=y, data=df_data)
    ax.set(title=subtitle) # title barplot
    # label each bar in barplot
    for p in ax.patches:
        # get the height of each bar
        height = p.get_height()
        # adding text to each bar
        ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
        y = height+100, # y-coordinate position of data label, padded 100 above bar
        s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
        ha = 'center') # sets horizontal alignment (ha) to center

def clean_related_work(df_data, column_name):
    list_of_related_work = []
    for item in list(df_data[column_name]): 
        item = str(item)
        item = ' '.join(item.split())
        list_of_related_work.append(item)

    list_of_related_work_sorted = []
    for each in list_of_related_work:
        each = each.split('#')
        for each_one in each:
            each_one = each_one.split(';')
            if (len(each_one) > 1):
                if each_one[1][0] == ' ':
                    each_one[1] = each_one[1][1:]
                each_one[1] = each_one[1].replace('.', '')
                each_one[1] = each_one[1].replace(',', '')
                each_one[1] = each_one[1].replace('“', '')
                each_one[1] = each_one[1].replace('”', '')
                list_of_related_work_sorted.append(each_one[1])
    list_of_related_work_sorted.sort()
    return list_of_related_work_sorted

def remove_cotation_space1(my_list):
    list_temp = []
    if (len(my_list) > 1):
        for each in my_list:
            each = each.replace('"', '')
            if each[0] == ' ':
                each = each[1:]
            if each[-1] == ' ':
                each = each[:-1]
            list_temp.append(each)
        return list_temp
    else:
        return my_list

def extract_techniques_approuches_tools(df_data, column_name='Techniques, approach and methods (parsed)'):
    list_of_techniques = []
    list_of_approaches = []
    list_of_tools = []
    list_of_tat = []

    for item in list(df_data[column_name]): 
        item = str(item)
        item = ' '.join(item.split())
        list_of_tat.append(item)
    for each in list_of_tat:
        each = each.split('#')
        general = each[0].replace('general:', '') 
        general = general.split(',')
        general = remove_cotation_space1(general)
        for one in general:
            list_of_techniques.append(one)   
        if (len(each) == 3):  
            approuch = each[1].replace('approuch:', '')
            approuch = approuch.split(',')
            approuch = remove_cotation_space1(approuch)
            for one in approuch:
                list_of_approaches.append(one)
            tools = each[2].replace('tools:', '')
            tools = tools.split(',')
            tools = remove_cotation_space1(tools)
            for one in tools:
                list_of_tools.append(one)
    return list_of_tat, list_of_techniques, list_of_approaches, list_of_tools


def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False

def create_latex_table(my_df, my_path, my_file_name):
    file_path = my_path + '/' + my_file_name
    try:
        with open(file_path,'w', encoding='utf-8') as my_file:
            my_file.write(my_df.to_latex(index=False))
        print("Arquivo " + file_path + "  gerado com sucesso!")
    except Exception as e:
        print("Erro " + str(e)+ " ao tentar gerar o arquivo latex! " + file_path)

def create_markdown_table(my_df, my_path, my_file_name):
    file_path = my_path + '/' + my_file_name
    try:
        with open(file_path,'w', encoding='utf-8') as my_file:
            my_file.write( tabulate(my_df, tablefmt="pipe", headers="keys",  ) )
        print("Arquivo " + file_path + "  gerado com sucesso!")
    except Exception as e:
        print("Erro " + str(e)+ " ao tentar gerar o arquivo markdown! " + file_path)

def view_question_distribution(my_dict, my_list, my_question):
    list_q_is_nan = []
    list_q_is_no = []
    list_q_feature = []
    for key, value in my_dict.items():
        if isnan(value):
            list_q_is_nan.append((key, value))
        if (value == 'no'):
            list_q_is_no.append((key, value))
        if ( not isnan(value) and (value != 'no') ):
            list_q_feature.append((key, value))

    list_of_most_common_q = []
    list_of_most_common_q.append(len(list_q_feature))
    list_of_most_common_q.append(len(list_q_is_no))
    list_of_most_common_q.append(len(list_q_is_nan))

    q = my_list
    count_q = list_of_most_common_q
    my_q = {my_question: q, 'count':count_q}
    my_q

    my_q_id = list(range(1,len(list_of_most_common_q)+1))
    my_q_id

    df_my_q = pd.DataFrame(data=my_q, index=my_q_id)
    df_my_q.reset_index(drop=True, inplace=True)
    return df_my_q

def view_question_distribution_update_sp(my_df_distribution, my_df_data, my_feature):
    i = 0
    for each in my_df_distribution:
        list_q_is_nan = []
        list_q_is_no = []
        list_q_feature = []
        j = 0
        for item in my_df_data[my_feature]:
            value = item
            if isnan(value):
                list_q_is_nan.append(my_df_data['sp'].iloc[j])
            if (str(value).lower() == 'no'):
                list_q_is_no.append(my_df_data['sp'].iloc[j])
            if ( not isnan(value) and (str(value).lower() != 'no') ):
                list_q_feature.append(my_df_data['sp'].iloc[j])
            j = j + 1
        i = i + 1
    my_df_distribution['sp'].iloc[0] = list_q_feature
    my_df_distribution['sp'].iloc[1] = list_q_is_no
    my_df_distribution['sp'].iloc[2] = list_q_is_nan

    return my_df_distribution

# 1) Dataset
def load_dataset(my_path='../../dataset/Extraction_form_basic.xlsx'):
    df_sms_extraction = pd.read_excel(my_path)
    pd.set_option('display.max_colwidth',255)
    return df_sms_extraction

# Adding new column sp (Selected Paper)
def add_column_sp(df_sms_extraction):
    df_sms_extraction['SP Index'] = df_sms_extraction.index+1
    df_sms_extraction['SP Aux'] = 'SP' 
    df_sms_extraction['sp'] = [y + str(x) for x, y in zip(df_sms_extraction['SP Index'], df_sms_extraction['SP Aux'])]
    return df_sms_extraction

# 2) Selected papers
def selected_papers(df_sms_extraction):
    df_my_data_papers = df_sms_extraction[['sp', 'Citation', 'Title']]
    return df_my_data_papers

def remove_enter(my_df):
    my_df = ' '.join(my_df.split())
    return my_df