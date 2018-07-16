
from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['Fulltext']

    word_list = fulltext.split()

    wordcount_dict = {

    }

    for word in word_list:
        if word in wordcount_dict:
            wordcount_dict[word] += 1
        else:
            wordcount_dict[word] = 1

    sorted_words = sorted(wordcount_dict.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    return render(request, 'count.html', {
        'fulltext': fulltext,
        'count_words': len(word_list),
        'sorted_words': sorted_words,

    })