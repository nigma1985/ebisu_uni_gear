DROP VIEW IF EXISTS v_openingtimes CASCADE;

CREATE VIEW v_openingtimes AS
(SELECT
	id,
	text,
	start::TIME,
	"end"::TIME,
	results::INTEGER
FROM
	public.openingtimes
);
