import { createContext, useState, useEffect } from "react";
import { postRegistrationToBackend, fetchPersonFromBackend } from "../AppService";

export const AuthContext = createContext({});

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState();

    useEffect(() => {
        setUser(user)
      }, [user]);


    const signin = (answers) => {
        let user = answers["user_id"];
        fetchPersonFromBackend(user)
            .then((response) => {
                const returnedUser = response.data;
                setUser(returnedUser["user_id"]);
                return;
            })
            .catch((error) => {
                console.error('Usuário não encontrado', error);
              });
    };

    function signup(answers) {
        postRegistrationToBackend(answers)
            .then((response) => {
                console.log('Resposta do servidor:', response.data);
            })
            .catch((error) => {
                console.error('Erro ao enviar respostas para o servidor:', error);
            });
    }

    const signout = () => {
        setUser(null);
        localStorage.removeItem("user_token");
    };

    return (
        <AuthContext.Provider
            value={{ user, signed: !!user, signin, signup, signout }}
        >
            {children}
        </AuthContext.Provider>
    );
}