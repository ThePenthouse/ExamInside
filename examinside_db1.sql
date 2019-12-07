-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: examinside
-- ------------------------------------------------------
-- Server version	5.7.28-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `quesid` int(11) NOT NULL AUTO_INCREMENT,
  `ques` varchar(100) NOT NULL,
  `option1` varchar(45) NOT NULL,
  `option2` varchar(45) NOT NULL,
  `option3` varchar(45) NOT NULL,
  `option4` varchar(45) NOT NULL,
  `ans` varchar(45) NOT NULL,
  PRIMARY KEY (`quesid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'We can have any number of classes in a java source file.','True','False','','','a'),(2,'Which of the following is not a java keyword?','static','try','Integer',' new','c'),(3,'JAVA is as acronym.',' True','False','','','b'),(4,'Which of the following classes are available in the java.lang package?',' Stack','Object','Vector','Random','b'),(5,'What is known as the founder of JAVA? ','James Gosling','Larry Page','Bjarne Stroustrup','None of these','a'),(6,'What is your name?','Lovely','Beauty','Subhajit','Daniel','a'),(7,'What is the oop language?','c','java','c#','python','java'),(8,'what is woomoodle?','moodle','woocommercemoodle','wordpressmoodle','woocommerce','c'),(9,'what is your name','sff','sdfsdf','sdfsdf','dsfdsf','b');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Contact` varchar(45) NOT NULL,
  `Profile_pic` varchar(45) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Debika Bhowmik','debika@gmail.com','debika123','7908611068','635959a421dc4839b5cb4ca1ccd6573e.jpg'),(2,'Lovely Chakraborty','Lovely345@gmail.com','lovely345','6789978944','11e3e53c596c4c92a0334603d79f7c84.jpg'),(3,'Prasad Bandyopadhyay','prsd1996@gmail.com','prsd1996','8907893453','9a29fa736622497ea8f5d6a362da7006.jpg'),(4,'Sayani Badyakar','sayani@gmail.com','sayani@1234','8978907970','9a29fa736622497ea8f5d6a362da7006.jpg'),(5,'Beauty Chakraborty','beau23ch@gmail.com','beauty123','7908611234','20190129_122528.jpg'),(6,'Dipankar Chowdhury','dip@gmail.com','dip123','7809875544','144d02a4-4d87-4135-9af1-f4017a686dd5.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-08  0:26:08
