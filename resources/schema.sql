# DDL(CREATE, ALTER, DROP) 테이블 생성문

CREATE TABLE `tbl_review` (
	`no` INT(10) NOT NULL AUTO_INCREMENT,
	`review` VARCHAR(500) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`score` INT(10) NOT NULL DEFAULT '0',
	`writer` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`reg_date` DATETIME NOT NULL,
	PRIMARY KEY (`no`) USING BTREE
)
COMMENT='다음 영화 리뷰'
COLLATE='utf8mb4_general_ci'
ENGINE=INNODB
;
