jira_db = [
    {"id": 105, "title": "Crash on login", "priority": "High", "status": "Open"},
    {"id": 106, "title": "Typo in footer", "priority": "Low", "status": "Open"},
    {"id": 107, "title": "Button color", "priority": "Low", "status": "Done"},
    {"id": 108, "title": "API Timeout", "priority": "High", "status": "Done"}
]
report_ids = [105, 107, 108, 999]
urgent_ticket = []
closed_ticket = []
missing_ids = []
def sort_tickets(database, ids_list):
    for id in ids_list:
        found = False
        for ticket in database:
            if ticket["id"] == id and ticket["priority"] == "High" and ticket["status"] == "Open":
                urgent_ticket.append(ticket["title"])
                found = True
                break
            elif ticket["id"] == id and ticket["status"] == "Done":
                closed_ticket.append(ticket["title"])
                found = True
                break
        if found == False:
            missing_ids.append(id)
    return {
    "urgent": urgent_ticket,
    "closed": closed_ticket,
    "missing": missing_ids,
}
result = sort_tickets(jira_db, report_ids)
print(result)