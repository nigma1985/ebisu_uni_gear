DROP VIEW IF EXISTS v_tankerkoenig CASCADE;

CREATE VIEW v_tankerkoenig AS
(SELECT
  id,
	method,
	ok::BOOLEAN AS ok,
	license,
	data,
	status,
	utc_datetime::TIMESTAMP AS utc_datetime,
	"user"
FROM
	public.tankerkoenig
);
