def sentence_maker(phrase):
    interrogatives = ("how", "why", "what", "where", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Enter Sentence: ")
    if user_input == "/end":
        break
    else:
        results.append(sentence_maker(user_input))

print("Formatted Sentence:", " ".join(results))
