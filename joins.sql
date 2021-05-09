-- Pull account balances in a join statement

Select account_id, checking_balance
From Accounts A
Inner Join Banking B
Where A.account_id = B.account_id 


-- Select all employees that are not in the departments table
Select id,name 
from Employees E
Left join Departments D
where D.id is NULL

