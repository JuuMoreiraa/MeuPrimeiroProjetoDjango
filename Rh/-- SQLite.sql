-- SQLite
--SQL (Structure Query Language)
--MDL (Manipulate Data Language)

-- insere registros na tabela
SELECT * FROM Rh_departamento;

INSERT INTO Rh_departamento (id, nome)
VALUES (6, 'Rh')

INSERT INTO Rh_departamento (id, nome)
VALUES (7, 'Docentes')

-- apaga registros da tabela

DELETE FROM Rh_departamento WHERE id = 7;


--ORM (Object Relational Mapping)