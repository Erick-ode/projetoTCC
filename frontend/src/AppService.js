import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const API_ROUTES = {
    fetchTechnic: `${API_BASE_URL}/retornar_tecnica`,
    fetchQuestions: `${API_BASE_URL}/carregar_perguntas`,
    postAnswers: `${API_BASE_URL}/processar_respostas`,
};

export function fetchTechnicFromBackend(id) {
    return axios.get(`${API_ROUTES.fetchTechnic}/${id}`);
}

export function fetchQuestionsFromBackend() {
    return axios.get(API_ROUTES.fetchQuestions);
}

export function postAnswersToBackend(data) {
    return axios.post(API_ROUTES.postAnswers, data);
}
