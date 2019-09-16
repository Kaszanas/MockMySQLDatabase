# Calculating the window between which we can say that the User first registered and the last time User was active.

SET @userID = '';
SET @num  = 1;

SELECT avg(datediff) as Lifetime FROM
(SELECT userID, DATEDIFF(max(eventDate), min(eventDate)) as datediff FROM
(SELECT *,
@num := if(@userID = userID, @num + 1, 1) as row_no,
@userID := userID as dummy FROM
(SELECT own_id, userID, eventName, price, eventDate
FROM YourDatabase.`table` ORDER BY userID, eventDate ASC, own_id ASC)DerivedTable)DerivedTable1 GROUP BY userID)DerivedTable2;