"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
)

story_2 = Story(
    ["exclamation", "adverb", "noun", "adjective"],
    "{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife."
)

story_3 = Story([
    "plural_noun", "adjective", "plural_animal", "plural_noun1", "adjective1", "color", "adjective2", "noun",
    "plural_noun2", "adjective3", "verb", "plural_noun3", "verb_ed", "verb1", "noun1", "adjective4"
    ], """Unicorns aren't like other {plural_noun}; they're {adjective}. They look like {plural_animal}, 
    with {plural_noun1} for feet and a {adjective1} mane of hair. But unicorns are {color} and have a {adjective2} {noun} 
    on their heads. Some {plural_noun2} don't believe unicorns are {adjective3} but I believe in them.  I would love to
    {verb} a unicorn to faraway {plural_noun3}. One thing I've always {verb_ed} about is whether unicorns {verb1} rainbows, 
    or is their {noun1} {adjective4} like any other animal's?"""
)


story_list = [story, story_2, story_3]





ans = {"verb": "eat", "noun": "mango", "place": "universe", "adjective": "luscious", "plural_noun": "other mangoes" }
ans_2 = {"exclamation": "Ouch", "adverb": "accidentaly", "noun": "car", "adjective": "beautiful"}
ans_3 = {"plural_noun": "fairies", "adjective": "blue", "plural_animal": "horses", "plural_noun1": "carrots", "adjective1": "small",
        "color": "brown", "adjective2": "huge", "noun": "bread", "plural_noun2": "dumps", "adjective3": "pink", "verb": "fart",
        "plural_noun3": "patatoes", "verb_ed": "pooped", "verb1": "dump", "noun1": "toilet", "adjective4": "shine"}
print(ans_2)
print(story_2.generate(ans_2))
print(story_3.generate(ans_3))
print (story_list)