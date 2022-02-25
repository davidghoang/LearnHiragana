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
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    "さ": "sa",
    "し": "si",
    "す": "su",
    "せ": "se",
    "そ": "so",
    "た": "ta",
    "ち": "ti",
    "つ": "tu",
    "て": "te",
    "と": "to",
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    "は": "ha",
    "ひ": "hi",
    "ふ": "hu",
    "へ": "he",
    "ほ": "ho",
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",
    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",
    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",
    "わ": "wa",
    "ゐ": "wi",
    "ゑ": "we",
    "を": "wo"
}


def hiragana(request):
    character, _ = random.choice(list(hiragana_table.items()))
    return redirect('/hiragana/' + character)


def quiz_character(request, character):
    template = loader.get_template('website/hiragana/quiz_character.html')

    correct_option = hiragana_table[character]

    hiragana_table_without_answer = []
    for key in hiragana_table:
        if key != character:
            hiragana_table_without_answer.append(hiragana_table[key])

    # hiragana_table_without_answer = {key: hiragana_table[key] for key in hiragana_table if key != character}
    options = random.sample(hiragana_table_without_answer, 3)
    options.insert(random.randint(0, len(options)), correct_option)

    context = {
        'character': character,
        'options': options,
    }
    return HttpResponse(template.render(context, request))


def check_answer(request, character, submission):
    # show a new page with my results + have a link to the /hiragana/
    template = loader.get_template('website/hiragana/quiz_result.html')

    if hiragana_table[character] == submission:
        result = "You are correct!"
    else:
        result = "You are wrong."

    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))



