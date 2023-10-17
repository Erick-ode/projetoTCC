import React, { useState, useEffect } from 'react';
import { fetchRegistrationFromBackend, postRegistrationToBackend } from '../AppService';
import { Link } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import './styles/questionnaire.css'
import { setSessionData } from '../Session'

const answers_expecteds = {
  role: [
    {
      question_id: 0,
      field_name: null,
      answer: null
    }
  ],
  experience: [
    {
      question_id: 1,
      field_name: null,
      answer: null
    }
  ],
  technic: [
    {
      question_id: 2,
      field_name: null,
      answer: null
    }
  ]
};


function Register() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState(answers_expecteds);

  useEffect(() => {
    loadQuestions();
  }, []);

  function loadQuestions() {
    fetchRegistrationFromBackend()
      .then((response) => {
        const loadedQuestions = response.data;
        setQuestions(loadedQuestions);
      })
      .catch((error) => {
        console.error('Erro ao carregar as perguntas:', error);
      });
  }

  const handleAnswer = (answer) => {
    const questionId = questions[currentQuestion].id;
    const questionParameter = questions[currentQuestion].parameter
    const question = questions[currentQuestion].question

    const updatedAnswers = { ...answers };

    for (const item in updatedAnswers[questionParameter]) {
      if (updatedAnswers[questionParameter][item].question_id.toString() === questionId) {
        updatedAnswers[questionParameter][item].answer = answer
        updatedAnswers[questionParameter][item].field_name = question
      }
    }
    setAnswers(updatedAnswers);

  };

  const handleNextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      console.log('Respostas:', answers);
    }
  };

  function goToPreviousQuestion() {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  }

  function sendAnswers() {
    console.log(answers)
    postRegistrationToBackend(answers)
      .then((response) => {
        console.log('Resposta do servidor:', response.data);
        setSessionData('userID', response.data.userID);
        setSessionData('userName', response.data.userName);
      })
      .catch((error) => {
        console.error('Erro ao enviar respostas para o servidor:', error);
      });
  }


  return (
    <div className="question-nav">
      <button onClick={goToPreviousQuestion} disabled={currentQuestion === 0}>
        <FaArrowLeft />
      </button>
      {currentQuestion < questions.length ? (
        <div className='question-container'>
          <h2>Pergunta {currentQuestion + 1}</h2>
          <p>{questions[currentQuestion].question}</p>
          {questions[currentQuestion].type === 'options' && (
            <select className='select-input'
              value={answers[questions[currentQuestion].parameter][0].answer}
              onChange={(e) => handleAnswer(e.target.value)}
            >
              <option>...</option>
              {questions[currentQuestion].options.map((option, index) => (
                <option key={index} value={option}>
                  {option}
                </option>
              ))}
            </select>
          )}

          {questions[currentQuestion].type === 'text' && (
            <input
              type="text"
              className='text-input'
              value={answers[questions[currentQuestion].parameter][0].answer || ''}
              onChange={(e) => handleAnswer(e.target.value)} />
          )}
        </div>
      ) : (
        <div>
          <p>Cadastramento concluído!</p>
        </div>
      )}
      {currentQuestion < questions.length - 1 ? (
        <button onClick={handleNextQuestion}><FaArrowRight /></button>
      ) : (
        <Link to="/formulario">
          <div className="finish-button-container">
            <button onClick={sendAnswers}>Iniciar questionário</button>
          </div>
        </Link>
      )}
    </div>
  );
}

export default Register;
