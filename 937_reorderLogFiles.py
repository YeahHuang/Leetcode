class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for i, log in enumerate(logs):
            if (log.split(" ")[1][0]).isdigit():
                digit_logs.append(i)
            else:
                letter_logs.append(i)
        letter_logs.sort(key = lambda idx: (" ".join(logs[idx].split(" ")[1:]), logs[idx].split(" ")[0]))
        return [logs[i] for i in letter_logs] + [logs[i] for i in digit_logs]

        #Sol 1.1 删除引用 48ms -> 44ms
        letter_logs = []
        digit_logs = []
        for i, log in enumerate(logs):
            if (log.split(" ")[1][0]).isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key = lambda log: (" ".join(log.split(" ")[1:]), log.split(" ")[0]))
        return letter_logs + digit_logs

        #Sol 2filter 44ms
        letter_logs = filter(lambda log: log[log.find(" ") + 1].isalpha(), logs)
        digit_logs = filter(lambda log: log[log.find(" ") + 1].isdigit(), logs)
        return sorted(letter_logs, key = lambda log: (log[log.find(" "):], log[:log.find(" ")])) + list(digit_logs)

        '''
        filter举例：https://book.pythontips.com/en/latest/map_filter.html
        number_list = range(-5, 5)
        less_than_zero = list(filter(lambda x: x < 0, number_list))
        '''