##TABELA CLIENTES
CREATE TABLE `clientes` (
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `endereco` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE KEY `cpf_unico` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

##TABELA PETS
CREATE TABLE `pets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `raca` varchar(20) NOT NULL,
  `cor` varchar(15) DEFAULT NULL,
  `cpf_dono` varchar(11) NOT NULL,
  `total_servicos` int(11) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `cpf_dono` (`cpf_dono`),
  CONSTRAINT `pets_ibfk_1` FOREIGN KEY (`cpf_dono`) REFERENCES `clientes` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

###TABELA SERVICO
CREATE TABLE `servico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

###TABELA SERVICO_REALIZADOS
CREATE TABLE `servico_realizados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpf_dono` varchar(11) DEFAULT NULL,
  `pet_id` int(11) NOT NULL,
  `servico_id` int(11) NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `data_hora` datetime NOT NULL,
  `nome_pet` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cpf_cliente` (`cpf_dono`),
  KEY `pet_id` (`pet_id`),
  KEY `servico_id` (`servico_id`),
  CONSTRAINT `servico_realizados_ibfk_1` FOREIGN KEY (`cpf_dono`) REFERENCES `clientes` (`cpf`),
  CONSTRAINT `servico_realizados_ibfk_2` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`),
  CONSTRAINT `servico_realizados_ibfk_3` FOREIGN KEY (`servico_id`) REFERENCES `servico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
