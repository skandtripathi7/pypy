logs = [
    "2026-01-28|TC_101|EngineSpeed|2500|PASS",
    "2026-01-28|TC_101|OilTemp|140|FAIL",
    "2026-01-28|TC_102|Voltage|12|PASS",
    "2026-01-28|TC_101|RPM|3000|FAIL",
]

def analyze_logs(logs):

    res_data = {}

    for log in logs:
        
        log_data = log.split("|")

        if len(log_data) == 5:
            if log_data[1] not in res_data.keys():
                res_data[log_data[1]] = {"PASS":0,"FAIL":0}

            if log_data[4] == "PASS":
                res_data[log_data[1]]["PASS"] += 1
            elif log_data[4] == "FAIL":
                res_data[log_data[1]]["FAIL"] += 1

        else:
            continue
    
    return res_data

print(analyze_logs(logs))
