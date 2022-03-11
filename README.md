# soccer-league-table
A command-line tool that can read in information about games played and write out a proper league table

Unfortunately I was doing this on a windows system and had to use about 15 minutes to set up git bash/pytest in my environment. As long as your environment can run python and has pytest installed, there shouldn't be anything else required to run this. 

There may be an issue in the repo where newlines in the file were replaced with windows newlines (\r\n?), and I haven't had a chance to test it on a linux system. I might have misconfigured git when installing.

I initially wrote out some pretty straightforward functions using lists/dicts to spit out a properly-formatted table, just to have something working, and once I got there I went back to make things a little cleaner and more object-oriented (using the LeagueTable and Team classes). I think that classes here are a much better approach especially should things need to expand in the future - for example, whether to also count GF/GA and sort the table accordingly - and it provides some greater control over what is made available to an end user or application. On that note, though, I think there some optimizations that could be made.

First, I don't have any checking to actually make sure that the correct arguments are used or that the file exists. This is as simple as adding a flag to the argparser and using a try-except block when reading in the file. 

Second, I think that this would not be able to handle massive datasets well in terms of file I/O. I'm reading in all of the lines at once into memory.

Third, and I don't think it is necessarily a problem in this application, but when adding points results this makes a comparison with every team already present. For soccer, it's probably fine since there are usually no more than 30 or so teams, but if you were using this for an online chess leaderboard with thousands of users, you'd probably want to make this better. I think that using a dictionary instead of a list for teams would give us better complexity on access.

Finally, I think that adding in sorted order would prevent us unnecessarily sorting the list of teams over and over per call to __str__, but since this application prints and exits, there is no specific difference here. if this was something that was persistent and queried for a table, I think that this change would be much more important.

I also would want to add far more tests with different inputs. I did some poking around online to see if I could get some similar data for the premier league, but I couldn't immediately find anything. the general infrastructure for the pytest suite is there though.

Hope this is enough! usage is here:

python3 main.py -i/--input-file <relative-path-to-input>


