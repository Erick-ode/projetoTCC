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

        if answer == 'Maioria Sênior' or answer == 'Mais sêniors e plenos do que juniors':
            self.input_values['cost'] = 180.00
        elif (answer == 'Maioria Plenos' or answer == 'Mesma quantidade em todos os níveis'
              or 'Mais sêniors e juniors do que plenos'):
            self.input_values['cost'] = 111.67
        elif answer == 'Maioria Juniors' or answer == 'Mais plenos e juniors do que sêniors':
            self.input_values['cost'] = 40.00

    def process_responsible(self):
        answer_about_many_people = int(self.responsible[0].get('answer', ''))
        answer_about_one_person = self.responsible[1].get('answer', '')

        if answer_about_many_people == 1:
            self.input_values['responsible'] = 23.99
        elif answer_about_many_people > 1 and str(answer_about_one_person).lower == 'não':
            self.input_values['responsible'] = 14.68
        else:
            self.input_values['responsible'] = 4.5

    def process_explanation(self):
        answer_about_framework = self.explanation[0].get('answer', '')
        answer_about_client = float(self.explanation[1].get('answer', ''))

        value = 0
        if (answer_about_framework == 'Ferramenta automatizada' or answer_about_framework == 'Observação') and answer_about_client <= 5.5:
            value = 5.5
        elif answer_about_framework == 'Conversas' and (5.51 <= answer_about_client <= 16.1):
            value = 16
        else:
            value = 36.75

        self.input_values['explanation'] = value

    def process_reliability(self):
        answer_about_level = self.reliability[0].get('answer', '')
        answer_about_trusting = self.reliability[1].get('answer', '')

        reliability_mapping = {
            'Sênior_Muita_confiança': 'high',
            'Sênior_Confio_parcialmente': 'high',
            'Pleno_Muita_confiança': 'high',
            'Sênior_Não_confio': 'medium',
            'Pleno_Confio_parcialmente': 'medium',
            'Junior_Muita_confiança': 'medium',
            'Pleno_Não_confio': 'low',
            'Junior_Confio_parcialmente': 'low',
            'Junior_Não_confio': 'low'
        }
        user_answer_key = f'{answer_about_level}_{str(answer_about_trusting).replace(" ", "_")}'
        
        if user_answer_key in reliability_mapping:
            reliability = reliability_mapping[user_answer_key]
        else:
            reliability = None

        values = {'high': 92.14, 'medium': 45.00, 'low': 15.31}
        self.input_values['reliability'] = values[reliability]

    def process_parametrization(self):
        answer = self.parametrization[0].get('answer', '')

        if answer == 'Métodos padronizados':
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
