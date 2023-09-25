from flask import Flask, request, jsonify, redirect, url_for
from backend.src.main.models.fuzzy_simulation import FuzzySimulation
from backend.src.main.models.fuzzy_structure import FuzzyStructure

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá mundo!'


@app.route('/processar_respostas', methods=['POST'])
def post_answers():
    data = request.get_json()

    time = data.get('time', 0.0)
    cost = data.get('cost', 0.0)
    responsible = data.get('responsible', 0.0)
    explanation = data.get('explanation', 0.0)
    reliability = data.get('reliability', 0.0)
    patronization = data.get('patronization', 0.0)
    productivity = data.get('productivity', 0.0)

    fuzzy_structure = FuzzyStructure()
    fuzzy_simulator = FuzzySimulation(time, cost, responsible, explanation, reliability, patronization, productivity)

    technic_result = fuzzy_simulator.calculate_fuzzy(fuzzy_structure.rules)

    return redirect(url_for('get_technic', technic_result=technic_result))


@app.route('/retornar_tecnica')
def get_technic():
    result = request.args.get('technic_result', '')

    return f'Resultado: {result}'


if __name__ == '__main__':
    app.run(debug=True)
