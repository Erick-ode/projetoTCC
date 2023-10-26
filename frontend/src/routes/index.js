import { React, Fragment } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import OpeningPage from '../pages/OpeningPage';
import FormPage from '../pages/FormPage';
import TechnicPage from '../pages/TechnicPage';
import RegisterPage from '../pages/RegisterPage';
import useAuth from '../hooks/useAuth';

const Private = ({ Item }) => {
  const {signed} = useAuth();

  return signed > 0 ? <Item /> : <OpeningPage />
}


function RoutesApp() {
  return (
    <BrowserRouter>
      <Fragment>
        <Routes>
          <Route path="/" element={<OpeningPage />} />
          <Route exact path="/formulario" element={<Private Item={FormPage} />} />
          <Route exact path="/tecnica" element={<Private Item={TechnicPage} />} />
          <Route path="/registro" element={<RegisterPage />} />
          <Route paht="*" element={<OpeningPage />}></Route>
        </Routes>
      </Fragment>
    </BrowserRouter>
    
  );
}

export default RoutesApp;
