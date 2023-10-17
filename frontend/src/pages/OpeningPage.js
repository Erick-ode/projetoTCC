import React from 'react';
import './styles/openingPage.css'
import { Link } from 'react-router-dom';

function OpeningPage() {
  return (
    <div className='container'>
      <h1>Bem-vindo ao Nosso Questionário sobre Técnicas de Levantamento de Requisitos</h1>
      <p>
        Este questionário tem o intuito de ajudar na escolha da melhor técnica de levantamento de requisitos para o seu projeto, com base em diversos parâmetros. As perguntas abordarão os seguintes aspectos:
      </p>
      <ul className='topic-list'>
        <li><strong>Tempo do Projeto:</strong> Avaliaremos o tempo estimado para o desenvolvimento;</li>
        <li><strong>Custo:</strong> Analisaremos o orçamento disponível;</li>
        <li><strong>Equipe:</strong> Verificaremos a quantidade de pessoas necessárias para levantar os requisitos;</li>
        <li><strong>Complexidade:</strong> Mediremos o quanto é preciso explicar sobre o projeto para que ele seja compreendido;</li>
        <li><strong>Experiência:</strong> Levar em conta o nível de experiência do aplicante e a qualidade da fonte de informações;</li>
        <li><strong>Padronização:</strong> Consideraremos a necessidade de padronização da técnica utilizada;</li>
        <li><strong>Produtividade:</strong> Analisaremos o impacto no nível de produtividade da equipe na implementação dos requisitos levantados.</li>
      </ul>
      <p>
        Por favor, preencha o questionário com atenção e honestidade. Agradecemos por sua colaboração!
      </p>

      <Link to="/registro">
        <button className="btn">Iniciar Questionário</button>
      </Link>
    </div>
  );
}

export default OpeningPage;
