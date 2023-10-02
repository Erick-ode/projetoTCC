import React, { useState, useEffect } from 'react';
import { fetchQuestionsFromBackend, postAnswersToBackend } from '../AppService';
import { Link } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import './styles/questionnaire.css'

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

  useEffect(() => {
    loadQuestions();
  }, []);

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
    console.log(updatedAnswers[questionParameter])
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
    postAnswersToBackend(answers)
      .then((response) => {
        console.log('Resposta do servidor:', response.data);
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
          {questions[currentQuestion].options.map((option, index) => (
            <div key={index}>
              <label>
                <input
                  type="radio"
                  name="options"
                  value={option}
                  checked={answers[questions[currentQuestion].parameter].some((answer) => {
                    return answer.answer === option;
                  })}
                  onChange={() => handleAnswer(option)} />
                <span >{option}</span>
              </label>
            </div>
          ))}
          {questions[currentQuestion].type === 'text' && (
            <input
              type="text"
              value={answers[questions[currentQuestion].parameter].length > 0
                ? answers[questions[currentQuestion].parameter][0].answer
                : ''}
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
        <Link to="/tecnica">
          <div className="finish-button-container">
            <button onClick={sendAnswers}>Finalizar questionário</button>
          </div>
        </Link>
      )}
    </div>
  );
}

export default Questionnaire;
