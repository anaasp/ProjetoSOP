CREATE DATABASE bancoProjeto;
USE bancoProjeto;

-- 3. Criar a tabela de usuários
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Chave primária com autoincremento
    username VARCHAR(100) NOT NULL,        -- Nome de usuário
    email VARCHAR(255) NOT NULL UNIQUE,    -- Email único
    password VARCHAR(255) NOT NULL,        -- Senha (normalmente você armazenaria um hash aqui)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp automático
);

-- 4. Criar a tabela de comentários
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Chave primária com autoincremento
    user_id INT,                               -- ID do usuário que fez o comentário
    comment TEXT NOT NULL,                     -- O texto do comentário
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data e hora do comentário
    FOREIGN KEY (user_id) REFERENCES users(id) -- Chave estrangeira referenciando a tabela de usuários
);

-- 5. (Opcional) Criar outras tabelas se necessárias, por exemplo, para categorizar comentários ou guardar likes
-- Aqui é um exemplo de uma tabela de likes para os comentários

CREATE TABLE likes (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Chave primária com autoincremento
    user_id INT,                                -- ID do usuário que deu o like
    comment_id INT,                             -- ID do comentário que recebeu o like
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp automático
    FOREIGN KEY (user_id) REFERENCES users(id), -- Relaciona com a tabela de usuários
    FOREIGN KEY (comment_id) REFERENCES comments(id) -- Relaciona com a tabela de comentários
);

-- 6. (Opcional) Você pode adicionar índices para melhorar o desempenho de consultas
CREATE INDEX idx_user_id ON comments(user_id);
CREATE INDEX idx_comment_id ON likes(comment_id);