from abc import ABC, abstractmethod

class TimeInterval(ABC):
    @abstractmethod
    def duration_in_seconds(self):
        pass

    @abstractmethod
    def to_human_readable(self):
        pass


class HMSInterval(TimeInterval):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def duration_in_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_human_readable(self):
        total_seconds = self.duration_in_seconds()
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"


class MSInterval(TimeInterval):
    def __init__(self, milliseconds):
        self.milliseconds = float(milliseconds)

    def duration_in_seconds(self):
        return self.milliseconds / 1000

    def to_human_readable(self):
        total_seconds = round(self.duration_in_seconds())
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"


class MinSecInterval(TimeInterval):
    def __init__(self, minutes, seconds):
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def duration_in_seconds(self):
        return self.minutes * 60 + self.seconds

    def to_human_readable(self):
        total_seconds = self.duration_in_seconds()
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"


class HoursInterval(TimeInterval):
    def __init__(self, hours):
        self.hours = float(hours)

    def duration_in_seconds(self):
        return self.hours * 3600

    def to_human_readable(self):
        total_seconds = round(self.duration_in_seconds())
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours}h {minutes}m {seconds}s"



def process_intervals(intervals, command):
    if not intervals or len(intervals) == 0:
        raise ValueError("No intervals provided")

    durations = [interval.duration_in_seconds() for interval in intervals]

    result_interval = None

    if command.lower() == 'sum':
        total_duration = sum(durations)
        result_interval = HMSInterval(
            total_duration // 3600,
            (total_duration % 3600) // 60,
            total_duration % 60
        )
    elif command.lower() == 'avg':
        avg_duration = sum(durations) / len(durations)
        result_interval = HMSInterval(
            int(avg_duration // 3600),
            int((avg_duration % 3600) // 60),
            int(avg_duration % 60)
        )
    elif command.lower() == 'max':
        max_duration = max(durations)
        result_interval = HMSInterval(
            max_duration // 3600,
            (max_duration % 3600) // 60,
            max_duration % 60
        )
    elif command.lower() == 'min':
        min_duration = min(durations)
        result_interval = HMSInterval(
            min_duration // 3600,
            (min_duration % 3600) // 60,
            min_duration % 60
        )
    else:
        raise ValueError(f"Unknown command '{command}'")

    return result_interval.to_human_readable(), result_interval.duration_in_seconds()


intervals = [
        HMSInterval(hours=1, minutes=30),
        MSInterval(milliseconds=90000),
        MinSecInterval(minutes=3, seconds=45),
        HoursInterval(hours=2.5)
    ]


result_format, result_value = process_intervals(intervals, 'avg')
print(f"Average: {result_format}, Average Duration: {result_value:.2f} sec.")

result_format, _ = process_intervals(intervals, 'max')
print(f"Max: {result_format}")

result_format, _ = process_intervals(intervals, 'min')
print(f"Min: {result_format}")
