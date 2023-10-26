import React from 'react';
import './styles/openingPage.css'
import { useNavigate } from 'react-router-dom';

function OpeningPage() {
  const navigate = useNavigate();

  return (
    <div className='container'>
      <h1>Bem-vindo ao Nosso Questionário sobre Técnicas de Levantamento de Requisitos</h1>
      <p>
      Este questionário tem o intuito de ajudar na escolha da melhor técnica de levantamento de requisitos para o seu projeto. As perguntas abordarão os seguintes aspectos:
      </p>
      <ul className='topic-list'>
        <li><strong>Tempo do Projeto:</strong> Avaliaremos o tempo estimado para o desenvolvimento;</li>
        <li><strong>Custo:</strong> Analisaremos quanto custa a equipe de desenvolvimento;</li>
        <li><strong>Equipe:</strong> Verificaremos a quantidade de pessoas necessárias para levantar os requisitos;</li>
        <li><strong>Complexidade:</strong> Mediremos o quanto é preciso explicar sobre o projeto para que ele seja compreendido;</li>
        <li><strong>Confiabilidade:</strong> Levar em conta o nível de experiência do aplicante e a qualidade da fonte de informações;</li>
        <li><strong>Padronização:</strong> Consideraremos a necessidade de padronização da técnica utilizada;</li>
        <li><strong>Produtividade:</strong> Analisaremos o impacto no nível de produtividade da equipe na implementação dos requisitos levantados.</li>
      </ul>
      <p>
      As respostas serão utilizadas em uma aplicação que utiliza lógica fuzzy, método de aprendizado de máquina destinado a estabelecer uma técnica de levantamento com base nas combinações de respostas com um determinado grau de confiança.
      </p>
      <p>
        Por favor, preencha o questionário com atenção e honestidade. Agradecemos por sua colaboração!
      </p>


      <button className="btn" onClick={() => { navigate("/registro") }}>Iniciar Questionário</button>

    </div>
  );
}

export default OpeningPage;
