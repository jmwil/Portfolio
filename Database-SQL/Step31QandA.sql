-- #1 How many copies of the book titled The Lost Tribe are owned by the library branch whose name is "Sharptown"?--

SELECT * FROM TBLBOOK AS B JOIN TBLBOOKCOPIES AS C
ON B.BOOKID =C.bookid
JOIN tbllibrarybranch AS LB
ON C.BRANCHID=LB.BRANCHID
WHERE B.title = 'The Lost Tribe'
AND LB.BRANCHNAME = 'Sharpstown'


-- #2 How many copies of the book titled The Lost Tribe are owned by each library branch?--

SELECT * FROM TBLBOOK AS B JOIN TBLBOOKCOPIES AS C
ON B.BOOKID =C.bookid
JOIN tbllibrarybranch AS LB
ON C.BRANCHID=LB.BRANCHID
WHERE B.title = 'The Lost Tribe'

-- #3 Retrieve the names of all borrowers who do not have any books checked out. --

select * from tblborrower as B left outer join tblbookloans as L
on B.cardno = L.cardno
where l.cardno IS NULL


-- #4 For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today, retrieve the book title, the borrower's name, and the borrower's address ---

select A.title, C.name, C.[address]
from tblbookloans as B join tbllibrarybranch as L
on B.branchid = L.branchid
join tblbook as A on A.bookid = b.bookid
join tblborrower as C on c.cardno = B.cardno
where L.branchName = 'Sharpstown' and B.duedate = '2016-02-20'

-- #5 for each library branch, retrieve the branch name and the total number of books loaned out from that branch. --


DECLARE @name varchar(30)
SET @name = 'Central'

select COUNT(bl.bookid) AS BooksOnLoan
from tbllibrarybranch as B join tblbookloans as bl
on B.branchid=bl.branchid
where b.branchname = @name

-- see the stored procedure below for each individual branch name...--

--#6 Retrieve the names, addresses, and number of books checked out for all borrowers who have more than five books checked out.

DECLARE @COUNT INT 
set @COUNT = (SELECT COUNT(l.cardno)
FROM TBLBORROWER AS B JOIN TBLBOOKLOANS AS L
ON B.CARDNO = L.CARDNO)

SELECT B.name, B.[address], @COUNT AS LOANS
FROM TBLBORROWER AS B JOIN TBLBOOKLOANS AS L
ON B.CARDNO = L.CARDNO
where @COUNT > 5
GROUP BY B.NAME, B.[ADDRESS]

--#7 For each book authored 9or co-authored) by "Stephen King', retrieve the title and the number of copies owned by the library branch whose name is "Central"


select C.noofcopies, B.title from tblbookcopies as C join tbllibrarybranch as LB
on c.branchid = lb.branchid
join tblbook as B on b.bookid = C.bookid
join tblbookauthors AS a on b.bookid = a.bookid
WHERE lb.branchname = 'central'
and A.AUTHORNAME='Stephen King'


-- #8 create a stored procedure that will execute one or more of those queries based on user choice --

CREATE PROC HR_BooksOnLoanByBranchName @branch varchar(30)
AS

select COUNT(bl.bookid) AS BooksOnLoan
from tbllibrarybranch as B join tblbookloans as bl
on B.branchid=bl.branchid
where b.branchname = @branch
GO

EXEC HR_BooksOnLoanByBranchName 'Multnomah'