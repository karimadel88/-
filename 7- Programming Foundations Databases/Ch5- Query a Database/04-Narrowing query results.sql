SELECT FirstName,LastName,State FROM Customers WHERE State="CA" OR State="EG";

SELECT FirstName,LastName,State FROM Customers WHERE State="CA" LIKE "C%; # %->all starting by c

SELECT CustomerID,FirstName,LastName,State FROM Customers WHERE FirstName="Taylor";

SELECT * FROM Reservations WHER `Date` > "2019-02-06" AND `DATE` < "2019-02-07";
