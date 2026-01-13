raw_logs = [
    "jdoe:ServerRoom",
    "ADMIN:Kitchen",
    "guest:Office",
    12345,               # int (AttributeError)
    "hacker:ServerRoom",
    "Manager : Office",  # Пробіли
    "corrupted_data"     # Немає розділювача (ValueError)
]
users_db = [
    {"id": "jdoe", "role": "dev", "access_rooms": ["Office", "Kitchen"]},
    {"id": "admin", "role": "admin", "access_rooms": ["ServerRoom", "Office", "Kitchen"]},
    {"id": "manager", "role": "manager", "access_rooms": ["Office", "MeetingRoom"]},
    {"id": "guest", "role": "visitor", "access_rooms": ["Reception"]}
]
security_report = []
def no_idea (log_list, user_list):
    while len(log_list) > 0:
        log = log_list.pop(0)
        found = False
        try:
            split_log = log.split(":")
            user_strip = split_log[0].strip()
            room_strip = split_log[1].strip()
            user_lower = user_strip.lower()
        except (AttributeError, ValueError, IndexError):
            print(f"{log} is not a log")
            continue
        for user in user_list:
            if user["id"] == user_lower:
                found = True
                if room_strip in user["access_rooms"]:
                    security_report.append(f"User {user_lower} -> {room_strip}: GRANTED")
                    break
                else:
                    security_report.append(f"User {user_lower} -> {room_strip}: DENIED")
                    break
        if not found:
            security_report.append(f"User {user_lower} -> UNKNOWN")
    return security_report
result = no_idea (raw_logs, users_db)
print(result)


