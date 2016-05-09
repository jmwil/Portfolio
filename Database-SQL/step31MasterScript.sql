--RUN THIS SCRIPT FOR THE SQL DRILL, ITEM 33 OF 43--

use master

IF EXISTS (SELECT * FROM SYS.SYSDATABASES WHERE [NAME] = 'BookStuff')
DROP DATABASE BookStuff
GO

CREATE DATABASE BookStuff
GO

USE BookStuff
GO

Create TABLE tblBook
(BookId INT PRIMARY KEY,
Title VARCHAR(30) NOT NULL,
PublisherName VARCHAR(30) NOT NULL)

INSERT INTO tblBook
Values (1, 'The Lost Tribe', 'Random House'),
(2, 'Intro to SQL', 'Nerd Alert'),
(3, 'Intro to HTML', 'Nerd Alert'),
(4, 'Intro to CSS', 'Nerd Alert'),
(5, 'Zombie Cats', 'Apocalypse Now Publishing'),
(6, 'Zombie Cats 2', 'Apocalypse Now Publishing'),
(7, 'Ice Cream Frenzy', 'Food Junkies Inc'),
(8, 'Jelly Been Bonanzan', 'Food Junkies Inc'),
(9, 'I Love Food', 'Food Junkies Inc'),
(10, 'Zetus Lapetus', 'Zenon Carr'),
(11, 'Zomg', 'Zenon Carr'),
(12, 'Falling Off a Cliff', 'Random House'),
(13, 'Don''t Talk to Me', 'Random House'),
(14, 'Why Am I Crying?', 'Random House'),
(15, 'All My Friends Are Dead', 'Apocalypse Now Publishing'),
(20, 'I <3 Technology', 'Nerd Alert')

CREATE TABLE tblBookAuthors
(
BookId INT PRIMARY KEY,
AuthorName VARCHAR(50) NOT NULL,
)

INSERT INTO tblBookAuthors
VALUES (1, 'Aaron Fitzgerald'),
(2, 'Alex Page'),
(3, 'Miles Fletcher'),
(4, 'Stephen King'),
(5, 'Lorraine Rose'),
(6, 'Leslie Hering'),
(7, 'Paige Stefani'),
(8, 'Matt Bordonaro'),
(9, 'Brian Getman'),
(10, 'Marcia Walsh'),
(11, 'Mark Nuss'),
(12, 'Peter Sanders'),
(13, 'Mark Branlund'),
(14, 'Mark Branlunh'),
(15, 'Brian Getman'),
(16, 'Lesle Hering'),
(17, 'Marcia Walsh'),
(18, 'Paige Stefani'),
(19, 'Chris Ingraham'),
(20, 'Jimmy Wilcox')


CREATE TABLE tblPublisher
(Name Varchar(30) PRIMARY KEY,
[Address] Varchar(30) not null,
Phone int)

INSERT INTO tblPublisher
values ('Random House', '2758 NE Where St', 4447898),
('Nerd Alert', '580 Couch St', 5553938),
('Apocalypse Now Publishing', '000 Nowhere Lane', 2958438),
('Food Junkies Inc', '875 Food Ave', 8887777),
('Zenon Carr', '48 Fute St', 4442222)

CREATE TABLE tblLibraryBranch
(
BranchID int PRIMARY KEY,
BranchName varchar(30) not null,
[Address] varchar(30) not null)

INSERT INTO tblLibraryBranch
Values (1, 'Central', '42 SW 10th'),
(2, 'Sharpstown', '593 NW 58th'),
(3, 'Multnomah', '29 SW Hillsdale Hwy'),
(4, 'Nopo', '5234 N Killingsworth'),
(5, 'Luxury', '13 NW Lovejoy')

CREATE TABLE tblBookCopies
(
BookId int,
BranchID int,
NoOfCopies int,
PRIMARY KEY (bookId, BranchID)
)

INSERT INTO tblBookCopies
VALUES (1, 1, 3),
(1,2,4),
(1,3,2),
(1,4,5),
(1,5,19),
(2,1,2),
(2,2,5),
(2,3,2),
(2,4,3),
(2,5,6),
(3,1,2),
(3,2,2),
(3,3,3),
(3,4,3),
(3,5,6),
(4,1,2),
(4,2,2),
(4,3,4),
(4,5,5),
(5,1,2),
(5,2,3),
(5,3,2),
(5,4,3),
(5,5,3),
(6,1,2),
(6,2,3),
(6,3,2),
(6,4,3),
(6,5,2),
(7,1,2),
(7,2,3),
(7,3,2),
(7,4,3),
(7,5,2),
(8,1,2),
(8,2,2),
(8,3,3),
(8,4,2),
(8,5,3),
(9,1,2),
(9,2,2),
(9,3,2),
(9,4,2),
(10,1,2),
(10,2,2),
(10,3,2),
(10,4,2),
(10,5,2),
(11,1,2),
(11,2,2),
(11,3,2),
(11,4,2),
(11,5,2),
(12,1,2),
(12,2,2),
(12,3,2),
(12,4,2),
(12,5,2),
(13,1,2),
(13,2,2),
(13,3,3),
(13,4,2),
(13,5,2),
(14,1,2),
(14,2,2),
(14,3,2),
(14,4,2),
(14,5,2),
(15,1,2),
(15,2,2),
(15,3,4),
(15,4,3),
(15,5,2),
(16,1,2),
(16,2,2),
(16,3,2),
(16,4,2),
(16,5,2),
(17,1,2),
(17,2,2),
(17,3,2),
(17,4,2),
(17,5,4),
(18,1,2),
(18,2,2),
(18,3,2),
(18,4,3),
(18,5,2),
(19,1,2),
(19,3,2),
(19,2,3),
(19,4,2),
(19,5,2),
(20,1,2),
(20,2,2),
(20,3,2),
(20,4,2),
(20,5,2)



