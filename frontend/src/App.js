import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import OpeningPage from './pages/OpeningPage';
import FormPage from './pages/FormPage';
import TechnicPage from './pages/TechnicPage';
import RegisterPage from './pages/RegisterPage';


function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<OpeningPage />} />
          <Route path="/formulario" element={<FormPage />} />
          <Route path="/tecnica" element={<TechnicPage />} />
          <Route path="/registro" element={<RegisterPage />} />
        </Routes>
    </Router>
  );
}

export default App;
