import unittest
from ..main.models.rule_validator import RuleValidator


class TestRuleValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.rule_validator = RuleValidator([4, 175, 14, 47, 126, 1, 1])

    def test_actual_results_return_right(self):
        results = self.rule_validator.actual_results
        self.assertFalse(results == ['longo', 'alto', 'grupo', 'alto', 'alta', 'sim', 'alta'])

    def test_closest_results_return_right(self):
        results = self.rule_validator.closest_results
        self.assertEqual(results, [None, 'alto', 'grupo', 'alto', 'alta', 'sim', None])

    def test_indexes_and_true_rule_are_right(self):
        close_results = self.rule_validator.closest_results
        results = self.rule_validator.validate_results(close_results)

        self.assertEqual(results['empty_index'], [0, 6])
        self.assertEqual(results['rule'], ['longo', 'alto', 'grupo', 'alto', 'alta', 'sim', 'alta'])
