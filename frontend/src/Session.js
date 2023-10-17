// session.js

// Função para armazenar informações de sessão
export function setSessionData(key, value) {
    localStorage.setItem(key, value);
  }
  
  // Função para verificar as informações de sessão
  export function getSessionData(key) {
    return localStorage.getItem(key);
  }
  
  // Função para encerrar a sessão
  export function clearSessionData(key) {
    localStorage.removeItem(key);
  }
  
  export function isUserLoggedIn() {
    // Verifique se as informações da sessão existem
    const userID = getSessionData('userID');
    const userName = getSessionData('userName');
    
    // Considere o usuário logado se as informações da sessão estiverem presentes
    return !!userID && !!userName;
  }
  