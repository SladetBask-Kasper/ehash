# ehash (ExtraHASH)
ehash is a class which takes a password and creates a hash of that password, and then hashes the hash of that password.
This makes it so that bute-forcing a password list can take really long, Example, Lets say that I have a list of passwords and a list of salts, I know how to use the salts to get the correct password, but I also know that the the site uses something like ehash, To get the password, I need to hash it a bunch of times, and this can add up to a second! And if you on top of that are going to look igenom 
