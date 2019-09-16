# The query below outputs UserIDs for all the Users that that turned on the Program at least 10 times.

SELECT userID FROM
(SELECT userID, count(eventName) AS eventCount FROM
(SELECT userID, eventName FROM 
(SELECT userID, eventName FROM YourDatabase.`table` WHERE eventName = 'New-User' or eventName = 'Program-Turned-On')DerivedTable)DerivedTable1 
GROUP BY userID)DerivedTable2 WHERE eventCount >= 10;