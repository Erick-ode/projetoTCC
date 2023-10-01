from flask import request, jsonify
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor
from backend.src.main.models.technic import Technic
from app import create_app, db


main = create_app()


@main.route('/')
def hello_world():
    return 'Hello world'


@main.route('/processar_respostas', methods=['POST'])
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

    results = fuzzy_simulator.calculate_fuzzy(fuzzy_structure.rules)
    technic_result = results[0]
    coherence = results[1]

    new_register = Technic(name=technic_result, coherence=coherence)

    db.session.add(new_register)
    db.session.commit()

    return jsonify({'technic_result': technic_result})


@main.route('/retornar_tecnica', methods=['GET'])
def get_technic():
    result = Technic.query.all()

    return f'Resultado: {result}'


if __name__ == '__main__':

    main.run(debug=True)



