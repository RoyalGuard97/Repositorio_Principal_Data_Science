CREATE PROCEDURE PoblarAtenciones 
AS
	
	TRUNCATE TABLE ACCENTURE.dbo.BaseAtenciones;
	TRUNCATE TABLE BDACCENTURE.dbo.BaseTickets;
	TRUNCATE TABLE ACCENTURE.dbo.Atenciones;

	BULK INSERT PRUEBA.dbo.BaseAtenciones
	FROM 'C:\Users\edgar\Desktop\WEBINARS\SQL SERVER\DATA CSV\Atenciones.csv'
	WITH (
			FORMAT = 'CSV'
			, FIRSTROW = 2
			, FIELDTERMINATOR = ';'
			, ROWTERMINATOR = '\n'
		)


	BULK INSERT PRUEBA.dbo.BaseTickets
	FROM 'C:\Users\edgar\Desktop\WEBINARS\SQL SERVER\DATA CSV\Tickets.csv'
	WITH (
			FORMAT = 'CSV'
			, FIRSTROW = 2
			, FIELDTERMINATOR = ';'
			, ROWTERMINATOR = '\n'
		)

	BULK INSERT ACCENTURE.dbo.DimCategoria
	FROM 'C:\Users\edgar\Desktop\WEBINARS\SQL SERVER\DATA CSV\Categoria.csv'
	WITH (
			FORMAT = 'CSV'
			, FIRSTROW = 2
			, FIELDTERMINATOR = ';'
			, ROWTERMINATOR = '\n'
		)


	BULK INSERT ACCENTURE.dbo.DimTipo
	FROM 'C:\Users\edgar\Desktop\WEBINARS\SQL SERVER\DATA CSV\Tipo.csv'
	WITH (
			FORMAT = 'CSV'
			, FIRSTROW = 2
			, FIELDTERMINATOR = ';'
			, ROWTERMINATOR = '\n'
		)


	BULK INSERT ACCENTURE.dbo.DimDetalle
	FROM 'C:\Users\edgar\Desktop\WEBINARS\SQL SERVER\DATA CSV\Detalle.csv'
	WITH (
			FORMAT = 'CSV'
			, FIRSTROW = 2
			, FIELDTERMINATOR = ';'
			, ROWTERMINATOR = '\n'
		)


	SELECT 
		num_ticket
		, categoria
		, tipo
		, detalle
		, ubicacion
		,

		CASE estado
			WHEN 'Terminado' THEN 'Cerrado'
			ELSE estado
		END as estado,
	
		CONVERT(date, TRIM(fecha_creacion), 103) as 'fecha_creacion',
		CONVERT(date, TRIM(COALESCE(fecha_termino, fecha_cierre)), 103) as 'fecha_real_fin',

		CASE CHARINDEX(' - ', ubicacion)
		WHEN 0 THEN NULL
		ELSE CHARINDEX(' - ', ubicacion) + 3
		END as inicio,
		len(ubicacion) as fin

	INTO PRUEBA.dbo.ETL_tickets1
	FROM PRUEBA.dbo.BaseTickets;

----------------------------------------

	SELECT	A.num_ticket,
			
			CASE A.inicio
				WHEN NULL THEN NULL
				ELSE TRIM(SUBSTRING(A.ubicacion, A.inicio, A.fin))
			END as 'AgenciaID',
			
			CASE C.CategoriaID
				WHEN NULL THEN 10
				ELSE C.CategoriaID
			END as 'CategoriaID',
			
			CASE T.TipoID
				WHEN NULL THEN 100
				ELSE T.TipoID
			END as 'TipoID',

			CASE D.DetalleID
				WHEN NULL THEN 100
				ELSE D.DetalleID
			END as 'DetalleID',

			A.estado,
			A.fecha_creacion,
			A.fecha_real_fin
	INTO PRUEBA.dbo.ETL_tickets2
	FROM PRUEBA.dbo.ETL_tickets1 A
	LEFT JOIN ACCENTURE.dbo.DimCategoria C
	ON A.categoria = C.Categoria
	LEFT JOIN ACCENTURE.dbo.DimTipo T
	ON A.tipo = T.Tipo
	LEFT JOIN ACCENTURE.dbo.DimDetalle D
	ON A.detalle = D.Detalle;
	
----------------------------------------

	SELECT	num_ticket,

	CONVERT(date, TRIM(fecha_programada), 103) as 'fecha_programada',

	TRIM(service_desk) as 'service_desk',

	CASE LEFT(UPPER(TRIM(tipo_ticket)), 4)
		WHEN 'DIFE' THEN 'FLAT'
		WHEN 'VARI' THEN 'VARIABLE'
		ELSE UPPER(TRIM(tipo_ticket))
	END as 'tipo_ticket',

	TRIM(proveedor) as 'proveedor',

	CAST(
	CASE costo
		WHEN 'SIN COSTO' then NULL
		ELSE costo
	END 
	as smallmoney)
	as 'costo'

	INTO PRUEBA.dbo.ETL_atenciones1
	FROM PRUEBA.dbo.BaseAtenciones;
	
-----------------------------------------

	INSERT INTO ACCENTURE.dbo.Atenciones
	SELECT	A.num_ticket,
			T.AgenciaID,
			T.CategoriaID,
			T.TipoID,
			T.DetalleID,
			T.fecha_creacion, 
			A.fecha_programada,
			T.fecha_real_fin,
			T.estado,
			A.service_desk,
			A.tipo_ticket,
			A.proveedor,
			A.costo
	FROM PRUEBA.dbo.ETL_atenciones1 as A
	INNER JOIN PRUEBA.dbo.ETL_tickets2 as T
	ON A.num_ticket = T.num_ticket;



	DROP TABLE ETL_tickets1;
	DROP TABLE ETL_tickets2;
	DROP TABLE ETL_atenciones1;
GO

SELECT * FROM ACCENTURE.dbo.Atenciones;