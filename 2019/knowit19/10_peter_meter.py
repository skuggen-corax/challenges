import timeit
import re
import datetime as dt

with open('data/in10.txt') as f:
    inputs = f.read().split('\n')

rgx_tannkrem = "...([0-9]+) ml (tannkrem)"
rgx_sjampo = "...([0-9]+) ml (sjampo)"
rgx_toalett = "...([0-9]+) meter (toalettpapir)"

def parse_input(inputs):
    current_date = dt.datetime.strptime("Jan 01" + " 2018", "%b %d %Y")
    sum_sj = sum_tan = sum_toa = o_sum_toa = s_sum_sj = 0

    for line in inputs:
        m_sj = re.match(rgx_sjampo, line)
        m_tan = re.match(rgx_tannkrem, line)
        m_toa = re.match(rgx_toalett, line)
        if m_sj:
            sum_sj += int(m_sj.group(1))
            if current_date.isoweekday() == 7:
                s_sum_sj += int(m_sj.group(1))
        elif m_tan:
            sum_tan += int(m_tan.group(1))
        elif m_toa:
            sum_toa += int(m_toa.group(1))
            if current_date.isoweekday() == 3:
                o_sum_toa += int(m_toa.group(1))
        else:
            current_date = dt.datetime.strptime(line + " 2018", "%b %d: %Y")
    return (sum_sj // 300) * (sum_tan // 125) * (sum_toa // 25) * s_sum_sj * o_sum_toa

result = parse_input(inputs)
print(result)