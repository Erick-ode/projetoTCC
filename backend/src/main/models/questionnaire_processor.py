import random
from backend.src.main.utils.settings import ANTECEDENTS_DATA
from typing import Dict, List


class QuestionnaireProcessor:
    def __init__(self, response):
        self.data = response.get('attributes', {})

        self.time = self.data.get('time', [])
        self.cost = self.data.get('cost', [])
        self.responsible = self.data.get('responsible', [])
        self.explanation = self.data.get('explanation', [])
        self.reliability = self.data.get('reliability', [])
        self.parametrization = self.data.get('parametrization', [])
        self.productivity = self.data.get('productivity', [])

        self.input_values = {}
        self.process_time()
        self.process_cost()
        self.process_responsible()
        self.process_explanation()

    def process_time(self):
        answer = self.time[0].get('answer', '')
        if 1 <= float(answer) <= 5:
            self.input_values['time'] = 2.5
        else:
            self.input_values['time'] = 8.0

    def process_cost(self):
        answer = self.cost[0].get('answer', '')

        pairs = answer.split(';')
        people_in_team = {}
        for pair in pairs:
            name, value = pair.split(':')
            people_in_team[name] = int(value)

        count_members = sum(people_in_team.values())

        percents = {}
        for position, qtd in people_in_team.items():
            percent = (qtd / count_members) * 100
            percents[position] = percent

        if percents['Sênior'] >= sum([percents['Pleno'], percents['Junior']]):
            self.input_values['cost'] = 180.00
        elif percents['Pleno'] >= sum([percents['Pleno'], percents['Junior']]):
            self.input_values['cost'] = 111.67
        else:
            self.input_values['cost'] = 40.00

    def process_responsible(self):
        answer_about_many_people = int(self.responsible[0].get('answer', ''))
        answer_about_one_person = self.responsible[1].get('answer', '')

        if answer_about_many_people == 1:
            self.input_values['responsible'] = 23.99
        elif answer_about_many_people > 1 and answer_about_one_person.lower == 'não':
            self.input_values['responsible'] = 14.68
        else:
            self.input_values['responsible'] = 4.5

    def process_explanation(self):
        answer_about_framework = self.explanation[0].get('answer', '')
        answer_about_client = float(self.explanation[1].get('answer', ''))

        first_value = 0
        if 'ferramenta automatizada' in answer_about_framework.lower:
            first_value = 5.5
        elif 'papel' in answer_about_framework.lower or 'diagrama' in answer_about_framework.lower:
            first_value = 16
        else:
            first_value = 36.75

        second_value = 0
        if answer_about_client <= 5.5:
            second_value = 5.5
        elif 5.51 <= answer_about_client <= 16.1:
            second_value = 16
        else:
            second_value = 36.75

        self.input_values['explanation'] = (first_value + second_value) / 2

    def process_reliability(self):
        pass