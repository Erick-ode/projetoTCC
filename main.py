from flask import request, jsonify
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor
from backend.src.main.models.models import Result, Person
from app import create_app, db
import os

main = create_app()


@main.route("/carregar_perguntas")
def load_questions():
    file_path = os.path.abspath("backend/src/main/questions/form_questions.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        questions = []
        for line in lines:
            parts = line.strip().split(";")
            question = {
                "id": parts[0],
                "question": parts[1],
                "parameter": parts[2],
                "type": parts[3],
                "options": parts[4:],
            }
            questions.append(question)
        return jsonify(questions)


@main.route("/carregar_perguntas_registro")
def load_user_questions():
    file_path = os.path.abspath("backend/src/main/questions/register_questions.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        questions = []
        for line in lines:
            parts = line.strip().split(";")
            question = {
                "id": parts[0],
                "question": parts[1],
                "parameter": parts[2],
                "type": parts[3],
                "options": parts[4:],
            }
            questions.append(question)
        return jsonify(questions)


@main.route("/registrar_respondente", methods=["POST"])
def post_answerer():
    try:
        data = request.get_json()
        role = data.get("role")[0].get("answer")
        experience = data.get("experience")[0].get("answer")
        chosen_technic = data.get("technic")[0].get("answer")
        user_id = data.get("user_id")
        
        new_person = Person(
            user_id=user_id,
            role=role,
            experience=experience,
            chosen_technic=chosen_technic,
        )

        db.session.add(new_person)
        db.session.commit()

        return jsonify({"message": "Respondente registrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route("/processar_respostas/<int:user_id>", methods=["POST"])
def post_answers(user_id):
    data = request.get_json()

    questionnaire = QuestionnaireProcessor(data)

    time = questionnaire.input_values["time"]
    cost = questionnaire.input_values["cost"]
    responsible = questionnaire.input_values["responsible"]
    explanation = questionnaire.input_values["explanation"]
    reliability = questionnaire.input_values["reliability"]
    parametrization = questionnaire.input_values["parametrization"]
    productivity = questionnaire.input_values["productivity"]
    fuzzy_structure = FuzzyStructure()
    fuzzy_simulator = FuzzySimulation(
        time, cost, responsible, explanation, reliability, parametrization, productivity
    )

    results = fuzzy_simulator.calculate_fuzzy(fuzzy_structure.rules)
    technic_result = results[0]
    confidence_level = results[1]

    new_register = Result(
        name=technic_result, coherence=confidence_level, person_id=user_id, answers=data
    )

    db.session.add(new_register)
    db.session.commit()

    return jsonify({"technic_result": technic_result})


@main.route("/adicionar_feedback/<int:user_id>", methods=["POST"])
def adicionar_feedback(user_id):
    try:
        data = request.get_json()
        feedback = data.get("feedback")
        user = Person.query.filter_by(user_id=user_id).first()

        if user:
            user.feedback = feedback
            db.session.commit()
            return jsonify({"message": "Feedback adicionado com sucesso."}), 200
        else:
            return jsonify({"error": "Usuário não encontrado."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route("/retornar_resultados", methods=["GET"])
def get_all_technics():
    results = Result.query.all()

    technic_list = [
        {
            "id": result.id,
            "name": result.name,
            "confidence_level": result.confidence_level,
            "Pessoa": result.person_id,
            "Respostas": result.answers,
        }
        for result in results
    ]

    return jsonify(technic_list)


@main.route("/retornar_resultados/<int:user_id>", methods=["GET"])
def get_technic(user_id):
    result = Result.query.filter_by(person_id=user_id).first()
    
    response = jsonify(
        {
            "Técnica": result.name,
            "Coerência": result.confidence_level,
            "Respostas": result.answers,
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response


@main.route("/retornar_pessoas", methods=["GET"])
def get_people():
    results = Person.query.all()

    technic_list = [
        {
            "id": result.id,
            "role": result.role,
            "experience": result.experience,
            "chosen_technic": result.chosen_technic,
            "user_id": result.user_id,
        }
        for result in results
    ]

    return jsonify(technic_list)


@main.route("/retornar_pessoas/<int:user_id>", methods=["GET"])
def get_person(user_id):
    result = Person.query.filter_by(user_id=user_id).first()

    if result:
        return jsonify(
            {
                "Cargo": result.role,
                "Experiência": result.experience,
                "user_id": result.user_id,
                "feedback": result.feedback
            }
        )
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404


@main.route("/apagar_registro/<int:id>", methods=["DELETE"])
def delete_register(id):
    register = Person.query.get(id)

    if register:
        db.session.delete(register)
        db.session.commit()
        return jsonify({"message": f"Registro com ID {id} apagado com sucesso"}), 200
    else:
        return jsonify({"error": f"Registro com ID {id} não encontrado"}), 404


@main.route("/deletar_todos_os_respondentes", methods=["DELETE"])
def delete_all_people():
    try:
        people = Person.query.all()

        for person in people:
            db.session.delete(person)

        db.session.commit()

        return (
            jsonify({"message": "Todos os respondentes foram excluídos com sucesso."}),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     main.run(debug=True)
