// i18n.js

import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n
  .use(initReactI18next) // inicializa o react-i18next
  .init({
    resources: {
      en: {
        translation: {
          category: 'Category',
          cost: "Cost",
          explanation: "Explanation",
          parametrization: "Parametrization",
          productivity: "Productivity",
          reliability: "Reliability",
          responsible: "Responsible",
          time: "Time"
        },
      },
      pt: {
        translation: {
          category: 'Categoria',
          cost: "Custo",
          explanation: "Necessidade de explicação",
          parametrization: "Padronização",
          productivity: "Produtividade",
          reliability: "Confiança",
          responsible: "Responsável",
          time: "Tempo"
        },
      },
    },
    lng: 'en', // idioma padrão
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false, // reage a entradas HTML nas traduções
    },
  });

export default i18n;
