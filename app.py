from flask import Flask, render_template, request, send_file
import requests
from openai import OpenAI

app = Flask(__name__)

def call_api(client, form_data):
    response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
        "role": "system",
        "content": "Today's date is February 13, 2024. I am located in the Eastern Standard Time (EST) zone. I'd like you to analyze the upcoming text I provide and create an .ics file with any events you find. ONLY respond with the ics file contents and nothing else. Remember to be flexible as event information may be expressed in various ways. Also, keep an eye out for recurring events.\n\nGuidelines:\n\nLook for dates: Identify mentions of specific dates (mm/dd/yyyy) or days of the week along with phrases like \"next Tuesday\" or \"this weekend.\"\n\nTimes: Try to catch both exact times (HH:MM) and more descriptive references (e.g., \"afternoon,\" \"all day\").\n\nEvent Indicators: Words like \"meeting,\" \"appointment,\" \"class,\" \"party,\" \"concert,\" etc. might suggest an event.\n\nLocations: Pay attention to phrases like \"at [place],\" \"in [location],\" etc.\n\nRecurring Clues: Look for words like \"every,\" \"weekly,\" \"monthly,\" \"daily,\" \"repeats,\" etc. If possible, try to determine the end date of the recurring event.\n\nTime zone is always EST\nExample Input:\n\nWe 2:45PM - 5:30PM\nLocation: H 431 SGW\nClass\nName: INSE 6311-WW\nRecurring every week until may 1st\n\nSample output:\nBEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//ical.marudot.com//iCal Event Maker\nCALSCALE:GREGORIAN\nBEGIN:VTIMEZONE\nTZID:America/Toronto\nLAST-MODIFIED:20231222T233358Z\nTZURL:https://www.tzurl.org/zoneinfo-outlook/America/Toronto\nX-LIC-LOCATION:America/Toronto\nBEGIN:DAYLIGHT\nTZNAME:EDT\nTZOFFSETFROM:-0500\nTZOFFSETTO:-0400\nDTSTART:19700308T020000\nRRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\nEND:DAYLIGHT\nBEGIN:STANDARD\nTZNAME:EST\nTZOFFSETFROM:-0400\nTZOFFSETTO:-0500\nDTSTART:19701101T020000\nRRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\nEND:STANDARD\nEND:VTIMEZONE\nBEGIN:VEVENT\nDTSTAMP:20240219T213058Z\nUID:1708378246496-83841@ical.marudot.com\nDTSTART;TZID=America/Toronto:20240221T144500\nRRULE:FREQ=WEEKLY;BYDAY=WE;UNTIL=20240501T184500Z\nDTEND;TZID=America/Toronto:20240221T173000\nSUMMARY:INSE 6311-WW\nLOCATION: H 431 SGW\nEND:VEVENT\nEND:VCALENDAR"
        },
        {
        "role": "user",
        "content": form_data
        }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response.choices[0].message)
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form['field_name']
        api_key = request.form['api_key']
        try:
            client = OpenAI(api_key=api_key)
        except Exception as e:
            return "Error wit API key"
        ics_content = call_api(client, form_data)
        # ics_content = "dsfsdfs"
        
        with open("output.ics","w") as f:
            f.write(ics_content)

        if ics_content:
            return send_file(
                "output.ics",
                as_attachment=True,
                download_name="calendar_event.ics",
                mimetype="text/calendar"
            )
        else:
            return "Error generating ICS file"

    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)
