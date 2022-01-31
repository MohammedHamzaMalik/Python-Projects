import requests

# account credentials
username = "o_3v0ulxxxxx"
password = "your_password_here"


'''
the username is the account name I just showed you how to get it, the password is the actual 
password of your Bitly account, so you should replace them with your credentials.

If you read the Bitly API documentation carefully, you'll see that we need an access token to 
make API calls to get the shortened URL, so let's create a new access token:
'''

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()


'''
We used requests.post() method to make a POST request to /oauth/access_token endpoint and 
obtain our access token. We passed auth parameter to add our account credentials to the request 
headers.

Now we have our access token, before we dive into shortening URLs, we first need to get the 
group UID associated with our Bitly account:
'''

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()


# Now that we have guid, let's make our request to shorten an example URL:
# the URL you want to shorten
url = "https://www.thepythoncode.com/topic/using-apis-in-python"
# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)


'''
We're sending a POST request to /v4/shorten endpoint to shorten our url, we passed the 
group_guid of our account and the url we want to shorten as the body of the request.

We used json parameter instead of data in requests.post() method to automatically encode our 
Python dictionary into JSON format and send it with Content-Type as application/json, we then 
added the headers to contain the authorization token we grabbed earlier. Here is my output:
'''

# Output: Shortened URL: https://bit.ly/32dtJ00