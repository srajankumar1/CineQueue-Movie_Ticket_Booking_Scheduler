from copy import deepcopy


class Process:
    def __init__(self, pid, at, bt, priority):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.priority = priority


# ==================================================
# DISPLAY FUNCTION
# ==================================================

def display_results(title, results, gantt):

    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)

    print("\nGantt Chart:")
    print(" -> ".join(gantt))

    print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT\tRT")

    total_tat = 0
    total_wt = 0

    completion_times = []

    for p in results:

        total_tat += p["tat"]
        total_wt += p["wt"]

        completion_times.append(p["ct"])

        print(
            f"{p['pid']}\t"
            f"{p['at']}\t"
            f"{p['bt']}\t"
            f"{p['priority']}\t"
            f"{p['ct']}\t"
            f"{p['tat']}\t"
            f"{p['wt']}\t"
            f"{p['rt']}"
        )

    avg_wt = total_wt / len(results)
    avg_tat = total_tat / len(results)

    total_bt = sum(p["bt"] for p in results)

    finish_time = max(completion_times)

    cpu_utilization = (total_bt / finish_time) * 100

    throughput = len(results) / finish_time

    print("\nAverage Waiting Time     :", round(avg_wt, 2))
    print("Average Turnaround Time  :", round(avg_tat, 2))
    print("CPU Utilization (%)      :", round(cpu_utilization, 2))
    print("Throughput (P/s)         :", round(throughput, 3))


# ==================================================
# FCFS
# ==================================================

def fcfs(processes):

    procs = sorted(deepcopy(processes), key=lambda x: x.at)

    time = 0
    gantt = []
    results = []

    for p in procs:

        if time < p.at:
            time = p.at

        start = time

        time += p.bt

        ct = time
        tat = ct - p.at
        wt = tat - p.bt
        rt = start - p.at

        gantt.append(p.pid)

        results.append({
            "pid": p.pid,
            "at": p.at,
            "bt": p.bt,
            "priority": p.priority,
            "ct": ct,
            "tat": tat,
            "wt": wt,
            "rt": rt
        })

    display_results("FCFS (NON PREEMPTIVE)", results, gantt)


# ==================================================
# SJF NON PREEMPTIVE
# ==================================================

def sjf(processes):

    n = len(processes)

    proc = []

    for p in processes:
        proc.append({
            "pid": p.pid,
            "at": p.at,
            "bt": p.bt,
            "priority": p.priority,
            "done": False
        })

    completed = 0
    time = 0

    results = []
    gantt = []

    while completed < n:

        available = [
            p for p in proc
            if p["at"] <= time and not p["done"]
        ]

        if not available:
            time += 1
            continue

        current = min(
            available,
            key=lambda x: (x["bt"], x["at"])
        )

        start = time

        time += current["bt"]

        ct = time
        tat = ct - current["at"]
        wt = tat - current["bt"]
        rt = start - current["at"]

        current["done"] = True

        gantt.append(current["pid"])

        results.append({
            "pid": current["pid"],
            "at": current["at"],
            "bt": current["bt"],
            "priority": current["priority"],
            "ct": ct,
            "tat": tat,
            "wt": wt,
            "rt": rt
        })

        completed += 1

    display_results("SJF (NON PREEMPTIVE)", results, gantt)


# ==================================================
# SRTF PREEMPTIVE
# ==================================================

def srtf(processes):

    n = len(processes)

    proc = []

    for p in processes:

        proc.append({
            "pid": p.pid,
            "at": p.at,
            "bt": p.bt,
            "priority": p.priority,
            "remaining": p.bt,
            "ct": 0,
            "start": None
        })

    completed = 0
    time = 0
    gantt = []

    while completed < n:

        available = [
            p for p in proc
            if p["at"] <= time and p["remaining"] > 0
        ]

        if not available:
            time += 1
            continue

        current = min(
            available,
            key=lambda x: (
                x["remaining"],
                x["at"]
            )
        )

        if current["start"] is None:
            current["start"] = time

        gantt.append(current["pid"])

        current["remaining"] -= 1

        time += 1

        if current["remaining"] == 0:
            current["ct"] = time
            completed += 1

    results = []

    for p in proc:

        tat = p["ct"] - p["at"]
        wt = tat - p["bt"]
        rt = p["start"] - p["at"]

        results.append({
            "pid": p["pid"],
            "at": p["at"],
            "bt": p["bt"],
            "priority": p["priority"],
            "ct": p["ct"],
            "tat": tat,
            "wt": wt,
            "rt": rt
        })

    display_results("SRTF (PREEMPTIVE)", results, gantt)


# ==================================================
# PRIORITY PREEMPTIVE
# ==================================================

def priority_preemptive(processes):

    n = len(processes)

    proc = []

    for p in processes:

        proc.append({
            "pid": p.pid,
            "at": p.at,
            "bt": p.bt,
            "priority": p.priority,
            "remaining": p.bt,
            "ct": 0,
            "start": None
        })

    completed = 0
    time = 0
    gantt = []

    while completed < n:

        available = [
            p for p in proc
            if p["at"] <= time and p["remaining"] > 0
        ]

        if not available:
            time += 1
            continue

        current = min(
            available,
            key=lambda x: (
                x["priority"],
                x["at"]
            )
        )

        if current["start"] is None:
            current["start"] = time

        gantt.append(current["pid"])

        current["remaining"] -= 1

        time += 1

        if current["remaining"] == 0:

            current["ct"] = time
            completed += 1

    results = []

    for p in proc:

        tat = p["ct"] - p["at"]
        wt = tat - p["bt"]
        rt = p["start"] - p["at"]

        results.append({
            "pid": p["pid"],
            "at": p["at"],
            "bt": p["bt"],
            "priority": p["priority"],
            "ct": p["ct"],
            "tat": tat,
            "wt": wt,
            "rt": rt
        })

    display_results(
        "PRIORITY SCHEDULING (PREEMPTIVE VIP FIRST)",
        results,
        gantt
    )


# ==================================================
# MAIN
# ==================================================

print("=" * 90)
print("ONLINE MOVIE TICKET BOOKING SYSTEM")
print("CPU SCHEDULING SIMULATOR")
print("=" * 90)

n = int(input("\nEnter Number of Booking Requests: "))

processes = []

for i in range(n):

    print(f"\nBooking Request {i + 1}")

    pid = input("User ID                : ")

    at = int(input("Arrival Time           : "))

    bt = int(input("Booking Time (BT)      : "))

    print("\nPriority Levels")
    print("1 = VIP")
    print("2 = Premium")
    print("3 = Regular")
    print("4 = Economy")

    priority = int(
        input("Priority Class         : ")
    )

    processes.append(
        Process(
            pid,
            at,
            bt,
            priority
        )
    )

fcfs(processes)
sjf(processes)
srtf(processes)
priority_preemptive(processes)