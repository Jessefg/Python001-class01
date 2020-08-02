
create database filmdb default charset utf8 collate utf8_general_ci;

CREATE TABLE `comments` (
   `id` bigint NOT NULL AUTO_INCREMENT,
   `stars` int NOT NULL DEFAULT '0',
   `comment` varchar(400) NOT NULL DEFAULT '',
   `sentiment` float(12,10) NOT NULL DEFAULT '0.0000000000',
   PRIMARY KEY (`id`)
 ) DEFAULT CHARSET=utf8;



