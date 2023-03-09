Postmortem Report: The DNS Blunder that Made My Website BIHUB
On January 13, 2023, I set out to create a website for my school work on .TECH DOMAIN. Everything was going smoothly until I hit a roadblock. The dreaded DNS configuration.

Now, I don’t know about you, but DNS sounds like something that should come with a warning label: “May cause headaches, dizziness, and bouts of frustration”. But I soldiered on, determined to figure it out.

Or so I thought.

Fast forward to February 25, 2023. I try to access my website and BAM! Error message: “The requested URL could not be retrieved”. I’m thinking, “What COULD BE WRONG”


The freaking error

After some sleuthing, I realized the root cause of the issue: I had set up my DNS records with the wrong IP address. Instead of pointing to the server that was recommended to me, I pointed it to my local machine. D’oh!

Postmortem Report: DNS Configuration Error on .TECH DOMAIN

Issue Summary:

Duration: The DNS configuration error occurred from 10 January to 25 February, 2023.

Impact: My website was now about as useful as a screen door on a submarine. It was inaccessible, unusable, and just plain frustrating. Not to mention i even failed my project — you can imagine how this is a pain!!!.

Root Cause: The root cause of the issue was that the DNS records were not configured with an A entry to point to the correct server. Instead, the website was set up on a local machine, which caused the website to be inaccessible.

Timeline:

10 January 2023: The website was set up on my local machine instead of the recommended server.
25 February 2023:I detected the DNS configuration error, and found that the root domain could not be retrieved.
Actions taken: I investigated the DNS records , and i found that an A entry was missing, causing the website to be inaccessible.
Misleading investigation/debugging paths: None.
Escalated to: The issue was escalated to my school work cause of the wrong DNS configuration.
Resolution: The issue was resolved by configuring the DNS records with an A entry to point to the correct server.
Root Cause and Resolution:

Root Cause: The root cause of the issue was that the DNS records were not configured with an A entry to point to the correct server.

Resolution: The issue was resolved by configuring the DNS records with an A entry to point to the correct server.

Corrective and Preventative Measures:

Things that can be improved/fixed: The process of setting up a website on a domain needs to be reviewed to ensure that DNS records are properly configured.
Tasks to address the issue:
Create a DNS configuration checklist (with helpful diagrams and pop-up tips!)
Double-check my work (with the help of a caffeine-fueled colleague)
Add monitoring to alert for any DNS errors or mis-configurations in the future.
Schedule periodic reviews to ensure that DNS records are up-to-date and properly configured.(Make use of my fellow internet gurus who would have alerted me the website being down!)
Seek help when unsure of the process(i didn’t even bother to find my peers — such a disappointment i am)
Monitor the website regularly to ensure it is functioning properly.
Keep calm and carry on (with a stash of chocolate nearby)
In conclusion, my DNS blunder was a cautionary tale of what happens when you don’t pay attention to the details. But with a little humor, a helpful checklist, and a stash of chocolate, I’m confident that I’ll avoid future disasters. Cheers to better DNS days ahead!
