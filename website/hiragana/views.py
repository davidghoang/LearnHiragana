from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import random
hiragana_table = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka"
}


def hiragana(request):
    character, _ = random.choice(list(hiragana_table.items()))
    return redirect('/hiragana/' + character)


def quiz_character(request, character):
    template = loader.get_template('website/hiragana/quiz_character.html')

    options = hiragana_table.values()

    context = {
        'character': character,
        'options': options,
    }
    return HttpResponse(template.render(context, request))


def check_answer(request, character, submission):
    # show a new page with my results + have a link to the /hiragana/
    template = loader.get_template('website/hiragana/quiz_result.html')

    if hiragana_table[character] == submission:
        result = "You are correct"
    else:
        result = "You are wrong"

    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))

