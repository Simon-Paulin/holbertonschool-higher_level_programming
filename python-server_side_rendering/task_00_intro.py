def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("template should be a string.")
        return
    elif (not isinstance(attendees, list) or
          not all(isinstance(a, dict) for a in attendees)):
        print("attendees shoud be a list of dictionary.")
        return
    elif not template:
        print("Template is empty, no output files generated.")
        return
    elif not attendees:
        print("No data provided, no output files generated.")
        return
    else:
        idx = 1
        for person in attendees:
            name = person.get('name') or 'N/A'
            title = person.get('event_title') or 'N/A'
            date = person.get('event_date') or 'N/A'
            location = person.get('event_location') or 'N/A'

            output = template.replace('{name}', name)
            output = output.replace('{event_title}', title)
            output = output.replace('{event_date}', date)
            output = output.replace('{event_location}', location)

            filename = f'output_{idx}.txt'
            with open(filename, 'w') as file:
                file.write(output)

            idx += 1
