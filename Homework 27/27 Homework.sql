--radganac wina davalebebic ar mewera
CREATE TABLE Deposit (
    DepositID SERIAL PRIMARY KEY,
    DepOwnerName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    City VARCHAR(100) NOT NULL,
    StreetName VARCHAR(150) NOT NULL,
    DepositAmount DECIMAL(15, 2) NOT NULL,
    Interest DECIMAL(5, 2) NOT NULL,
    Comission DECIMAL(10, 2) NOT NULL,
    Total DECIMAL(15, 2) NOT NULL
);


CREATE TABLE "Order" (
    OrderID SERIAL PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerPhone VARCHAR(15) NOT NULL,
    ProductName VARCHAR(150) NOT NULL,
    ProductCategory VARCHAR(100) NOT NULL,
    ProductCategoryType VARCHAR(100) NOT NULL,
    ProductPrice DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    OrderDate DATE NOT NULL,
    DeliveryAddress VARCHAR(200) NOT NULL,
    DepositID INT,
    CONSTRAINT fk_deposit FOREIGN KEY (DepositID) REFERENCES Deposit (DepositID)
);



INSERT INTO Deposit (DepOwnerName, DateOfBirth, City, StreetName, DepositAmount, Interest, Comission, Total)
VALUES
('Alice Brown', '1990-01-15', 'Springfield', '123 Elm Street', 5000, 3.5, 100, 5150),
('Bob Green', '1985-06-10', 'Rivertown', '456 Oak Avenue', 7000, 4.0, 150, 7350),
('Charlie Smith', '1992-09-20', 'Mapleton', '789 Pine Road', 3000, 3.0, 75, 3075),
('Diane White', '1988-11-05', 'Lakeside', '456 Oak Avenue', 6000, 4.2, 120, 6120);


INSERT INTO "Order" (CustomerName, CustomerPhone, ProductName, ProductCategory, ProductCategoryType, ProductPrice, Quantity, OrderDate, DeliveryAddress, DepositID)
VALUES
('Alice Brown', '555-1234', 'MacBook Air M2', 'Electronics', 'Laptop', 1200, 1, '2025-01-01', '123 Elm Street', 1),
('Bob Green', '555-5678', 'iPhone 14 Pro', 'Electronics', 'Smartphone', 1100, 2, '2025-01-02', '456 Oak Avenue', 2),
('Alice Brown', '555-1234', 'Herman Miller Chair', 'Furniture', 'Office Chair', 1500, 1, '2025-01-03', '123 Elm Street', 1),
('Bob Green', '555-5678', 'Dell XPS 13', 'Electronics', 'Laptop', 1000, 1, '2025-01-04', '456 Oak Avenue', 2),
('Alice Brown', '555-1234', 'Samsung Galaxy S23', 'Electronics', 'Smartphone', 900, 1, '2025-01-05', '123 Elm Street', 1),
('Charlie Smith', '555-7890', 'Logitech MX Master 3', 'Electronics', 'Computer Accessory', 99.99, 2, '2025-01-06', '789 Pine Road', 3),
('Diane White', '555-3456', 'Sony WH-1000XM5', 'Electronics', 'Headphones', 349.99, 1, '2025-01-07', '456 Oak Avenue', 4),
('Charlie Smith', '555-7890', 'Ikea Bekant Desk', 'Furniture', 'Office Desk', 299.99, 1, '2025-01-08', '789 Pine Road', 3);
