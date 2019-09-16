# Calculating 7D retention of Users.

SET @userID = '';
SET @num  = 1;

SELECT min_date, sum(UserStayed)/count(DerivedTable2.UserStayed) AS 7DRetention FROM
(SELECT userID, min(eventDate) as min_date, IF(DATEDIFF(max(eventDate), min(eventDate))>=7,1,0) as UserStayed FROM
(SELECT userID, eventDate,
@num := if(@userID = userID, @num + 1, 1) as row_no,
@userID := userID as dummy FROM
(SELECT userID, eventDate
FROM YourDatabase.`table` ORDER BY userID, eventDate ASC, own_id ASC)DerivedTable)DerivedTable1 GROUP BY userID ORDER BY min_date)DerivedTable2 GROUP BY min_date;