-- SCRIPT SQL FINAL: APENAS INSERÇÃO DE DADOS (Certificado sempre Pendente)

-- --------------------------------------------------------
-- 1. Limpeza (Obrigatório para começar do zero)
-- --------------------------------------------------------

DELETE FROM inscricao;
DELETE FROM evento;
DELETE FROM usuario;
DELETE FROM sqlite_sequence WHERE name='usuario';
DELETE FROM sqlite_sequence WHERE name='evento';
DELETE FROM sqlite_sequence WHERE name='inscricao';

-- --------------------------------------------------------
-- 2. População de USUÁRIOS CHAVE (8 Usuários Principais)
-- IDs 1 a 8
-- --------------------------------------------------------

INSERT INTO usuario (nome, telefone, instituicao_ensino, perfil, data_criacao, data_atualizacao) VALUES 
('Ana Organizadora Líder', '61987654321', 'Universidade CEUB', 'ORGANIZADOR', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Bruno Gerente Eventos', '61911112222', 'Faculdade de Tecnologia', 'ORGANIZADOR', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Carlos Organizador', '61933334444', 'Universidade CEUB', 'ORGANIZADOR', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Profa. Denise Matematicas', '61955556666', 'Universidade CEUB', 'PROFESSOR', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Prof. Eduardo Web', '61977778888', 'Universidade CEUB', 'PROFESSOR', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Felipe Aluno ADS', '61912345678', 'Universidade CEUB', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Gabriela Aluna Design', '61987654321', 'Faculdade de Artes', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Henrique Testador', '61910102020', 'Universidade CEUB', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- --------------------------------------------------------
-- 3. População de USUÁRIOS DE TESTE (50 Alunos Adicionais)
-- IDs 9 a 58
-- --------------------------------------------------------

INSERT INTO usuario (nome, telefone, instituicao_ensino, perfil, data_criacao, data_atualizacao)
VALUES 
('Aluno Teste 09', '61910000009', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 10', '61910000010', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 11', '61910000011', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 12', '61910000012', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 13', '61910000013', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 14', '61910000014', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 15', '61910000015', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 16', '61910000016', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 17', '61910000017', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 18', '61910000018', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 19', '61910000019', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 20', '61910000020', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 21', '61910000021', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 22', '61910000022', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 23', '61910000023', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 24', '61910000024', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 25', '61910000025', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 26', '61910000026', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 27', '61910000027', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 28', '61910000028', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 29', '61910000029', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 30', '61910000030', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 31', '61910000031', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 32', '61910000032', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 33', '61910000033', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 34', '61910000034', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 35', '61910000035', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 36', '61910000036', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 37', '61910000037', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 38', '61910000038', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 39', '61910000039', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 40', '61910000040', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 41', '61910000041', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 42', '61910000042', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 43', '61910000043', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 44', '61910000044', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 45', '61910000045', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 46', '61910000046', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 47', '61910000047', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 48', '61910000048', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 49', '61910000049', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 50', '61910000050', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 51', '61910000051', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 52', '61910000052', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 53', '61910000053', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 54', '61910000054', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 55', '61910000055', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 56', '61910000056', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 57', '61910000057', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Aluno Teste 58', '61910000058', 'Universidade Teste', 'ALUNO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- --------------------------------------------------------
-- 4. População de EVENTOS (IDs 1 a 4)
-- --------------------------------------------------------

INSERT INTO evento (nome, tipo_evento, palestrante_nome, data_inicial, data_final, horario, local, quantidade_participantes, organizador_responsavel_id, data_criacao, data_atualizacao)
VALUES ('Palestra: O Futuro da I.A. no Desenvolvimento', 'PALESTRA', 'Dr. Alencar Smith', '2025-11-10 14:00:00', '2025-11-10 16:00:00', '14:00:00', 'Auditório Principal', 50, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP); 

INSERT INTO evento (nome, tipo_evento, palestrante_nome, data_inicial, data_final, horario, local, quantidade_participantes, organizador_responsavel_id, data_criacao, data_atualizacao)
VALUES ('Seminário de Boas Práticas de Código', 'SEMINARIO', 'Equipe Tec.', '2025-11-15 09:00:00', '2025-11-15 12:00:00', '09:00:00', 'Sala de Reuniões 10B', 2, 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP); 

INSERT INTO evento (nome, tipo_evento, palestrante_nome, data_inicial, data_final, horario, local, quantidade_participantes, organizador_responsavel_id, data_criacao, data_atualizacao)
VALUES ('Minicurso: Introdução ao Framework Django', 'MINICURSO', 'Prof. Eduardo Web', '2025-12-01 09:00:00', '2025-12-05 12:00:00', '09:00:00', 'Laboratório 301', 30, 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO evento (nome, tipo_evento, palestrante_nome, data_inicial, data_final, horario, local, quantidade_participantes, organizador_responsavel_id, data_criacao, data_atualizacao)
VALUES ('Semana de Inovação e Startups', 'SEMANA_ACADEMICA', 'Vários Convidados', '2026-03-20 08:00:00', '2026-03-24 18:00:00', '08:00:00', 'Bloco Principal', 200, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- NO ARQUIVO sgea_script_expandido.sql (Seção 5):

-- Cenário 1: Certificado Emitido (ID 4)
-- Este campo TEM que ser 1 (True) para fins de teste.

INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES (4, 1, 1, CURRENT_TIMESTAMP); 

-- Cenário 2: Vagas Esgotadas (Lotando o Seminário - 2 vagas)
-- CORREÇÃO: Adicionando '0' para certificado_emitido

INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES (6, 2, 0, CURRENT_TIMESTAMP);
INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES (7, 2, 0, CURRENT_TIMESTAMP); 

-- Cenário 3: Inscrição em Massa (Lotando o Evento 1 - Palestra I.A.)
-- Todos estes devem ser 0 (Falso)

INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES 
(9, 1, 0, CURRENT_TIMESTAMP),
(10, 1, 0, CURRENT_TIMESTAMP),
(11, 1, 0, CURRENT_TIMESTAMP),
(12, 1, 0, CURRENT_TIMESTAMP),
(13, 1, 0, CURRENT_TIMESTAMP),
(14, 1, 0, CURRENT_TIMESTAMP),
(15, 1, 0, CURRENT_TIMESTAMP),
(16, 1, 0, CURRENT_TIMESTAMP),
(17, 1, 0, CURRENT_TIMESTAMP),
(18, 1, 0, CURRENT_TIMESTAMP),
(19, 1, 0, CURRENT_TIMESTAMP),
(20, 1, 0, CURRENT_TIMESTAMP),
(21, 1, 0, CURRENT_TIMESTAMP),
(22, 1, 0, CURRENT_TIMESTAMP),
(23, 1, 0, CURRENT_TIMESTAMP),
(24, 1, 0, CURRENT_TIMESTAMP),
(25, 1, 0, CURRENT_TIMESTAMP),
(26, 1, 0, CURRENT_TIMESTAMP),
(27, 1, 0, CURRENT_TIMESTAMP),
(28, 1, 0, CURRENT_TIMESTAMP),
(29, 1, 0, CURRENT_TIMESTAMP),
(30, 1, 0, CURRENT_TIMESTAMP),
(31, 1, 0, CURRENT_TIMESTAMP),
(32, 1, 0, CURRENT_TIMESTAMP),
(33, 1, 0, CURRENT_TIMESTAMP),
(34, 1, 0, CURRENT_TIMESTAMP),
(35, 1, 0, CURRENT_TIMESTAMP),
(36, 1, 0, CURRENT_TIMESTAMP),
(37, 1, 0, CURRENT_TIMESTAMP),
(38, 1, 0, CURRENT_TIMESTAMP),
(39, 1, 0, CURRENT_TIMESTAMP),
(40, 1, 0, CURRENT_TIMESTAMP),
(41, 1, 0, CURRENT_TIMESTAMP),
(42, 1, 0, CURRENT_TIMESTAMP),
(43, 1, 0, CURRENT_TIMESTAMP),
(44, 1, 0, CURRENT_TIMESTAMP),
(45, 1, 0, CURRENT_TIMESTAMP),
(46, 1, 0, CURRENT_TIMESTAMP),
(47, 1, 0, CURRENT_TIMESTAMP),
(48, 1, 0, CURRENT_TIMESTAMP),
(49, 1, 0, CURRENT_TIMESTAMP),
(50, 1, 0, CURRENT_TIMESTAMP),
(51, 1, 0, CURRENT_TIMESTAMP),
(52, 1, 0, CURRENT_TIMESTAMP),
(53, 1, 0, CURRENT_TIMESTAMP),
(54, 1, 0, CURRENT_TIMESTAMP),
(55, 1, 0, CURRENT_TIMESTAMP),
(56, 1, 0, CURRENT_TIMESTAMP),
(57, 1, 0, CURRENT_TIMESTAMP),
(58, 1, 0, CURRENT_TIMESTAMP);

-- Cenário 4: Inscrições Normais

INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES (5, 3, 0, CURRENT_TIMESTAMP);
INSERT INTO inscricao (usuario_id, evento_id, certificado_emitido, data_inscricao)
VALUES (8, 4, 0, CURRENT_TIMESTAMP);