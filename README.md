# Feedbro-to-NewPipe
 Replaces subscriptions from [NewPipe](https://newpipe.schabi.org/) with those exported by [Feedbro](https://nodetics.com/feedbro/).  

Basically I don’t really care to use an account for watching YouTube, so I use [Feedbro](https://nodetics.com/feedbro/) as a Firefox addon on my desktop and [NewPipe](https://newpipe.schabi.org/) on my Android. To synchronize my “subscriptions” between them, I created this little script.  

*Warning:* This is a one way synchronization from [Feedbro](https://nodetics.com/feedbro/) to [NewPipe](https://newpipe.schabi.org/). The current version doesn’t try to merge subscriptions and you cannot synchronize from [NewPipe](https://newpipe.schabi.org/) to [Feedbro](https://nodetics.com/feedbro/). Maybe I will add this in the future, but right now this is simply not my use case.  

(Sidenote: I used to use [YouTube Checker](https://github.com/XrXr/YoutubeSubscriptionChecker), but lately it failed to download subscriptions due to deactivation of the API key. Since I don’t want to add my own API key, I’ve now switched.)  

# Dependencies
Python3 for the Python version

# Usage
`./feedbro_to_newpipe.py Feedbro-Subscriptions.opml NewPipe-Subscriptions.json`  

A new file will be created with subscriptions from [Feedbro](https://nodetics.com/feedbro/).  
After running this script, import the JSON file to replace your subscriptions.  

Steps to export [Feedbro](https://nodetics.com/feedbro/) subscriptions:
1. Open Feedbro
2. Go to the settings
3. Click the “Export as OPML” button
(You don’t need to filter for YouTube channels, the script will automatically extract them.)  

Steps to import [NewPipe](https://newpipe.schabi.org/) subscriptions
1. Go to your subscriptions
2. Click on Import/Export
3. Select import from YouTube export and select NewPipe-Subscriptions.csv.
