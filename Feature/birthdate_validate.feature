@validate_bd

Feature: Test case to validate the birth date user enters.

Scenario Outline: Validate birth date of user
	Given User access website homepage
	When user enters birth month as <month>
	When user enters birth day as <day>
	When user enters birth year as <year>
	Then validate action as per <expected_output>

	Examples:
	|month	|day	|year	|expected_output	|
	#Validate Data
	|12     |12     |1987	|valid				|
	#invalid month
	|13		|12		|1987	|invalid_month		|
	#Invalid Day
	|12  	|32 	|1987	|invalid_day		|
	#invalid_year
	|30     |12		|0001	|invalid_year		|
	#Invalid Year-less than 18
	|12   	|12	    |2020	|invalid_message	|
	#Invalid Year-More than 100 years
	|12		|12		|1800	|invalid_message	|
	#Leap year-Invalid Day for month of Feb
	|02     |30		|2000	|invalid_day		|
	#Leap year- Valid Day for month of Feb
	|02     |29  	|2000	|valid				|
	#Non leap year-Invalid day for month of Feb
	|02		|30		|1999   |invalid_message	|
	#Valid-Month with 31 days
	|01     |31     |1999   |valid				|
	#Valid-Month with 30 days
	|03     |30     |1999   |valid			    |
	#Invalid-Months with 30 days
	|04     |31     |1999   |invalid_day		|

Scenario: User navigates via page URL without date validation
	Given User access website homepage
	When user tries to navigate via URL
	Then User should be navigated back to gateway