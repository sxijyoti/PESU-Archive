Use University_Fest;

-- Q1
SELECT DISTINCT p.Name AS Participant_Name
FROM Participants p
JOIN Registration r ON p.SRN = r.SRN
JOIN Event e ON r.Event_ID = e.Event_ID
WHERE e.Price > (
    SELECT AVG(Price)
    FROM Event
);

-- Q2
SELECT e.Event_name, COUNT(r.SRN) AS Total_Registrations
FROM Event e
JOIN Registration r ON e.Event_ID = r.Event_ID
GROUP BY e.Event_ID, e.Event_name
HAVING COUNT(r.SRN) > (
    SELECT AVG(reg_count)
    FROM (
        SELECT COUNT(SRN) AS reg_count
        FROM Registration
        GROUP BY Event_ID
    ) AS avg_reg
);

-- Q3
SELECT DISTINCT p.Name AS Participant_Name, e.Event_name, e.Price
FROM Participants p
JOIN Registration r ON p.SRN = r.SRN
JOIN Event e ON r.Event_ID = e.Event_ID
WHERE e.Price = (
    SELECT MAX(Price) FROM Event
);

-- Q4
SELECT si.Stall_ID, si.Item_name, si.Price_per_unit
FROM Stall_items si
WHERE si.Price_per_unit < (
    SELECT AVG(s2.Price_per_unit)
    FROM Stall_items s2
    WHERE s2.Item_name = si.Item_name
);

-- Q5
SELECT 
    p.SRN,
    p.Name,
    COUNT(DISTINCT pur.Timestamp) AS Purchases_Made,
    SUM(pur.Quantity) AS Total_Quantity,
    RANK() OVER (ORDER BY SUM(pur.Quantity) DESC) AS Purchase_Rank
FROM Participants p
JOIN Purchased pur ON p.SRN = pur.SRN
GROUP BY p.SRN, p.Name;

-- Q6
SELECT 
    p.Department,
    p.Name AS Participant_Name,
    COUNT(r.Event_ID) AS Total_Events,
    RANK() OVER (PARTITION BY p.Department ORDER BY COUNT(r.Event_ID) DESC) AS Dept_Rank
FROM Participants p
JOIN Registration r ON p.SRN = r.SRN
GROUP BY p.Department, p.Name;

-- Q7
ALTER TABLE Event ADD FULLTEXT(event_name);

SELECT 
    Event_ID,
    Event_name,
    MATCH(Event_name) AGAINST('Tournament' IN NATURAL LANGUAGE MODE) AS Relevance
FROM Event
WHERE MATCH(Event_name) AGAINST('Tournament' IN NATURAL LANGUAGE MODE)
ORDER BY Relevance DESC;

-- Q8

ALTER TABLE Stall_items ADD COLUMN Item_desc VARCHAR(200);
UPDATE Stall_items SET Item_desc = Item_name;
ALTER TABLE Stall_items ADD FULLTEXT(Item_desc);


SELECT 
    s.Stall_ID,
    s.Name AS Stall_Name,
    SUM(si.Total_quantity) AS Total_Stock
FROM Stall s
JOIN Stall_items si ON s.Stall_ID = si.Stall_ID
WHERE MATCH(si.Item_desc) AGAINST('chicken soup' IN NATURAL LANGUAGE MODE)
GROUP BY s.Stall_ID, s.Name;

