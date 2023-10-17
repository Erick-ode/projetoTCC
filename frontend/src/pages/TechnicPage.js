import React, { useState, useEffect } from 'react';
import './styles/openingPage.css';
import { fetchTechnicFromBackend, fetchAllResultsFromBackend } from '../AppService';

const allResults = null;


function TechnicPage() {
  const [technic, setTechnic] = useState({ coherence: 0.0, name: '' });
  const [results, setResults] = useState([]);

  useEffect(() => {

    fetchAllResultsFromBackend()
      .then((response) => {
        const allResults = response.data;
        setResults(allResults);
      })
      .catch((error) => {
        console.error('Erro ao buscar resultados do backend:', error);
      });
      
      const id = results.length;
  
      fetchTechnicFromBackend(id)
          .then((response) => {
            const technicData = response.data
            setTechnic({ coherence: technicData.Coerência, name: technicData.Técnica });
          })
          .catch((error) => {
            console.error('Erro ao buscar a técnica do backend:', error);
          });
  }, []);

  return (
    <div className='container'>
      <h1>Técnica Calculada</h1>
      <p>Nome da Técnica: {technic.name.toUpperCase()}</p>
      <p>Confiança: {technic.coherence.toFixed(2)}</p>
      <button onClick={() => window.location.href = '/'}>Voltar para a Página Inicial</button>
    </div>
  );
}

export default TechnicPage;
