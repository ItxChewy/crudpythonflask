CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT DEFAULT 0,
  `username` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `image_filename` varchar(255) DEFAULT NULL,
  `image_blob` longblob,
  `numeric_column` float DEFAULT NULL,
  `date_column` date DEFAULT NULL
) 