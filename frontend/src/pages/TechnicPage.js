import React, { useState, useEffect } from 'react';
import './styles/openingPage.css';
import { fetchResultFromBackend, postFeedbackToBackend } from '../AppService';
import useAuth from '../hooks/useAuth';
import { useNavigate } from 'react-router-dom';

function TechnicPage() {
  const [technic, setTechnic] = useState({ coherence: 0.0, name: '' });
  const [answers, setAnswers] = useState([]);
  const [showAnswers, setShowAnswers] = useState(false);
  const [feedback, setFeedback] = useState("");

  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchResultFromBackend(user)
      .then((response) => {
        const result = response.data;   
        setTechnic({ coherence: result.Coerência, name: result.Técnica });
        setAnswers(result.Respostas)
      })
      .catch((error) => {
        console.error('Erro ao buscar resultados do backend:', error);
      });

  }, [user]);

  const handleFeedbackChange = (e) => {
    setFeedback(e.target.value);
  };

  const handleSendFeedback = () => {
    const feedbackData = { feedback : feedback };
    postFeedbackToBackend(feedbackData, user)
      .then((response) => {
        console.log('Feedback enviado:', response.data); 
        setFeedback("");
      })
      .catch((error) => {
        console.error('Erro ao enviar feedback para o servidor:', error);
      });
  };

  return (
    <div className='container'>
      <h1>Técnica Calculada</h1>
      <p>Nome da Técnica: {technic.name.toUpperCase()}</p>
      <p>Confiança: {technic.coherence.toFixed(2)}</p>

      <button onClick={() => setShowAnswers(!showAnswers)}>Mostrar Respostas</button>

      {showAnswers && (
        <div>
          <h2>Respostas:</h2>
          {Object.keys(answers).map((category) => (
            <div key={category}>
              
              {answers[category].map((answer, index) => (
                <div key={index}>
                  <h3>{answer.field_name}</h3>
                  <p>Resposta: {answer.answer}</p>
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      <div className="feedback-container">
        <h2>Escreva sua opinião sobre o resultado obtido a partir das suas respostas:</h2>
        <textarea
          className="feedback-textarea"
          value={feedback}
          onChange={handleFeedbackChange}
          placeholder="Digite seu feedback aqui"
          rows="4"
          cols="50"
        />
        <button onClick={handleSendFeedback}>Enviar Feedback</button>
      </div>

      <button onClick={() => navigate("/")}>Voltar para a Página Inicial</button>
    </div>
  );
}

export default TechnicPage;
