# The query below is calculating an average second transaction performed by a User.

SET @userID = '';
SET @num  = 1;

SELECT avg(price) FROM
(SELECT userID, price,
@num := if(@userID = userID, @num + 1, 1) as row_no,
@userID := userID as dummy FROM
(SELECT userID, eventName, price
FROM YourDatabase.`table` WHERE eventName = 'Performed-Transaction' ORDER BY userID)DerivedTable)DerivedTable1 WHERE DerivedTable1.row_no = 2;