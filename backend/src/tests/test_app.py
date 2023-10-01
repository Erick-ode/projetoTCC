import json

from main import main
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        main.testing = True
        self.app = main.test_client()

    def test_root_source(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_tecnic(self):
        response = self.app.get('/retornar_tecnica')
        self.assertEqual(response.status_code, 200)

    def test_post_answers(self):
        json_string = '''
        {
            "time": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "4"
                }
            ],
            "cost": [
                {
                    "question_id": 0,
                    "field_name": "",
                    "answer": "Sênior:6;Pleno:2;Junior:3"
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
                    "answer": "diagrama"
                },
                {
                    "question_id": 1,
                    "field_name": "",
                    "answer": "4"
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
                    "answer": "Alta"
                }
            ]
        }
        '''
        response = self.app.post('/processar_respostas', json=json.loads(json_string), content_type='application/json')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
