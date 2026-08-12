def count_log_levels(parsed_logs):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for log in parsed_logs:
        level = log["level"]

        if level in counts:
            counts[level] += 1

    return counts