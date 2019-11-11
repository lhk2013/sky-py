CREATE TABLE `meituan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `shopName` varchar(50) DEFAULT NULL,
  `tag` bigint(20) DEFAULT NULL,
  `tagName` varchar(255) DEFAULT NULL,
  `spuId` int(11) DEFAULT NULL,
  `spuName` varchar(255) DEFAULT NULL,
  `skuId` bigint(20) DEFAULT NULL,
  `spec` varchar(255) DEFAULT NULL,
  `originPrice` decimal(10,2) DEFAULT NULL,
  `currentPrice` decimal(10,2) DEFAULT NULL,
  `spuPromotionInfo` varchar(50) DEFAULT NULL,
  `praiseNum` varchar(50) DEFAULT NULL,
  `saleVolume` varchar(50) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

