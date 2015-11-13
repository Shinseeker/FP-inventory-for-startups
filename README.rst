#########################
FP-inventory-for-startups
#########################


Pretty much all companies depend on inventory to operate or fill client orders.
Inventory is a major asset that helps a company with tasks such as 
planing or staying within a budget. However, there are many startups out 
there that does not take great inventory, and suffe because of it. They need a software that
can store inventory and modify it to benefit both their business and their clients.

#########
Personas:
#########

Adam
=====

Adams recently opened up his garage called Project M-spec. He has many auto parts in 
his garage, he is lost keeping track of all the equipment.Instead of using a 
spreadsheet he wants a simple program that stores his inventory more efficiently. 
This program will make it easier for him to see how many parts he has in his 
garage and what parts he can use, so that he can best serve his clients.

Details
=======
With this program Adam can see how many parts he has in his garage, and 
what parts he can use. This way he can best serve his clients and charges them 
accordingly depending what part and the instaliation.

Goals
=====
- locate how many parts he has in inventory.

- get the price of each part

- add/remove parts from the inventory.

- produce an estimate of installtion of some of the parts.

Problem Scenario:
=================

Project M-spec is a star-up business. They dont have all the tools needed to
keep track of all the inventory that comes in. Having a basic excel
spreadsheet to record the inventory is not good enough.

Current Alternatives:
=====================
Adam's current alternatives is hiring extra staff to help manage his inventory, 
or implement a small scale CRM to help manage his clients and his invetory. 
If he does so it would cost him thousands of dollars a year. Money he needs to 
invest in his startup.

Value Proposition
=================
This inventory software will save him thousands of dollars. Money he will 
need to invest in more parts and mechanics.With this software it easy to 
track, manage, and profit off the inventory. 

User Stories:
=============
As Adam, I would want to modify my inventory so i can locate each part. 
After modfying the inventory,I would look into creating an estimate for the client 
depending on what part i have. The estimate will come with the additional cost of labor.

Acceptance Stories
^^^^^^^^^^^^^^^^^^
-Scenario: 1-
`````````````
Adding Auto parts into inventory:
````````````````````````````````````````````    
Given that I recieve new auto parts on a daily basis.
I Would immidetaley put items into inventory.

When selecting 1 I can enter in a 
new item, along with it I can enter
additional information about it.

Then the info would be stored in the database. 

-Scenario: 2-
`````````````
Removing auto parts from inventory:
`````````````````````````````````````````````
Given that the customers come into the garage,and
purchase auto parts like tires, rims and shocks, it needs
to be taken off the database. 

When the item is finally purchased i would remove it
from the database.

Then I can press 2 to remove it from the inventory.

-Scenario: 3-
`````````````
Shows one item:
`````````````````````````````
Given that a customer comes into the garage
looking for a particular item to be installed.

And I can search in the database to instantly check the 
price of the item for that customer, and give them a quote. 

When pressing 3 I can access that 1 particular record.
And then I can charge them accordingly.

-Scenario: 4-
`````````````
Shows all info!
````````````````
Given that I have to view multiple items at a time to see
what i got,

And I have to search for the item in my inventory to
look up prices, This way i know what I have in stock.

When i choose option 4 it will show all items.
And inclue all the details.
