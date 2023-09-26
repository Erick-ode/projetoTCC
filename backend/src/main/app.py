from flask import Flask, request, jsonify, redirect, url_for
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá mundo!'


@app.route('/processar_respostas', methods=['POST'])
def post_answers():
    data = request.get_json()

    questionnaire = QuestionnaireProcessor(data)

    time = questionnaire.input_values['time']
    cost = questionnaire.input_values['cost']
    responsible = questionnaire.input_values['responsible']
    explanation = questionnaire.input_values['explanation']
    reliability = questionnaire.input_values['reliability']
    parametrization = questionnaire.input_values['parametrization']
    productivity = questionnaire.input_values['productivity']
    fuzzy_structure = FuzzyStructure()
    fuzzy_simulator = FuzzySimulation(time, cost, responsible, explanation, reliability, parametrization, productivity)

    technic_result = fuzzy_simulator.calculate_fuzzy(fuzzy_structure.rules)

    return jsonify({'technic_result': technic_result})


@app.route('/retornar_tecnica', methods=['GET'])
def get_technic():
    result = request.args.get('technic_result', '')

    return f'Resultado: {result}'


if __name__ == '__main__':
    app.run(debug=True)
