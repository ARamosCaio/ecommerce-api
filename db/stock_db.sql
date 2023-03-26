create database stock;
use stock;

create table couches (
    id int not null auto_increment primary key,
    product_type set('Canto', 'Sofá-cama', 'Poltrona', 'Retrátil'),
    product_size set('2 lugares', '3 lugares', '4 lugares'),
    amount_stock int default 0,
    price decimal(6,2) not null
);

create table beds (
    id int not null auto_increment primary key,
    product_type set('Cama box', 'Bicama', 'Tradicional de Madeira', 'Cama baú'),
    product_size set('Solteiro', 'Casal'),
    amount_stock int default 0,
    price decimal(6,2) not null
);

create table wardrobe (
    id int not null auto_increment primary key,
    product_type set('Porta de correr sem espelho','Porta de puxar sem espelho', 'Porta de correr e espelho', 'Porta de puxar e espelho'),
    product_size set('2 portas', '3 portas', '4 portas'),
    amount_stock int default 0,
    price decimal(6,2) not null
);