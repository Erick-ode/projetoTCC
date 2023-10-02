import React from 'react';
import './styles/openingPage.css'
import { Link } from 'react-router-dom';

function OpeningPage() {
  return (
    <div class='container'>
        <h1>Bem-vindo ao Nosso Questionário</h1>
        <p>
            Aqui está uma breve descrição do propósito do questionário.
            Você pode adicionar mais detalhes aqui.
        </p>
        <Link to="/formulario">
          <button class="btn">Iniciar Questionário</button>
        </Link>
    </div>
  );
}

export default OpeningPage;
