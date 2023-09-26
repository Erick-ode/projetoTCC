import unittest
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor


class TestQuestionnaireProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.response = {

            "time": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "6"
                }
            ],
            "cost": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "Sênior:3;Pleno:5;Junior:8"
                }
            ],
            "responsible": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "5"
                },
                {
                    "question_id": 1,
                    "field_name": "",
                    "answer": "sim"
                }
            ],
            "explanation": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "ferramenta automatizada"
                },
                {
                    "question_id": 1,
                    "field_name": "",
                    "answer": "13"
                }
            ],
            "reliability": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "senior"
                },
                {
                    "question_id": 1,
                    "field_name": "",
                    "answer": "partially_trust"
                }
            ],
            "parametrization": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "Sim"
                }
            ],
            "productivity": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "Média"
                }
            ]

        }
        self.processor = QuestionnaireProcessor(self.response)

    def test_process_time(self):
        self.processor.process_time()

        self.assertEqual(self.processor.input_values['time'], 8.0)

    def test_process_cost(self):
        self.processor.process_cost()

        self.assertEqual(self.processor.input_values['cost'], 40.0)

    def test_process_responsible(self):
        self.processor.process_responsible()

        self.assertEqual(self.processor.input_values['responsible'], 4.5)

    def test_process_explanation(self):
        self.processor.process_explanation()

        self.assertEqual(self.processor.input_values['explanation'], 10.75)

    def test_process_reliability(self):
        self.processor.process_reliability()

        self.assertEqual(self.processor.input_values['reliability'], 92.14)

    def test_process_parametrization(self):
        self.processor.process_parametrization()

        self.assertEqual(self.processor.input_values['parametrization'], 2.5)

    def test_process_productivity(self):
        self.processor.process_productivity()

        self.assertEqual(self.processor.input_values['productivity'], 45.00)
