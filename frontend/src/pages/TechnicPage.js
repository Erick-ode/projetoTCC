import React, { useState, useEffect } from 'react';
import './styles/openingPage.css';
import { fetchTechnicFromBackend } from '../AppService';

function TechnicPage() {
  const [technic, setTechnic] = useState({coherence: 0.0, name: ''});

  useEffect(() => {
    fetchTechnicFromBackend(3)
      .then((response) => {
        const technicData = response.data
        setTechnic({coherence: technicData.Coerência, name: technicData.Técnica});
      })
      .catch((error) => {
        console.error('Erro ao buscar a técnica do backend:', error);
      });
  }, []);

  return (
    <div className='container'>
      <h1>Técnica Calculada</h1>
      <p>Nome da Técnica: {technic.name.toUpperCase()}</p>
      <p>Coerência: {technic.coherence.toFixed(2)}</p>
      <button onClick={() => window.location.href = '/'}>Voltar para a Página Inicial</button>
    </div>
  );
}

export default TechnicPage;
