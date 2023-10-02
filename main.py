from flask import request, jsonify
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor
from backend.src.main.models.technic import Technic
from app import create_app, db
import os

main = create_app()


@main.route('/carregar_perguntas')
def load_questions():
    file_path = os.path.abspath('backend/src/main/questions/questions.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        questions = []
        for line in lines:
            parts = line.strip().split(';')
            question = {
                'id': parts[0],
                'question': parts[1],
                'parameter': parts[2],
                'type': parts[3],
                'options': parts[4:]
            }
            questions.append(question)
        return jsonify(questions)


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
def get_all_technics():
    results = Technic.query.all()

    technic_list = [{"id": result.id, "name": result.name, "coherence": result.coherence} for result in results]

    return jsonify(technic_list)


@main.route('/apagar_registro/<int:id>', methods=['DELETE'])
def delete_register(id):
    register = Technic.query.get(id)

    if register:
        db.session.delete(register)
        db.session.commit()
        return jsonify({'message': f'Registro com ID {id} apagado com sucesso'}), 200
    else:
        return jsonify({'error': f'Registro com ID {id} não encontrado'}), 404


@main.route('/retornar_tecnica/<int:id>', methods=['GET'])
def get_technic(id):
    result = Technic.query.order_by(Technic.id.desc()).first()

    return jsonify({'Técnica': result.name, 'Coerência': result.coherence})


if __name__ == '__main__':
    main.run(debug=True)
