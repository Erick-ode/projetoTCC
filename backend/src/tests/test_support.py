import unittest
from ..main.utils.settings import DF_TERMS, DF_RULES
from ..main.utils.support import *


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.terms = DF_TERMS
        self.rules = DF_RULES

        self.dict_terms = {'termo1': [0, 2, 4], 'termo2': [3, 5, 7, 9]}
        self.dict_consequent_terms = {'resultado1': [0, 2, 4], 'resultado2': [3, 5, 7, 9]}
        self.range_values = (0, 10)

        self.antecedent_1 = create_clause(self.range_values, 'antecedente1', self.dict_terms)
        self.antecedent_2 = create_clause(self.range_values, 'antecedente2', self.dict_terms)

        self.consequent = create_clause(self.range_values, 'consequente', self.dict_consequent_terms, 1)

        self.results = {'resultado1': ['termo1', 'termo2'], 'resultado2': ['termo2', 'termo1']}

    def test_create_clause_with_right_type_right_label(self):
        self.assertEqual(self.antecedent_2.label, 'antecedente2')
        self.assertIsInstance(self.antecedent_2, ctrl.Antecedent)

    def test_split_antecedents_names(self):
        names = split_antecedents_names(self.terms)

        self.assertTrue(len(names) == 7)

    def test_create_rule(self):
        antecedent_one = self.antecedent_1
        antecedent_two = self.antecedent_2

        consequent = self.consequent

        activating_terms = [antecedent_one['termo1'], antecedent_two['termo2']]
        rule = create_rule(activating_terms, consequent['resultado1'])

        self.assertIsNotNone(rule)
        self.assertIsInstance(rule, ctrl.Rule)

        self.assertEqual(rule.antecedent_terms, activating_terms)

    def test_create_multiple_rules(self):
        rules = create_multiple_rules([self.antecedent_1, self.antecedent_2], self.results, self.consequent)

        self.assertIsNotNone(rules)

        for rule in rules:
            self.assertIsInstance(rule, ctrl.Rule)

    def test_set_sentences(self):
        sentences = set_sentences(DF_RULES)

        self.assertIsNotNone(sentences)

    def test_find_value(self):
        dict_items = set_terms_to_dictionary(DF_TERMS, 'tecnica')
        value = find_result(dict_items, 98)

        self.assertEqual(value, 'questionarios')


if __name__ == '__main__':
    unittest.main()
