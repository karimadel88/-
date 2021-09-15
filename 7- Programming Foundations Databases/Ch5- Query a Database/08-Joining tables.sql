SELECT FirstName,LastName,FavDish, Dishes.`Name` FROM Customers;
JOIN Dishes ON Customers.FavDish=Dishes.DishID;
ORDER BY Reservations.`Date`;

