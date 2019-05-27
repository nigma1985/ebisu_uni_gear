DROP VIEW IF EXISTS v_place CASCADE;

CREATE VIEW v_place AS
	(SELECT
		id,
		type,
		CAST ( place_id AS INTEGER ) AS place_id,
		CAST ( location AS BIGINT ) AS location,
		name,
		facebookplaceid,
		foursquareid
	FROM public.place
);
