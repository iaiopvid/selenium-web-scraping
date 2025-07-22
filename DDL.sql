-- Copiando estrutura para tabela fidelity.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `cod_cliente` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `nome` text NOT NULL,
  `documento` varchar(20) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`cod_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `cod_uf` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uf` char(2) NOT NULL,
  `cod_fornecedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`cod_uf`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.lote
CREATE TABLE IF NOT EXISTS `lote` (
  `cod_lote` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cod_lote_prazo` text DEFAULT NULL,
  `cod_funcionario` int(11) DEFAULT NULL,
  `prioridade` text DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`cod_lote`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.lote_pesquisa
CREATE TABLE IF NOT EXISTS `lote_pesquisa` (
  `cod_lote_pesquisa` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cod_lote` bigint(20) unsigned DEFAULT NULL,
  `cod_pesquisa` bigint(20) unsigned DEFAULT NULL,
  `cod_funcionario` int(11) DEFAULT NULL,
  `cod_funcionario_conclusao` int(11) DEFAULT NULL,
  `cod_fornecedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`cod_lote_pesquisa`),
  KEY `cod_lote` (`cod_lote`),
  KEY `cod_pesquisa` (`cod_pesquisa`),
  CONSTRAINT `lote_pesquisa_ibfk_1` FOREIGN KEY (`cod_lote`) REFERENCES `lote` (`cod_lote`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `lote_pesquisa_ibfk_2` FOREIGN KEY (`cod_pesquisa`) REFERENCES `pesquisa` (`cod_pesquisa`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.pesquisa
CREATE TABLE IF NOT EXISTS `pesquisa` (
  `cod_pesquisa` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cod_cliente` int(11) NOT NULL,
  `cod_uf` bigint(20) unsigned NOT NULL,
  `cod_servico` bigint(20) unsigned NOT NULL,
  `tipo` int(11) DEFAULT 0,
  `cpf` varchar(20) DEFAULT NULL,
  `cod_uf_nascimento` char(2) NOT NULL,
  `cod_uf_rg` char(2) NOT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `rg_corrigido` varchar(20) DEFAULT NULL,
  `nome` text DEFAULT NULL,
  `nome_corrigido` text DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `mae` text DEFAULT NULL,
  `mae_corrigido` text DEFAULT NULL,
  `anexo` text DEFAULT NULL,
  `data_entrada` timestamp NULL DEFAULT current_timestamp(),
  `data_conclusao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cod_pesquisa`),
  KEY `cod_uf` (`cod_uf`),
  KEY `cod_servico` (`cod_servico`),
  CONSTRAINT `pesquisa_ibfk_1` FOREIGN KEY (`cod_uf`) REFERENCES `estado` (`cod_uf`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pesquisa_ibfk_2` FOREIGN KEY (`cod_servico`) REFERENCES `servico` (`cod_servico`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.pesquisa_spv
CREATE TABLE IF NOT EXISTS `pesquisa_spv` (
  `cod_spv` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cod_pesquisa` bigint(20) unsigned DEFAULT NULL,
  `cod_spv_computador` int(11) DEFAULT NULL,
  `cod_spv_tipo` text DEFAULT NULL,
  `resultado` int(11) DEFAULT NULL,
  `cod_funcionario` int(11) DEFAULT NULL,
  `filtro` int(11) DEFAULT NULL,
  `website_id` int(11) DEFAULT NULL,
  `data_execucao` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`cod_spv`),
  KEY `cod_pesquisa` (`cod_pesquisa`),
  CONSTRAINT `pesquisa_spv_ibfk_1` FOREIGN KEY (`cod_pesquisa`) REFERENCES `pesquisa` (`cod_pesquisa`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando estrutura para tabela fidelity.servico
CREATE TABLE IF NOT EXISTS `servico` (
  `cod_servico` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `civel` text NOT NULL,
  `criminal` text DEFAULT NULL,
  PRIMARY KEY (`cod_servico`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
