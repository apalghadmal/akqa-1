@validate_bd

Feature: Test case to validate the birth date user enters.

Scenario Outline: Validate birth date of user
	Given User access website homepage
	When user enters birth month as <month>
	When user enters birth day as <day>
	When user enters birth year as <year>
	Then validate action as per <action>

	Examples:
	|month	|day	|year	|action			|
	#Validate Data
	|12     |12     |1987	|Validate Date	|
	#invalid month
	|13		|12		|1987	|				|
	#Invalid Day
	|12  	|32 	|1987	|				|
	#Invalid Year-less than 18 years
	|12   	|12	    |2020	|				|
	#Invalid Year-More than 100 years
	|12		|12		|1800	|	      		|
	#Leap year-Invalid Day for month of Feb
	|02     |30		|2000	|				|
	#Leap year- Valid Day for month of Feb
	|02     |29  	|2000	|				|
	#Non leap year-Invalid day for month of Feb
	|02		|30		|1999   |				|
	#non numeric values for Month day and Year
	|abc    |30     |1999   | 				|
	|02		|pdf    |1999   |			    |
	|01     |20    	|ABCD   |				|
	#Valid-Month with 31 days
	|01     |31     |1999   |    |
	#Valid-Month with 30 days
	|03     |30     |1999   |    |
	#Invlaid-Months with 30 days
	|04     |31     |1999   |    			|
