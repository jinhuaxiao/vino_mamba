CREATE  TABLE `vino_manba_db`.`tb_cse_result` (
  `cse_id` INT NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(100) NULL ,
  `link` VARCHAR(255) NULL ,
  `cacheId` VARCHAR(50) NULL ,
  `snippet` VARCHAR(255) NULL ,
  `generateTime` DATETIME NULL ,
  `keywords` VARCHAR(300) NULL,
  PRIMARY KEY (`cse_id`) ,
  UNIQUE INDEX `cse_id_UNIQUE` (`cse_id` ASC) );

