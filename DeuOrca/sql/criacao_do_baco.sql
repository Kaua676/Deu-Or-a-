create database DeuOrca;

create table type_product (
	id serial primary key not null,
	name varchar(30)
);

insert into type_product(name) values('produto');
insert into type_product(name) values('serviço');
insert into type_product(name) values('transporte');

create table clients (
	id serial primary key not null,
	name varchar(255),
	cpf varchar(14),
	phone varchar(20)
);

create table users (
	id serial primary key not null,
	name varchar(50),
	email varchar(100),
	password varchar(25),
	cpf_cnpj varchar(18),
	type_user varchar(20),
	logo varchar(255)
);

create table products (
	id serial primary key not null,
	name varchar(100),
	price decimal(10,2),
	type_product_id int not null,
	foreign key (type_product_id) references type_product(id)
		on delete cascade
		on update cascade
);

create table budgets (
	id serial primary key not null,
	date date,
	total_value decimal(10,2),
	discounted_value decimal(10,2),
	client_id int not null,
	foreign key (client_id) references clients(id)
		on delete cascade
		on update cascade
);

create table budgets_products (
	id serial primary key not null,
	budget_id int not null,
	product_id int not null,
	foreign key (budget_id) references budgets(id)
		on delete cascade
		on update cascade,
	foreign key (product_id) references products(id)
		on delete cascade
		on update cascade
);


