# word_entry.py -- Raul Matthew Mosley, 2026
#
# A class for a word definition

class WordEntry:
    def __init__(self, word, definitions, pos, occurrences):
        self._word = word
        self._defs = definitions
        self._occurs = occurrences

        # Part of speech
        self._pos = pos

    def get_word(self):
        return self._word

    def get_defs(self):
        return self._def

    def get_occurs(self):
        return self._occurs

    def get_pos(self):
        return self._pos

    word = property(fget=get_word)
    definition = property(fget=get_defs)
    occurrences = property(fget=get_occurs)
    pos = property(fget=get_pos)

    def __str__(self):
        return f'{self._word}: [{self._pos}] x{self._occurs} {"; ".join(self._defs)}'
