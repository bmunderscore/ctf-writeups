# Pipeline Problems
# Gitea actions runner hijacking?
## I recommend watching this video about CI/CD hacking: https://www.youtube.com/watch?v=fcibOy-zoN8

We were first presented with a swagger UI containing different API endpoints that you could test.

If you visit /source, it brings you to a gitea server (http://git.hackmeto.win)

Step 2: registration is enabled (disabled by default) and you can explore public repositories, where you would find the admin's repo with the API source code as well as a CI/CD pipeline demo.yaml file.

Step 3: migrate that repository into your own (not forking because it explicitly said not to fork lmao)

Step 4: In repo settings, enable Actions on your new repo, and you'll be able to see that there are a few runners available (which do not belong to us).

Step 5: However, once you have actions enabled and you make a change such as a file commit (editing demo.yaml), it will trigger the action and start running your code with one of the available runners.

Step 6: How to get the flag? As we saw in the api source, the endoint for getting flag is whitelisted to an IP range of 10.0.0.0/24. I thought it was safe to assume that these runners might also be on the same network

Step 7: In the network endpoint, we can identify the local IP of the server, which is 10.0.0.9. Let's try to make the runner send a request to that endpoint.

Step 8: In demo.yaml, add a line with the command:
`echo $(curl http://10.0.0.9:8000/get_flag)`

Step 9: Make the commit, then go to the actions tab and inspect the runner logs. The curl output should show up somewhere, containing the flag.
