select firstname, lastname, city, state 
from person
Left join Address on person.personId = Address.personId
