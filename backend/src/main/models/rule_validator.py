from ..utils.settings import ANTECEDENTS_NAMES, ANTECEDENTS_DATA, SENTENCES
from ..utils.support import find_result
import numpy as np


class RuleValidator:
    def __init__(self, parameters):
        self.parameters = parameters

        self.actual_results = []
        self.set_actual_results()

        self.closest_results = []
        self.set_closest_results()

        self.coherence = 0
        self.set_coherence(self.closest_results)

    def set_actual_results(self):
        for name, p in zip(ANTECEDENTS_DATA, self.parameters):
            self.actual_results.append(find_result(name, p))

    def set_closest_results(self):
        for rule in SENTENCES.values():
            list_aux = self.define_possible_values(rule, self.actual_results)

            if self.compare_filled_values(list_aux, self.closest_results):
                self.closest_results = list_aux

    def validate_results(self, expected_results):
        empty_indexes = self.find_empty_indexes(expected_results)
        filled_indexes = self.find_filled_indexes(expected_results)

        for rule in SENTENCES.values():
            value_is_correct = []
            for index in filled_indexes:
                if expected_results[index] == rule[index]:
                    value_is_correct.append(True)
            if len(value_is_correct) == len(filled_indexes):
                return {'empty_index': empty_indexes, 'filled_index': filled_indexes, 'rule': rule}

    def reset_inputs(self, simulator):
        values_to_change = self.validate_results(self.closest_results)
        indexes = values_to_change['empty_index']
        true_rule = values_to_change['rule']
        for i in indexes:
            term = true_rule[i]
            mean = np.mean(ANTECEDENTS_DATA[i][term])
            name_parameter = ANTECEDENTS_NAMES[i]
            simulator.input[name_parameter] = mean

    def set_coherence(self, expected_results):
        filled_indexes_count = self.count_values_filled(expected_results)
        total = len(expected_results)
        self.coherence = filled_indexes_count / total * 100

    @staticmethod
    def find_empty_indexes(_list):
        return [index for index, value in enumerate(_list) if value is None]

    @staticmethod
    def find_filled_indexes(_list):
        return [index for index, value in enumerate(_list) if value is not None]

    @staticmethod
    def count_values_filled(_list):
        return sum(1 for valor in _list if valor is not None)

    def compare_filled_values(self, actual_values, expected_values):
        sum_values_filled_act = self.count_values_filled(actual_values)
        sum_values_filled_exp = self.count_values_filled(expected_values)

        return sum_values_filled_act >= sum_values_filled_exp

    @staticmethod
    def define_possible_values(expected_values, actual_values):
        list_aux = []
        for term, result in zip(expected_values, actual_values):
            if term == result:
                list_aux.append(result)
            else:
                list_aux.append(None)
        return list_aux
