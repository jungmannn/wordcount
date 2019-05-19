from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    full_text = request.GET['fulltext']
    
    word_list = full_text.split()
    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sortedArr = sorted(word_dictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'result.html', {'fulltext':full_text, 'total' : len(word_list), 'dictionary': sortedArr, 'first' : sortedArr[0][1]})
# Create your views here.
