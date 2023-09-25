from skfuzzy import control as ctrl
from typing import List, Dict
from backend.src.main.utils.settings import CONSEQUENT_DATA, ANTECEDENTS_DATA


class FuzzySimulation:
    def __init__(self, time: float, cost: float, responsible: float, explanation: float, reliability: float,
                 parameterization: float, productivity: float):
        self.time = time
        self.cost = cost
        self.responsible = responsible
        self.explanation = explanation
        self.reliability = reliability
        self.parameterization = parameterization
        self.productivity = productivity

    def calculate_fuzzy(self, rules: List[ctrl.Rule]):
        control = ctrl.ControlSystem(rules=rules)
        simulator = ctrl.ControlSystemSimulation(control)

        simulator.input['tempo'] = self.time
        simulator.input['custo'] = self.cost
        simulator.input['pessoas'] = self.responsible
        simulator.input['imposicao'] = self.explanation
        simulator.input['confiabilidade'] = self.reliability
        simulator.input['padronizacao'] = self.parameterization
        simulator.input['produtividade'] = self.productivity

        simulator.compute()

        return self.find_result(CONSEQUENT_DATA, simulator.output['tecnica'])

    def validate_rule(self, value):
        pass

    @staticmethod
    def find_result(items: Dict[str, List[float]], value: float) -> str:
        for key, values in items.items():
            if min(values) <= value <= max(values):
                return key
