from backend.src.main.utils.support import set_terms_to_dictionary, create_clause, create_multiple_rules
from backend.src.main.utils.settings import CONSEQUENT, ANTECEDENTS_NAMES, LIMITS, DF_TERMS, SENTENCES


class FuzzyStructure:

    def __init__(self):
        self._antecedents = []
        self.set_antecedents()

        self._consequent = CONSEQUENT

        self._rules = None
        self.set_rules()

    @property
    def antecedents(self):
        return self._antecedents

    @property
    def consequent(self):
        return self._consequent

    @property
    def rules(self):
        return self._rules

    def set_antecedents(self):
        for antecedent_name, limit in zip(ANTECEDENTS_NAMES, LIMITS):
            dictionary = set_terms_to_dictionary(DF_TERMS, antecedent_name)
            antecedent = create_clause((0, limit), antecedent_name, dictionary)
            self._antecedents.append(antecedent)

    def set_rules(self):
        self._rules = create_multiple_rules(self._antecedents, SENTENCES, self._consequent)
