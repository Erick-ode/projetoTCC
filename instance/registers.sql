SQLite format 3   @     (                                                               ( .4 N ? V*!?�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         �)++�	tablealembic_versionalembic_versionCREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
)=Q+ indexsqlite_autoindex_alembic_version_1alembic_version�t�CtableresultresultCREATE TABLE result (
	id INTEGER NOT NULL, 
	name VARCHAR(100), 
	confidence_level FLOAT, 
	person_id INTEGER, 
	answers JSON, 
	PRIMARY KEY (id), 
	UNIQUE (person_id), 
	FOREIGN KEY(person_id) REFERENCES person (id)
)+? indexsqlite_autoindex_result_1result       �'�)tablepersonpersonCREATE TABLE person (
	id INTEGER NOT NULL, 
	role VARCHAR(100), 
	experience VARCHAR(100), 
	chosen_technic VARCHAR(50), 
	PRIMARY KEY (id)
)   � ��|QB�����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 S)AnalistaSêniorPrototipação  /!TEstessasJuniorEtnografia     4 !AnalistaSêniorEntrevista! )AnalistaJuniorPrototipação  wacPleno) 7AnalistaSêniorAnálise de protocolo' ')DesenvolvedorSêniorPrototipação  ' )DesenvolvedorPrototipação7 97Analista de requisitosSêniorAnálise de protocolo   �    �                                                                    �1 !�;entrevista@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "4"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria Juniors"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Observa\u00e7\u00e3o"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "6"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "Pleno"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "Muita confian\u00e7a"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}�4 1�1analiseDeProtocolo@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "5"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria Juniors"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Observa\u00e7\u00e3o"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "1"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "Pleno"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "N\u00e3o confio"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}�@ '�Uquestionarios@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "4"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria S\u00eanior"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Ferramenta automatizada"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "1"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "S\u00eanior"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "Muita confian\u00e7a"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alt   
   � ����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          	   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      %b726754d2b95
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      %	b726754d2b95    R 
�� R                                                                    �1 !�;entrevista@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "4"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria Juniors"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Observa\u00e7\u00e3o"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "6"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "Pleno"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "Muita confian\u00e7a"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}�4 1�1analiseDeProtocolo@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "5"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria Juniors"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Observa\u00e7\u00e3o"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "1"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "Pleno"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "N\u00e3o confio"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}�@ '�Uquestionarios@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "4"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Maioria S\u00eanior"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Ferramenta automatizada"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "1"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "S\u00eanior"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "Muita confian\u00e7a"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}   
� 
�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            �W '�questionarios@Q�m��m�{"time": [{"question_id": 0, "field_name": "Qual o tempo de desenvolvimento (em meses)?", "answer": "4"}], "cost": [{"question_id": 1, "field_name": "Como est\u00e1 distribu\u00eddo o n\u00edvel de pessoas da equipe?", "answer": "Mais s\u00eaniors e plenos do que juniors"}], "responsible": [{"question_id": 2, "field_name": "Quantas pessoas participam do levantamento de requisitos?", "answer": "1"}, {"question_id": 3, "field_name": "\u00c9 poss\u00edvel apenas uma pessoa fazer?", "answer": "Sim"}], "explanation": [{"question_id": 4, "field_name": "Quais ferramentas prefere utilizar no levantamento de requisitos?", "answer": "Ferramenta automatizada"}, {"question_id": 5, "field_name": "Quantas horas por semana o cliente precisa participar do projeto?", "answer": "4"}], "reliability": [{"question_id": 6, "field_name": "N\u00edvel do aplicador da t\u00e9cnica?", "answer": "S\u00eanior"}, {"question_id": 7, "field_name": "N\u00edvel de confian\u00e7a na fonte de informa\u00e7\u00f5es?", "answer": "Muita confian\u00e7a"}], "parametrization": [{"question_id": 8, "field_name": "Opta por m\u00e9todos padronizados ou aceita trabalhar com m\u00e9todos din\u00e2micos?", "answer": "M\u00e9todos din\u00e2micos"}], "productivity": [{"question_id": 9, "field_name": "Qual o n\u00edvel de produtividade da equipe?", "answer": "Alta"}]}