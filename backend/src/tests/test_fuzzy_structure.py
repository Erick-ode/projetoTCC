import unittest
from ..main.models.fuzzy_structure import FuzzyStructure
from ..main.utils.support import ctrl


class TestFuzzyStructure(unittest.TestCase):
    def setUp(self) -> None:
        self.fuzzy_structure = FuzzyStructure()

    def test_consequent_setter_returns_consequent_type(self):
        self.assertIsInstance(self.fuzzy_structure.consequent, ctrl.Consequent)

    def test_set_antecedents_returns_antecedents_type(self):
        print(self.fuzzy_structure.antecedents)
        for antecedent in self.fuzzy_structure.antecedents:
            self.assertIsInstance(antecedent, ctrl.Antecedent)

    def test_set_rules_returns_rule_type(self):
        for rule in self.fuzzy_structure.rules:
            self.assertIsInstance(rule, ctrl.Rule)

    def test_antecedents_names(self):
        self.assertEqual(self.fuzzy_structure.antecedents[1].label, 'custo')


if __name__ == '__main__':
    unittest.main()
