from detector import count_log_levels


def read_logs(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def parse_log(log):
    parts = log.strip().split()

    parsed_log = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": " ".join(parts[3:])
    }

    return parsed_log


logs = read_logs("logs/sample.log")

parsed_logs = []

for log in logs:
    parsed_logs.append(parse_log(log))

print(parsed_logs)

print()

print(count_log_levels(parsed_logs))