CREATE TABLE tblBorrower
(
CardNo int Primary key,
Name varchar(30) not null,
[Address] varchar(30) not null,
Phone int not null,
)

INSERT INTO tblBorrower
VALUES (1, 'John', '123 NW Hopscotch ln', 2924229),
(2, 'Sally', '126 NW Hopscotch ln', 4448888),
(3, 'Sam', '123 NW Hopscotch ln', 2229999),
(4, 'Seth', '427 NW Hopscotch ln', 3337878),
(5, 'Raja', '542 NW Hopscotch ln', 5549878),
(6, 'Katrina', '473 NW Hopscotch ln', 5783322),
(7, 'Alli', '442 NW Hopscotch ln', 4789382),
(8, 'Eva', '442 NW Hopscotch ln', 4789383)



CREATE TABLE tblBookLoans
(
BookID int,
BranchID int,
CardNO int,
DateOut date,
DueDate date,
PRIMARY KEY (BookID, BranchID, CardNO)
)

INSERT INTO tblBookLoans
VALUES (1,1,1, '2016-01-28', '2016-02-20'),
(1,5,1, '2016-01-28', '2016-02-20'),
(1,5,2, '2016-01-28', '2016-02-20'),
(1,5,4, '2016-01-28', '2016-02-20'),
(1,5,5, '2016-01-28', '2016-02-20'),
(1,5,6, '2016-01-28', '2016-02-20'),
(1,5,7, '2016-01-28', '2016-02-20'),
(1,5,8, '2016-01-28', '2016-02-20'),
(2,2,8, '2016-01-28', '2016-02-20'),
(3,1,8, '2016-01-28', '2016-02-20'),
(4,1,8, '2016-01-28', '2016-02-20'),
(5,1,8, '2016-01-28', '2016-02-20'),
(6,1,8, '2016-01-28', '2016-02-20'),
(7,1,8, '2016-01-28', '2016-02-20'),
(8,1,8, '2016-01-28', '2016-02-20'),
(2,2,7, '2016-01-28', '2016-02-20'),
(3,2,7, '2016-01-28', '2016-02-20'),
(4,2,7, '2016-01-28', '2016-02-20'),
(5,2,7, '2016-01-28', '2016-02-20'),
(6,2,7, '2016-01-28', '2016-02-20'),
(14,2,7, '2016-01-28', '2016-02-20'),
(17,2,7, '2016-01-28', '2016-02-20'),
(1,4,1, '2016-01-28', '2016-02-20'),
(2,4,1, '2016-01-28', '2016-02-20'),
(3,4,1, '2016-01-28', '2016-02-20'),
(15,4,1, '2016-01-28', '2016-02-20'),
(16,4,1, '2016-01-28', '2016-02-20'),
(17,4,1, '2016-01-28', '2016-02-20'),
(18,4,1, '2016-01-28', '2016-02-20'),
(19,4,1, '2016-01-28', '2016-02-20'),
(10,5,4, '2016-01-28', '2016-02-20'),
(11,5,4, '2016-01-28', '2016-02-20'),
(12,5,4, '2016-01-28', '2016-02-20'),
(13,5,4, '2016-01-28', '2016-02-20'),
(1,3,2, '2016-01-28', '2016-02-20'),
(2,3,2, '2016-01-28', '2016-02-20'),
(4,3,2, '2016-01-28', '2016-02-20'),
(5,3,2, '2016-01-28', '2016-02-20'),
(6,3,2, '2016-01-28', '2016-02-20'),
(7,3,2, '2016-01-28', '2016-02-20'),
(8,3,2, '2016-01-28', '2016-02-20'),
(9,3,2, '2016-01-28', '2016-02-20'),
(10,3,2, '2016-01-28', '2016-02-20'),
(11,3,2, '2016-01-28', '2016-02-20'),
(12,3,2, '2016-01-28', '2016-02-20'),
(13,3,2, '2016-01-28', '2016-02-20'),
(14,3,2, '2016-01-28', '2016-02-20'),
(15,3,2, '2016-01-28', '2016-02-20'),
(17,3,2, '2016-01-28', '2016-02-20'),
(18,3,2, '2016-01-28', '2016-02-20'),
(20,3,2, '2016-01-28', '2016-02-20')

--OMG YAY!!!--