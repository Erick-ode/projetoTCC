import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';

const API_ROUTES = {
    fetchResult: `${API_BASE_URL}/retornar_resultados`,

    fetchPeople: `${API_BASE_URL}/retornar_pessoas`,

    fetchQuestions: `${API_BASE_URL}/carregar_perguntas`,
    fecthRegisterQuestions: `${API_BASE_URL}/carregar_perguntas_registro`,

    postAnswers: `${API_BASE_URL}/processar_respostas`,
    postRegister: `${API_BASE_URL}/registrar_respondente`,

    postFeedback: `${API_BASE_URL}/adicionar_feedback`
};

export function fetchResultFromBackend(user_id) {
    return axios.get(`${API_ROUTES.fetchResult}/${user_id}`);
}


export function fetchQuestionsFromBackend() {
    return axios.get(API_ROUTES.fetchQuestions);
}

export function fetchRegistrationQuestionsFromBackend() {
    return axios.get(API_ROUTES.fecthRegisterQuestions);
}

export function fetchPersonFromBackend(id) {
    return axios.get(`${API_ROUTES.fetchPeople}/${id}`);
}

export function postAnswersToBackend(data, id) {
    return axios.post(`${API_ROUTES.postAnswers}/${id}`, data);
}

export function postRegistrationToBackend(data) {
    return axios.post(API_ROUTES.postRegister, data);
}

export function postFeedbackToBackend(data, id) {
    return axios.post(`${API_ROUTES.postFeedback}/${id}`, data);
}
