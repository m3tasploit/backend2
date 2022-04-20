/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - election_ss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`election_ss` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `election_ss`;

/*Table structure for table `candidate` */

DROP TABLE IF EXISTS `candidate`;

CREATE TABLE `candidate` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `candidateid` varchar(25) DEFAULT NULL,
  `support1` varchar(25) DEFAULT NULL,
  `support2` varchar(25) DEFAULT NULL,
  `postid` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `candidate` */

insert  into `candidate`(`cid`,`candidateid`,`support1`,`support2`,`postid`) values (1,'','','',0),(15,'','','',0),(29,'6','6','7',8),(31,'7','6','6',8),(32,'8','7','6',9),(33,'6','6','6',8),(34,'8','8','8',6);

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `courseid` int(11) NOT NULL AUTO_INCREMENT,
  `coursename` varchar(50) DEFAULT NULL,
  `depid` int(11) DEFAULT NULL,
  `cyear` int(11) DEFAULT NULL,
  PRIMARY KEY (`courseid`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`courseid`,`coursename`,`depid`,`cyear`) values (1,'',NULL,0),(2,'ba',NULL,1),(3,'eerr',NULL,123),(4,'cvvx',NULL,1234),(12,'sdd',8,651),(11,'sanjsm',6,19999),(7,'vcs',7,5),(8,'afgh',6,1999),(9,'fdxctf',7,1999),(10,'gddgdgt',7,1888),(13,'sa',8,723),(15,'sasimatheri',7,1999),(20,'sasa',8,3);

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `depid` int(11) NOT NULL AUTO_INCREMENT,
  `depname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`depid`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`depid`,`depname`) values (8,'statisticss'),(7,'mathematics'),(6,'cs');

/*Table structure for table `election` */

DROP TABLE IF EXISTS `election`;

CREATE TABLE `election` (
  `eleid` int(11) NOT NULL AUTO_INCREMENT,
  `elename` varchar(20) DEFAULT NULL,
  `dateandtime` datetime DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`eleid`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `election` */

insert  into `election`(`eleid`,`elename`,`dateandtime`,`status`) values (6,'aelection','2019-12-21 21:00:20','of'),(5,'aelection','2019-12-21 21:00:20','axasx');

/*Table structure for table `elevote` */

DROP TABLE IF EXISTS `elevote`;

CREATE TABLE `elevote` (
  `evid` int(11) NOT NULL AUTO_INCREMENT,
  `stuid` int(11) DEFAULT NULL,
  `candid` int(11) DEFAULT NULL,
  `dateandtime` date DEFAULT NULL,
  PRIMARY KEY (`evid`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `elevote` */

insert  into `elevote`(`evid`,`stuid`,`candid`,`dateandtime`) values (1,0,0,'0000-00-00'),(3,7,5,'2010-11-20'),(10,6,7,'2010-11-20'),(8,7,6,'2010-11-20'),(9,8,7,'2010-11-20'),(11,8,0,'0000-00-00'),(12,8,0,'0000-00-00'),(13,8,0,'2010-11-20'),(14,6,0,'2010-11-20'),(15,6,0,'2010-11-20'),(16,8,0,'2010-11-20');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`type`) values (1,'admin','admin','admin');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notid` int(11) NOT NULL AUTO_INCREMENT,
  `notcontent` varchar(100) DEFAULT NULL,
  `notdate` date DEFAULT NULL,
  `expirydate` date DEFAULT NULL,
  PRIMARY KEY (`notid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notid`,`notcontent`,`notdate`,`expirydate`) values (2,'evurrunremk','2019-12-21','2019-12-25'),(4,'election hai\r\n                ','2019-12-31','2020-02-29');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `postid` int(11) NOT NULL AUTO_INCREMENT,
  `postname` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`postid`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `post` */

insert  into `post`(`postid`,`postname`) values (6,'chairman'),(5,' p2'),(7,'asdhbds'),(8,'asdsd'),(9,'asdsd'),(10,' ertge');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stuid` int(11) NOT NULL AUTO_INCREMENT,
  `stuname` varchar(50) NOT NULL,
  `admno` int(11) DEFAULT NULL,
  `courseid` int(11) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `guardian` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phoneno` varchar(12) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`stuid`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stuid`,`stuname`,`admno`,`courseid`,`semester`,`gender`,`guardian`,`dob`,`phoneno`,`email`) values (8,'faiz',123,7,4,'MALE','asad','2020-04-02','9946071470','Noneagadvs@gmail.com'),(6,'arsh',2222,10,6,'FEMALE','asgvsd','2019-12-14','513513513','Noneagadvs@gmail.com'),(7,'asdsd',51321,8,2,'FEMALE','asds','2019-12-20','51651615','faizki@gmail.com');

/*Table structure for table `winner` */

DROP TABLE IF EXISTS `winner`;

CREATE TABLE `winner` (
  `winnerid` int(11) NOT NULL AUTO_INCREMENT,
  `stuid` int(11) DEFAULT NULL,
  `postid` int(11) DEFAULT NULL,
  `yearfrom` varchar(6) DEFAULT NULL,
  `yearto` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`winnerid`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `winner` */

insert  into `winner`(`winnerid`,`stuid`,`postid`,`yearfrom`,`yearto`) values (3,6,7,'6626','1211'),(4,6,10,'6626','1900');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
