import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const API_ROUTES = {
    fetchTechnic: `${API_BASE_URL}/retornar_tecnica`,

    fetchQuestions: `${API_BASE_URL}/carregar_perguntas`,
    fecthRegisterQuestions: `${API_BASE_URL}/carregar_perguntas_registro`,

    fetchPeople: `${API_BASE_URL}/retornar_pessoas`,

    postAnswers: `${API_BASE_URL}/processar_respostas`,
    postRegister: `${API_BASE_URL}/registrar_respondente`
};

export function fetchTechnicFromBackend(id) {
    return axios.get(`${API_ROUTES.fetchTechnic}/${id}`);
}

export function fetchAllResultsFromBackend() {
    return axios.get(API_ROUTES.fetchTechnic);
}

export function fetchQuestionsFromBackend() {
    return axios.get(API_ROUTES.fetchQuestions);
}

export function fetchRegistrationFromBackend() {
    return axios.get(API_ROUTES.fecthRegisterQuestions);
}

export function fetchPeopleFromBackend() {
    return axios.get(API_ROUTES.fetchPeople);
}

export function fetchPersonFromBackend() {
    return axios.get(`${API_ROUTES.fetchPeople}/${id}`);
}

export function postAnswersToBackend(data) {
    return axios.post(API_ROUTES.postAnswers, data);
}

export function postRegistrationToBackend(data) {
    return axios.post(API_ROUTES.postRegister, data);
}
