#creeer een database
CREATE DATABASE gnomad;
use gnomad;

CREATE TABLE variants (
  chrom VARCHAR(2),
  pos INTEGER(35),
  bef VARCHAR(2),
  aft VARCHAR(2),
  freq FLOAT(30)
);

INSERT INTO variants
  (chrom, pos, bef, aft, freq)

VALUES
    ('Y','1','G','A','2.3');

