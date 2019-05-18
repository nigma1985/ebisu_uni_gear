CREATE TABLE "SuperStore";

ALTER TABLE "SuperStore"
	ADD COLUMN rowID TEXT,
	ADD COLUMN orderID TEXT,
	ADD COLUMN orderDate TEXT,
	ADD COLUMN shipDate TEXT,
	ADD COLUMN shipMode TEXT,
	ADD COLUMN customerID TEXT,
	ADD COLUMN customerName TEXT,
	ADD COLUMN segment TEXT,
	ADD COLUMN city TEXT,
	ADD COLUMN "state" TEXT,
	ADD COLUMN country TEXT,
	ADD COLUMN po TEXT,
	ADD COLUMN market TEXT,
	ADD COLUMN region TEXT,
	ADD COLUMN productID TEXT,
	ADD COLUMN category TEXT,
	ADD COLUMN subCategory TEXT,
	ADD COLUMN productName TEXT,
	ADD COLUMN sales TEXT,
	ADD COLUMN quantity TEXT,
	ADD COLUMN discount TEXT,
	ADD COLUMN profit TEXT,
	ADD COLUMN shippingCost TEXT,
	ADD COLUMN orderPriority TEXT
;

DROP VIEW IF EXISTS v_superstore CASCADE;

CREATE VIEW v_superstore AS
	(SELECT
		CAST ( rowID AS INTEGER ) AS rowID,
		orderID,
		CAST ( orderDate AS DATE ) AS orderDate,
		CAST ( shipDate AS DATE ) AS shipDate,
		shipMode,
		customerID,
		customerName,
		segment,
		city,
		"state",
		country,
		CASE WHEN po = '' THEN NULL ELSE CAST ( po AS INTEGER ) END AS po,
		market,
		region,
		productID,
		category,
		subCategory,
		TRIM(both '"' from productName) AS productName,
		CAST ( sales AS REAL ) AS sales,
		CAST ( quantity AS INTEGER ) AS quantity,
		CAST ( discount AS REAL ) AS discount,
		CAST ( profit AS REAL ) AS profit,
		CAST ( shippingCost AS REAL ) AS shippingCost,
		CAST ( orderPriority AS TEXT ) AS orderPriority
	FROM "SuperStore"
);
