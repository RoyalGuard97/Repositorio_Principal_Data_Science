--SQL-Completo

--¡¡CLASE 01!!
--Seleccionar apartados de una tabla
SELECT * from usuarios
--Observar la Estructura de una tabla
exec sp_columns usuarios
--Crear una nueva tabla 
create table cursos(
	nombre varchar (30),
	categoria varchar(10)
)
--Seleccionar otra tabla después de haberse creado
SELECT * from cursos

--Se le pide elmininar tabla cursos
drop table cursos

--Si se desea ejecutar todo al mismo tiempo, lo recomendable sería usar ";" al final.

--¡¡CLASE 02!! - Insertar Filas

--Uso de condicionales

--Eliminarmos el objeto identificado como "usuarios" si no es nulo su ID, aplicamos el query.
if OBJECT_ID('usuarios') is not NULL
    drop table usuarios

--Creamos una nueva tabla 
CREATE TABLE usuarios(
    nombre VARCHAR(30),
    clave VARCHAR(10)
)

--¿Cómo Insertar Nuevas Filas? Sencillo!

insert into usuarios(nombre,clave) values 
('Mariano','123abc')

insert into usuarios(nombre,clave) values 
('Ana','hola123')

SELECT * from usuarios

 
--¡¡CLASE 03!! - Tipos de Datos

if OBJECT_ID('libros') is not NULL  
    DROP TABLE libros

create table libros(
    titulo VARCHAR(80),
    autor VARCHAR(40),
    editorial VARCHAR(30),
    precio FLOAT,
    cantidad INTEGER
)
--Recuerda que con esto vemos la estructura de una tabla
exec sp_columns libros

--Insertamos Filas
insert into libros(titulo,autor,editorial,precio,cantidad) values ('Alicia','Mergoti','Santillana',23.60,150),('Avaro','Matias','Lumbreras',27.50,210)
--Los Datos numéricos no llevan comillas simples

select * from libros 

--¡¡CLASE 03!! - Tipos de Datos
select titulo,precio from libros where precio > 25

if OBJECT_ID('tabla1_01') is not NULL  
    DROP TABLE tabla1_01
if OBJECT_ID('tabla2_01') is not NULL  
    DROP TABLE tabla2_01

create table tabla1_01(
    A VARCHAR(5),
    B VARCHAR(5)
) 

create table tabla2_01(
    C VARCHAR(5),
    D VARCHAR(5)
) 

insert into tabla1_01(A,B) values 
('C1','S1'),('C2','S2'),('C3','S3')

insert into tabla2_01(C,D) values ('C1','W1'),('C2','W2')

select * from tabla1_01
SELECT * from tabla2_01

--RPTA
select A,B,D from tabla1_01 left join tabla2_01 on tabla1_01.A = tabla2_01.C


if OBJECT_ID('tabla1_02') is not NULL  
    DROP TABLE tabla1_02

create table tabla1_02(
    A VARCHAR(5),
    B VARCHAR(5),
    C INT
) 

insert into tabla1_02(A,B,C) values 
('C1','S1',2),('C2','S1',4),('C1','S2',8),('C2','S1',10),('C1','S2',3)

select * from tabla1_02

--RPTA - 2 - 1
select A,sum(C) as C from tabla1_02 GROUP BY A
--RPTA - 2 - 2
select A,B,sum(C) as C from tabla1_02 GROUP by A,B ORDER BY C ASC

if OBJECT_ID('tabla1_03') is not NULL 
    drop table tabla1_03

create table tabla1_03 (
    A VARCHAR(5),
    B VARCHAR(10)
)

insert into tabla1_03(A,B) values 
('C1','Alto'),('C2','Medio') ,('C3','Medio') ,('C4','Bajo') 

select * from tabla1_03

select A,B, 
CASE WHEN B = 'Alto' THEN 20
WHEN B = 'Medio' THEN 14
ELSE 10 END AS FILTRO from tabla1_03

update tabla1_03 set A = 'C5' where B = 'Bajo'

select * from tabla1_03
select distinct * from tabla1_03