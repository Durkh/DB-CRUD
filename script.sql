CREATE TABLE pessoas (
	nome varchar NOT NULL,
	cpf varchar NOT NULL,
	email varchar NULL,
	CONSTRAINT pessoas_pk PRIMARY KEY (cpf)
);

CREATE TABLE clientes (
	cpf varchar NOT NULL,
	time_do_coracao varchar NOT NULL,
	obra_favorita varchar NOT NULL,
	cidade_natal varchar NOT NULL,
	CONSTRAINT clientes_pk PRIMARY KEY (cpf)
);

CREATE TABLE funcionarios (
	cpf varchar NOT NULL,
	matricula varchar NOT NULL,
	CONSTRAINT funcionarios_pk PRIMARY KEY (cpf)
);

CREATE TABLE estoque (
	ISBN varchar NOT NULL,
	titulo varchar,
	autor varchar,
	volume int,
	preco real NOT NULL DEFAULT 0,
	quantidade int NOT NULL DEFAULT 0,
	categoria varchar,
	local_de_fab varchar,

	CONSTRAINT estoque_pk PRIMARY KEY (ISBN)
);

CREATE TABLE vendas (
	cliente varchar NULL,
	vendedor varchar NULL,
	id_venda serial NOT NULL,
	quantidade int NULL,
	total real NULL,
	metodo_pagamento varchar NULL,
	status_pagamento varchar NULL,
	CONSTRAINT vendas_pk PRIMARY KEY (id_venda)
);

CREATE TABLE itens_vendidos (
    id_venda serial NOT NULL,
	ISBN varchar NOT NULL,
	preco real NOT NULL DEFAULT 0,
	quantidade int NOT NULL DEFAULT 0,
    desconto varchar NOT NULL
);

CREATE TABLE public.relatorio_venda (
	id_relatorio int NOT NULL,
	matricula varchar NULL,
	id_venda int NULL,
	quantidade int NULL,
	total float4 NULL,
	"data" int NULL
);

CREATE OR REPLACE VIEW view_clientes AS
SELECT pessoas.nome, pessoas.cpf, pessoas.email, clientes.time_do_coracao, clientes.obra_favorita, clientes.cidade_natal 
FROM pessoas
JOIN clientes ON pessoas.cpf = clientes.cpf;

CREATE OR REPLACE VIEW view_funcionarios AS
SELECT pessoas.nome, pessoas.cpf, pessoas.email, funcionarios.matricula 
FROM pessoas
JOIN funcionarios ON pessoas.cpf = funcionarios.cpf;

CREATE OR REPLACE VIEW view_vendas AS
SELECT vendas.id_venda, view_clientes.nome as cliente, view_funcionarios.nome as funcionario, vendas.quantidade, vendas.total, vendas.metodo_pagamento, vendas.status_pagamento, vendas.cliente as cpf_cliente, vendas.vendedor as cpf_funcionario
FROM vendas
JOIN view_clientes ON vendas.cliente = view_clientes.cpf
JOIN view_funcionarios ON vendas.vendedor = view_funcionarios.cpf;

CREATE OR REPLACE VIEW view_itens_vendidos AS
SELECT itens_vendidos.id_venda, estoque.titulo, itens_vendidos.quantidade, itens_vendidos.preco
FROM itens_vendidos
JOIN estoque ON itens_vendidos.isbn = estoque.isbn;
