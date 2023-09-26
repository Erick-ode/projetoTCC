class QuestionnaireProcessor:
    def __init__(self, response):
        self.data = response

        self.time = self.data.get('time', None)
        self.cost = self.data.get('cost', None)
        self.responsible = self.data.get('responsible', None)
        self.explanation = self.data.get('explanation', None)
        self.reliability = self.data.get('reliability', None)
        self.parametrization = self.data.get('parametrization', None)
        self.productivity = self.data.get('productivity', None)

        self.input_values = {}
        self.process_time()
        self.process_cost()
        self.process_responsible()
        self.process_explanation()
        self.process_reliability()
        self.process_parametrization()
        self.process_productivity()

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
        if 'ferramenta automatizada' in [answer_about_framework]:
            first_value = 5.5
        elif 'papel' in [answer_about_framework] or 'diagrama' in [answer_about_framework]:
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
        answer_about_level = self.reliability[0].get('answer', '')
        answer_about_trusting = self.reliability[1].get('answer', '')

        reliability_mapping = {
            'senior_all_trust': 'high',
            'senior_partially_trust': 'high',
            'pleno_all_trust': 'high',
            'senior_no_trust': 'medium',
            'pleno_partially_trust': 'medium',
            'junior_all_trust': 'medium',
            'pleno_no_trust': 'low',
            'junior_partially_trust': 'low',
            'junior_no_trust': 'low'
        }
        user_answer_key = f'{answer_about_level}_{answer_about_trusting}'
        if user_answer_key in reliability_mapping:
            reliability = reliability_mapping[user_answer_key]
        else:
            reliability = None

        values = {'high': 92.14, 'medium': 45.00, 'low': 15.31}
        self.input_values['reliability'] = values[reliability]

    def process_parametrization(self):
        answer = self.parametrization[0].get('answer', '')

        if answer == 'Sim':
            self.input_values['parametrization'] = 2.5
        else:
            self.input_values['parametrization'] = 7.5

    def process_productivity(self):
        answer = self.productivity[0].get('answer', '')

        if answer == 'Baixa':
            self.input_values['productivity'] = 15.00
        elif answer == 'Média':
            self.input_values['productivity'] = 45.00
        elif answer == 'Alta':
            self.input_values['productivity'] = 75.00
        else:
            self.input_values['productivity'] = 00.00
