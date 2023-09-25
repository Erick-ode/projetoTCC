import unittest
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure
from backend.src.main.utils.settings import ANTECEDENTS_DATA, SENTENCES


class TestFuzzySimulation(unittest.TestCase):
    def setUp(self) -> None:
        self.fuzzy_simulation = FuzzySimulation(12.795258311882149, 175.8650745039662, 14.92867659725409,
                                                47.456611622484715, 126.49172709989107, 1.446144933550861,
                                                66.4520288668543)
        self.fuzzy_structure = FuzzyStructure()

    def test_fuzzy_simulation_result_from_calculate_inputs(self):
        technic = self.fuzzy_simulation.calculate_fuzzy(self.fuzzy_structure.rules)[0]

        self.assertEqual(technic, 'jad')

    def test_fuzzy_simulation_inputs_return_rule(self):
        fs = self.fuzzy_simulation
        time = fs.time
        cost = fs.cost
        responsible = fs.responsible

        time_term = fs.find_result(ANTECEDENTS_DATA[0], time)
        cost_term = fs.find_result(ANTECEDENTS_DATA[1], cost)
        responsible_term = fs.find_result(ANTECEDENTS_DATA[2], responsible)
        term_expected = SENTENCES['jad'][0:3]

        self.assertEqual([time_term, cost_term, responsible_term], term_expected)


if __name__ == '__main__':
    unittest.main()
