from skfuzzy import control as ctrl
from typing import List
from ..utils.settings import CONSEQUENT_DATA
from ..utils.support import find_result
from .rule_validator import RuleValidator


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
        self.parameters = [time, cost, responsible, explanation, reliability, parameterization, productivity]
        self.rule_validator = RuleValidator(self.parameters)
        self.coherence = 0

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

        try:
            simulator.compute()
            self.coherence = 100
        except ValueError:
            self.rule_validator.reset_inputs(simulator)
            self.coherence = self.rule_validator.coherence
            simulator.compute()

        return find_result(CONSEQUENT_DATA, simulator.output['tecnica']), self.coherence
