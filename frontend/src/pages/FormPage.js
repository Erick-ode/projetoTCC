import React, { useState, useEffect } from 'react';
import { fetchQuestionsFromBackend, postAnswersToBackend } from '../AppService';
import { useNavigate } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import './styles/questionnaire.css';
import useAuth from '../hooks/useAuth';

const answers_expecteds = {
  time: [
    {
      question_id: 0,
      field_name: null,
      answer: null,
    },
  ],
  cost: [
    {
      question_id: 1,
      field_name: null,
      answer: null,
    },
  ],
  responsible: [
    {
      question_id: 2,
      field_name: null,
      answer: null,
    },
    {
      question_id: 3,
      field_name: null,
      answer: null,
    },
  ],
  explanation: [
    {
      question_id: 4,
      field_name: null,
      answer: null,
    },
    {
      question_id: 5,
      field_name: null,
      answer: null,
    },
  ],
  reliability: [
    {
      question_id: 6,
      field_name: null,
      answer: null,
    },
    {
      question_id: 7,
      field_name: null,
      answer: null,
    },
  ],
  parametrization: [
    {
      question_id: 8,
      field_name: null,
      answer: null,
    },
  ],
  productivity: [
    {
      question_id: 9,
      field_name: null,
      answer: null,
    },
  ],
};


function Questionnaire() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState(answers_expecteds);
  
  const navigate = useNavigate();

  const { user } = useAuth();

  useEffect(() => {
    loadQuestions();
    if (answers === null) {
      setAnswers(answers_expecteds);
    }
  }, [answers]);

  function loadQuestions() {
    fetchQuestionsFromBackend()
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
      sendAnswers();
    }
  };

  function goToPreviousQuestion() {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  }

  function sendAnswers() {    
    postAnswersToBackend(answers, user)
      .then((response) => {
        console.log('Resposta do servidor:', response.data);
      })
      .catch((error) => {
        console.error('Erro ao enviar respostas para o servidor:', error);
      });
      setTimeout(() => {
        navigate("/tecnica");
      }, 500);
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
              value={answers[questions[currentQuestion].parameter].length > 1
                ? answers[questions[currentQuestion].parameter][1].answer
                : answers[questions[currentQuestion].parameter][0].answer}
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

          {questions[currentQuestion].type === 'number' && (
            <input className='number-input'
              type="number"
              value={answers[questions[currentQuestion].parameter].length > 1
                ? answers[questions[currentQuestion].parameter][1].answer
                : answers[questions[currentQuestion].parameter][0].answer}
              onChange={(e) => handleAnswer(e.target.value)} />
          )}

        </div>
      ) : (
        <div>
          <p>Questionário concluído!</p>
        </div>
      )}
      {currentQuestion < questions.length - 1 ? (
        <button onClick={handleNextQuestion}><FaArrowRight /></button>
      ) : (
        <div className="finish-button-container">
          <button onClick={handleNextQuestion}>Finalizar questionário</button>
        </div>
      )}
    </div>
  );
}

export default Questionnaire;
