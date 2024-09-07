CREATE TABLE Automovil (
    id INT PRIMARY KEY AUTO_INCREMENT,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    max_velocidad INT NOT NULL,
    consumo_por_km DECIMAL(4,2) NOT NULL,
    combustible DECIMAL(6,2) NOT NULL
);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Toyota', 'Corolla', 180, 0.07, 45.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Honda', 'Civic', 200, 0.06, 50.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Ford', 'Mustang', 250, 0.12, 55.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Chevrolet', 'Camaro', 240, 0.11, 60.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Tesla', 'Model S', 220, 0.00, 0.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Nissan', 'Altima', 210, 0.08, 40.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('BMW', 'Serie 3', 230, 0.09, 45.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Audi', 'A4', 240, 0.08, 55.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Mercedes-Benz', 'C-Class', 220, 0.10, 50.00);

INSERT INTO Automovil (marca, modelo, max_velocidad, consumo_por_km, combustible) 
VALUES ('Mazda', 'CX-5', 190, 0.09, 60.00);

SELECT * FROM Automovil;

SELECT * FROM Automovil WHERE combustible > 50;

SELECT marca, modelo FROM Automovil WHERE consumo_por_km < 0.08;

SELECT SUM(combustible) AS total_combustible FROM Automovil;

SELECT marca, modelo FROM Automovil ORDER BY max_velocidad DESC LIMIT 1;