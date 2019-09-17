create database car;

use car;

create table car(
    id_car int auto_incremente primary key not null,
    name_car varchar(255) not null,
    model varchar(255) not null,
    year varchar(255) not null,
    price varchar(255) not null
)engine=InnoDB;

create table user_login(
    id_user int auto_incremente primary key not null,
    username varchar(255) not null,
    password varchar(255) not null,
)