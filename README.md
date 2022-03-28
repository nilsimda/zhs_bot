## Requirements
You need to have python3, selenium, chrome and and a chromedrive installed on you system.

## Usage
The following is an example of how to use the bot. It will reserve a spot for you in all available courses
including freies Spiel for the given sport. It requires that you have saved your ZHS Data with a password.
The Sportart has to be given exactly as on the ZHS Website.
```
from ZHS_Bot import ZHS_Bot

bot = ZHS_Bot("your_username", "your_password")
bot.reserve("Sportart")
```
