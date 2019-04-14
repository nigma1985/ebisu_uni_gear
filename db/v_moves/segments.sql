DROP VIEW IF EXISTS v_segments CASCADE;

CREATE VIEW v_segments AS
	(SELECT
		id,
		CAST ( starttime AS TIMESTAMPTZ ) AS starttime,
		CAST ( endtime AS TIMESTAMPTZ ) AS endtime,
		type,
		CAST ( place AS INTEGER ) AS place,
		CAST ( moves AS BIGINT ) AS moves,
		CAST ( lastupdate AS TIMESTAMP ) AS lastupdate
	FROM public.segments
);
