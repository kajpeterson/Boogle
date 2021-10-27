import enchant
def spellcheck(word):
    pwl = enchant.request_pwl_dict("en")
    if pwl.check(word):
      print(f"{word} is a real word.")
    else:
      print(f"{word} is not in the dictionary.")
spellcheck("hello")
