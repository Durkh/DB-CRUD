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


CREATE OR REPLACE PROCEDURE adicionar_cliente(
    nome_param TEXT,
    cpf_param TEXT,
    email_param TEXT,
    time_do_coracao_param TEXT,
    obra_favorita_param TEXT,
    cidade_natal_param TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Inserir os dados na tabela pessoas
    INSERT INTO pessoas (nome, cpf, email)
    VALUES (nome_param, cpf_param, email_param);
    
    -- Inserir os dados na tabela clientes
    INSERT INTO clientes (cpf, time_do_coracao, obra_favorita, cidade_natal)
    VALUES (cpf_param, time_do_coracao_param, obra_favorita_param, cidade_natal_param);
    
END;
$$;

CREATE OR REPLACE PROCEDURE adicionar_vendedor(
    nome_param TEXT,
    cpf_param TEXT,
    email_param TEXT,
    matricula_param TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Inserir os dados na tabela pessoas
    INSERT INTO pessoas (nome, cpf, email)
    VALUES (nome_param, cpf_param, email_param);
    
    -- Inserir os dados na tabela funcionarios
    INSERT INTO funcionarios (cpf, matricula)
    VALUES (cpf_param, matricula_param);
    
END;
$$;

CREATE OR REPLACE PROCEDURE remover_cliente(
    cpf_param TEXT
)
LANGUAGE plpgsql
AS $$
begin
	
	-- Remover o cliente da tabela clientes
    DELETE FROM clientes WHERE cpf = cpf_param;
   
    -- Remover o cliente da tabela pessoas
    DELETE FROM pessoas WHERE cpf = cpf_param;
    
   
END;
$$;


CREATE OR REPLACE PROCEDURE remover_vendedor(
    cpf_param TEXT
)
LANGUAGE plpgsql
AS $$
begin
	    
    -- Remover o vendedor da tabela funcionarios
    DELETE FROM funcionarios WHERE cpf = cpf_param;
   
    -- Remover o vendedor da tabela pessoas
    DELETE FROM pessoas WHERE cpf = cpf_param;

    
END;
$$;

CREATE OR REPLACE PROCEDURE alterar_cliente(
    cpf_param TEXT,
    novo_nome_param TEXT,
    novo_email_param TEXT,
    novo_time_param TEXT,
    nova_obra_favorita_param TEXT,
    nova_cidade_natal_param TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Atualizar o nome e o e-mail na tabela pessoas
    UPDATE pessoas
    SET nome = novo_nome_param, email = novo_email_param
    WHERE cpf = cpf_param;
    
    -- Atualizar o time do coração, a obra favorita e a cidade natal na tabela clientes
    UPDATE clientes
    SET time_do_coracao = novo_time_param, obra_favorita = nova_obra_favorita_param, cidade_natal = nova_cidade_natal_param
    WHERE cpf = cpf_param;
    
END;
$$;

CREATE OR REPLACE PROCEDURE alterar_vendedor(
    cpf_param TEXT,
    novo_nome_param TEXT,
    novo_email_param TEXT,
    nova_matricula_param TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Atualizar o nome e o e-mail na tabela pessoas
    UPDATE pessoas
    SET nome = novo_nome_param, email = novo_email_param
    WHERE cpf = cpf_param;
    
    -- Atualizar a matrícula na tabela funcionarios
    UPDATE funcionarios
    SET matricula = nova_matricula_param
    WHERE cpf = cpf_param;
    
END;
$$;