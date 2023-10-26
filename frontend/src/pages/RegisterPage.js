import React, { useState, useEffect } from 'react';
import { fetchRegistrationQuestionsFromBackend } from '../AppService';
import { useNavigate } from 'react-router-dom';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa';
import './styles/questionnaire.css'
import useAuth from '../hooks/useAuth';

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
  ],
  user_id: Math.floor(Math.random() * (Math.floor(1000) - Math.ceil(1) + 1)) + 1
};


function Register() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState(answers_expecteds);

  const { signup } = useAuth();
  const { signin } = useAuth();
  
  const navigate = useNavigate();

  useEffect(() => {
    loadQuestions();
  }, []);

  function loadQuestions() {
    fetchRegistrationQuestionsFromBackend()
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
    const updatedAnswers = { ...answers };
  
    
      signup(updatedAnswers);
      
      setTimeout(() => {
        signin(updatedAnswers);
        
        navigate("/formulario");
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

    <div className="button-container">
      {currentQuestion < questions.length - 1 ? (
        <button onClick={handleNextQuestion}><FaArrowRight /></button>
      ) : (
        <button onClick={sendAnswers}>Iniciar questionário</button>
      )}
    </div>
  </div>
);

}

export default Register;
