import enchant
def spellcheck(word):
    d = enchant.Dict("en_US")
    if d.check(word):
      print(f"{word} is a real word.")
    else:
      print(f"{word} is not in the dictionary.")
spellcheck("hello")
