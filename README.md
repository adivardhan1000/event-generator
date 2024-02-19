# event-generator
Custom prompt for GPT4 wrapped in flask to generate .ics files event files based on text.

**Published at**: https://ics-generator.adivardhan.tech/
Note: It takes 50secs for the VM to start on render free tier. 


# Want to run it locally?

## Managing Environment 
### Create a env:
    python -m venv myenv

### Activate env:
     .\myenv\Scripts\activate

     or 

    source myenv/bin/activate 

### Install all required packages from requirements.txt
    pip install -r requirements.txt

#### Note: Always update requirements.txt if new packages are installed
    pip freeze > requirements.txt

## Running Code
    flask run

# Prompt

```Today's date is February 13, 2024. I am located in the Eastern Standard Time (EST) zone. I'd like you to analyze the upcoming text I provide and create an .ics file with any events you find. ONLY respond with the ics file contents and nothing else. Remember to be flexible as event information may be expressed in various ways. Also, keep an eye out for recurring events.

Guidelines:

Look for dates: Identify mentions of specific dates (mm/dd/yyyy) or days of the week along with phrases like "next Tuesday" or "this weekend."

Times: Try to catch both exact times (HH:MM) and more descriptive references (e.g., "afternoon," "all day").

Event Indicators: Words like "meeting," "appointment," "class," "party," "concert," etc. might suggest an event.

Locations: Pay attention to phrases like "at [place]," "in [location]," etc.

Recurring Clues: Look for words like "every," "weekly," "monthly," "daily," "repeats," etc. If possible, try to determine the end date of the recurring event.

Time zone is always EST
Example Input:

We 2:45PM - 5:30PM
Location: H 431 SGW
Class
Name: INSE 6311-WW
Recurring every week until may 1st

Sample output:
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//ical.marudot.com//iCal Event Maker
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:America/Toronto
LAST-MODIFIED:20231222T233358Z
TZURL:https://www.tzurl.org/zoneinfo-outlook/America/Toronto
X-LIC-LOCATION:America/Toronto
BEGIN:DAYLIGHT
TZNAME:EDT
TZOFFSETFROM:-0500
TZOFFSETTO:-0400
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZNAME:EST
TZOFFSETFROM:-0400
TZOFFSETTO:-0500
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTSTAMP:20240219T213058Z
UID:1708378246496-83841@ical.marudot.com
DTSTART;TZID=America/Toronto:20240221T144500
RRULE:FREQ=WEEKLY;BYDAY=WE;UNTIL=20240501T184500Z
DTEND;TZID=America/Toronto:20240221T173000
SUMMARY:INSE 6311-WW
LOCATION: H 431 SGW
END:VEVENT
END:VCALENDAR```
