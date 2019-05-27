DROP VIEW IF EXISTS v_activities CASCADE;

CREATE VIEW v_activities AS
(SELECT
  	id,
  	activity,
  	"group",
  	CAST ( segments AS BIGINT ) AS segments,
  	CAST ( manual AS BOOLEAN ) AS manual,
  	CAST ( starttime AS TIMESTAMPTZ ) AS starttime,
  	CAST ( endtime AS TIMESTAMPTZ ) AS endtime,
  	CAST ( duration AS FLOAT ) AS duration,
  	CAST ( steps AS FLOAT ) AS steps,
  	CAST ( distance AS FLOAT ) AS distance,
  	CAST ( calories AS FLOAT ) AS calories
  FROM public.activities
);
