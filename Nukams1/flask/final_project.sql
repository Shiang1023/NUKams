-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- 主機: localhost
-- 產生時間： 2024-06-14 07:10:28
-- 伺服器版本: 5.7.17-log
-- PHP 版本： 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `final_project`
--

-- --------------------------------------------------------

--
-- 資料表結構 `account`
--

CREATE TABLE `account` (
  `id` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `account`
--

INSERT INTO `account` (`id`, `password`, `usertype`) VALUES
('A1105501', '1111111', '1'),
('A1105502', 'ffffee', '0'),
('A1105503', 'wwdwdd', '3'),
('R1105501', 'rgrgr', 'grrggr'),
('R1105502', 'dwwwf', 'wfwwf'),
('R1105503', 'efefg', 'feffef'),
('R1105504', 'dwfgrgr', 'wfwf'),
('R1105505', 'adawd', 'egrgr');

-- --------------------------------------------------------

--
-- 資料表結構 `administrator`
--

CREATE TABLE `administrator` (
  `id` varchar(10) NOT NULL,
  `administrator_id` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` int(1) NOT NULL,
  `phone` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `administrator`
--

INSERT INTO `administrator` (`id`, `administrator_id`, `name`, `email`, `gender`, `phone`) VALUES
('R1105501', 'R1105501', '邱秋秋', 'Eddd@gmail.com', 1, '0900000000'),
('R1105502', 'R1105502', '一二三', 'Eddddwd@gmail.com', 0, '0961255426');

-- --------------------------------------------------------

--
-- 資料表結構 `advertisement`
--

CREATE TABLE `advertisement` (
  `ad_id` varchar(10) NOT NULL,
  `rent_id` varchar(10) NOT NULL,
  `ad_detail` varchar(100) NOT NULL,
  `picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `comment`
--

CREATE TABLE `comment` (
  `comment_id` varchar(10) NOT NULL,
  `id` varchar(10) NOT NULL,
  `post_id` varchar(10) NOT NULL,
  `comment_detail` varchar(10) NOT NULL,
  `picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `contract`
--

CREATE TABLE `contract` (
  `contract_id` varchar(10) NOT NULL,
  `rent_id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `contract_time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `landlord`
--

CREATE TABLE `landlord` (
  `id` varchar(10) NOT NULL,
  `landlord_id` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `phone` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `post`
--

CREATE TABLE `post` (
  `post_id` varchar(10) NOT NULL,
  `id` varchar(10) NOT NULL,
  `post_detail` varchar(100) NOT NULL,
  `picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `rent_information`
--

CREATE TABLE `rent_information` (
  `rent_id` varchar(10) NOT NULL,
  `build_year` int(10) NOT NULL,
  `build_type` int(1) NOT NULL,
  `address` varchar(20) NOT NULL,
  `rent_limitation` varchar(30) NOT NULL,
  `rent` int(10) NOT NULL,
  `landlord_id` varchar(10) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `publish_time` varchar(20) NOT NULL,
  `other_requirement` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `repair`
--

CREATE TABLE `repair` (
  `repair_id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `landlord_id` varchar(10) NOT NULL,
  `repair_detail` varchar(50) NOT NULL,
  `repair_response` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `grade` int(3) NOT NULL,
  `gender` int(1) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `home_address` varchar(30) NOT NULL,
  `home_phone` varchar(10) NOT NULL,
  `home_contact` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `student_accommodate`
--

CREATE TABLE `student_accommodate` (
  `student_id` varchar(10) NOT NULL,
  `grade` int(3) NOT NULL,
  `landlord_id` varchar(10) NOT NULL,
  `semester` int(1) NOT NULL,
  `rent` int(10) NOT NULL,
  `roommate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `id` varchar(10) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` int(1) NOT NULL,
  `level` varchar(20) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `office_address` varchar(20) NOT NULL,
  `office_phone` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `visit_detail`
--

CREATE TABLE `visit_detail` (
  `visit_id` varchar(10) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `date` varchar(10) NOT NULL,
  `detail` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`administrator_id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `advertisement`
--
ALTER TABLE `advertisement`
  ADD PRIMARY KEY (`ad_id`),
  ADD KEY `rent_id` (`rent_id`);

--
-- 資料表索引 `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`comment_id`),
  ADD KEY `post_id` (`post_id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `contract`
--
ALTER TABLE `contract`
  ADD PRIMARY KEY (`contract_id`),
  ADD KEY `rent_id` (`rent_id`),
  ADD KEY `student_id` (`student_id`);

--
-- 資料表索引 `landlord`
--
ALTER TABLE `landlord`
  ADD PRIMARY KEY (`landlord_id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`post_id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `rent_information`
--
ALTER TABLE `rent_information`
  ADD PRIMARY KEY (`rent_id`),
  ADD KEY `landlord_id` (`landlord_id`);

--
-- 資料表索引 `repair`
--
ALTER TABLE `repair`
  ADD PRIMARY KEY (`repair_id`),
  ADD KEY `landlord_id` (`landlord_id`),
  ADD KEY `student_id` (`student_id`);

--
-- 資料表索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `id` (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- 資料表索引 `student_accommodate`
--
ALTER TABLE `student_accommodate`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `landlord_id` (`landlord_id`);

--
-- 資料表索引 `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacher_id`),
  ADD KEY `id` (`id`);

--
-- 資料表索引 `visit_detail`
--
ALTER TABLE `visit_detail`
  ADD PRIMARY KEY (`visit_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- 已匯出資料表的限制(Constraint)
--

--
-- 資料表的 Constraints `administrator`
--
ALTER TABLE `administrator`
  ADD CONSTRAINT `administrator_ibfk_1` FOREIGN KEY (`id`) REFERENCES `account` (`id`);

--
-- 資料表的 Constraints `advertisement`
--
ALTER TABLE `advertisement`
  ADD CONSTRAINT `advertisement_ibfk_1` FOREIGN KEY (`rent_id`) REFERENCES `rent_information` (`rent_id`);

--
-- 資料表的 Constraints `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`post_id`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`id`) REFERENCES `account` (`id`);

--
-- 資料表的 Constraints `contract`
--
ALTER TABLE `contract`
  ADD CONSTRAINT `contract_ibfk_1` FOREIGN KEY (`rent_id`) REFERENCES `rent_information` (`rent_id`),
  ADD CONSTRAINT `contract_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);

--
-- 資料表的 Constraints `landlord`
--
ALTER TABLE `landlord`
  ADD CONSTRAINT `landlord_ibfk_1` FOREIGN KEY (`id`) REFERENCES `account` (`id`);

--
-- 資料表的 Constraints `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`id`) REFERENCES `account` (`id`);

--
-- 資料表的 Constraints `rent_information`
--
ALTER TABLE `rent_information`
  ADD CONSTRAINT `rent_information_ibfk_1` FOREIGN KEY (`landlord_id`) REFERENCES `landlord` (`landlord_id`);

--
-- 資料表的 Constraints `repair`
--
ALTER TABLE `repair`
  ADD CONSTRAINT `repair_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `repair_ibfk_2` FOREIGN KEY (`landlord_id`) REFERENCES `landlord` (`landlord_id`);

--
-- 資料表的 Constraints `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id`) REFERENCES `account` (`id`),
  ADD CONSTRAINT `student_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`);

--
-- 資料表的 Constraints `student_accommodate`
--
ALTER TABLE `student_accommodate`
  ADD CONSTRAINT `student_accommodate_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `student_accommodate_ibfk_2` FOREIGN KEY (`landlord_id`) REFERENCES `landlord` (`landlord_id`);

--
-- 資料表的 Constraints `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`id`) REFERENCES `account` (`id`);

--
-- 資料表的 Constraints `visit_detail`
--
ALTER TABLE `visit_detail`
  ADD CONSTRAINT `visit_detail_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`),
  ADD CONSTRAINT `visit_detail_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
