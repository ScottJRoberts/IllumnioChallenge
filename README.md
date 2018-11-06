# Illumio Take Home Coding Challenge
By Scott Roberts

## Design Decisions

 I decided to store the rules in a nested dictionary data structure, seemed logically appropriate for buidling a quasi waterfall of references. Besides personal understanding, the main benefit is fast look up times. I also made the decision to store ports as strings to easily capture ranges. The downside to storing ports as strings is that I have to convert them into integers for comparing on ranges. I also decided to treat ranges of IP addresses and ports as boundaries instead of storing every possibilty. This saves on space and write time, especially with edge cases like all IP addresses. However, it comes at the cost of the fastest possible reads, since it has to do some processing instead of a constant lookup. If the rules were not ever changing I would've considered doing the preprocessing up front to optimize those reads, but that's a large assumption. 

## Testing Solution

I started with the base cases given in the exercise and then expanded testing for edge cases. I tried to include positive and negative test cases that tested all boundaries. I even added some for bad input. After this I moved into the special cases of every possible port and IP address, I didn't have time to test every port and every IP address though.

## Improvements

To clean up the interface more I would create an IP address class to initialize the IP address and  hold all of the comparator methods. I think this provides more longevity down the road because if we wanted to switch from IPv4 to IPv6 it would be easier. We could also add validators to ensure that every IP address fit within a criteria, this would protect us from an invalid IP address making its way into a rule and then that invalid IP address getting through our firewall and causing errors. 

The same idealogy could be applied to ports as well, to allow for a future where a greater range of ports could be supported without changing any business logic. 

I also would've built an actual test suite with a proper script, instead of just a quick and dirty trials. This way I could test more data points at random in between and outside of IP/port ranges, providing more insight on edge cases and overall performance. I also didn't test the effect of having a blank CSV. 

Speaking of I think the way I'm extracting text from the CSV and formatting it to my needs is a little crude and could be improved. For example, if you don't include a blank line at the end it will pull off the last character of the last line. I noticed this later on in the process and decided there were more important tasks to do. 

## Teams

All of the teams sound like they provide great places to have impact on an awesome field of Cyber Security, I'd be happy to work with any of them.

 1. Platform: 
 I've always been interested in distributed systems and would love to learn more. It seems to me like these problems are necessary and fun to fix
 
 2. Data:
 Understanding customers and applying that knowledge to extend data beyond patterns into insights is where the future is. I'm enamored with the hard question of how to provide tools and the infrastrucure to enable people to do more than they could before.
 
 3. Policy
 This team seems like it gets to do a great mix of a lot of things and seems like a great environment to learn a lot about different areas of the product. 
 
 
 Thanks so much for your consideration!
 


