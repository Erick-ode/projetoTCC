import React from 'react';
// import { fetchDataFromBackend } from './AppService';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import OpeningPage from './pages/OpeningPage';
import FormPage from './pages/FormPage';
import TechnicPage from './pages/TechnicPage';


function App() {
  // const [data, setData] = useState([{}])
  // useEffect(() => {
  //   fetchDataFromBackend()
  //     .then((response) => {
  //       setData(response.data);
  //     })
  //     .catch((error) => {
  //       console.error('Erro ao buscar dados do backend:', error);
  //     });
  // }, [])

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Página de Abertura</Link>
            </li>
            <li>
              <Link to="/formulario">Formulário</Link>
            </li>
            <li>
              <Link to="/tecnica">Técnica</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<OpeningPage />} />
          <Route path="/formulario" element={<FormPage />} />
          <Route path="/tecnica" element={<TechnicPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
