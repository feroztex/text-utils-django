import string

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def error(request):
    pass


def analyze(request):
    submitted_text = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    task = []

    if removepunc == "on" or uppercase == "on" or newlineremove == "on" or extraspaceremove == "on" or charcount == "on":
        if removepunc == "on":
            task_completed = 'Removed punctuation(s)'
            analyzed_text = ""

            for char in submitted_text:
                if char not in string.punctuation:
                    analyzed_text = analyzed_text + char

            submitted_text = analyzed_text
            task.append(task_completed)

        if uppercase == "on":
            task_completed = 'Changed to UPPERCASE'
            analyzed_text = ""

            for char in submitted_text:
                analyzed_text = submitted_text.upper()

            submitted_text = analyzed_text
            task.append(task_completed)

        if newlineremove == "on":
            task_completed = 'Removed new line(s)'
            analyzed_text = ""

            for char in submitted_text:
                if char != '\n' and char != '\r':
                    analyzed_text = analyzed_text + char

            submitted_text = analyzed_text
            task.append(task_completed)

        if extraspaceremove == "on":
            task_completed = 'Removed extra space(s)'
            analyzed_text = ""

            for index, char in enumerate(submitted_text):
                if not (submitted_text[index] == ' ' and submitted_text[index + 1] == ' '):
                    analyzed_text = analyzed_text + char

            submitted_text = analyzed_text
            task.append(task_completed)

        if charcount == "on":
            task_completed = 'Counted the number of character(s)'
            analyzed_text = ""
            character_count = 0

            for char in submitted_text:
                if char not in string.punctuation and not (char == ' '):
                    analyzed_text = analyzed_text + char

            character_count = str(len(analyzed_text))
            task.append(task_completed)

            params = {'task': task, 'analyzed_text': analyzed_text, 'character_count': character_count}
            return render(request, 'analyze.html', params)

    else:
        return render(request, 'error.html')
