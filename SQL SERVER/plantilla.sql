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

--Insertar Valores.
insert into tabla1_03(A,B) values 
('C1','Alto'),('C2','Medio') ,('C3','Medio') ,('C4','Bajo') 

select * from tabla1_03

--Uso de Casos y Agregar Nueva Columna en la visualizacion
select A,B, 
CASE WHEN B = 'Alto' THEN 20
WHEN B = 'Medio' THEN 14
ELSE 10 END AS FILTRO from tabla1_03

--Actualizar una tabla, modificar
update tabla1_03 set A = 'C5' where B = 'Bajo'

--Basicamente eliminar Duplicado. 
select distinct * from tabla1_03