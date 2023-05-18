import json

c = {}

deep_sleep_total_count = 0  #  1
deep_sleep_count_arr = [] 
deep_sleep_count = 0
last_deep_sleep = ""
light_sleep_total_count = 0  #  2
light_sleep_count_arr = [] 
light_sleep_count = 0
last_light_sleep = ""
rem_sleep_total_count = 0 # 3
rem_sleep_count_arr = [] 
rem_sleep_count = 0
last_rem_sleep = ""
other_sleep_total_count = 0 # 4
other_sleep_count_arr = [] 
other_sleep_count = 0
last_other_sleep = ""
wake_sleep_total_count = 0 # 0
wake_sleep_count_arr = [] 
wake_sleep_count = 0
last_wake_sleep = ""

sleep_time_arr = []
sleep_value_arr = []
max_hr = 0
min_hr = 999
count = 0
total = 0
hr_value_arr = [] 

file_path = "/Users/golfy/Documents/睡眠文档/sleepReport/Sleepreport_liu/王尔卓.txt"


file_obj = open(file_path,'r')

try:
    all_text = file_obj.readlines()
    
    for idx,line in enumerate(all_text):

        if idx == 0:
            c["phone"] = line.split("\n")[0]
            continue

        if idx < 5:
            continue

        line_arr = line.split("\n")[0].split("\t")

        hr_value = float(line_arr[0])
        hr_value_arr.append(line_arr[0])
        if max_hr <= hr_value:
            max_hr = hr_value
        if min_hr >= hr_value:
            min_hr = hr_value
        total += hr_value
        count += 1


        line1_arr = line_arr[1].split()
        sleep_time_arr.append(line1_arr[1].replace(","," "))

        res = line1_arr[0].split(":")[0]
        sleep_value_arr.append(res)

        if res == "1":
            deep_sleep_total_count = deep_sleep_total_count + 1

            if last_deep_sleep == "":
                deep_sleep_count = 1
            else:
                deep_sleep_count += 1

            if last_light_sleep != "":
                light_sleep_count_arr.append(light_sleep_count)
                light_sleep_count = 0
                last_light_sleep = ""
            if last_rem_sleep != "":
                rem_sleep_count_arr.append(rem_sleep_count)
                rem_sleep_count = 0
                last_rem_sleep = ""
            if last_other_sleep != "":
                other_sleep_count_arr.append(other_sleep_count)
                other_sleep_count = 0
                last_other_sleep = ""
            if last_wake_sleep != "":
                wake_sleep_count_arr.append(wake_sleep_count)
                wake_sleep_count = 0
                last_wake_sleep = ""

            last_deep_sleep = res
        elif res == "2":
            light_sleep_total_count = light_sleep_total_count + 1

            if last_light_sleep == "":
                light_sleep_count = 1
            else:
                light_sleep_count += 1

            if last_deep_sleep != "":
                deep_sleep_count_arr.append(deep_sleep_count)
                deep_sleep_count = 0
                last_deep_sleep = ""
            if last_rem_sleep != "":
                rem_sleep_count_arr.append(rem_sleep_count)
                rem_sleep_count = 0
                last_rem_sleep = ""
            if last_other_sleep != "":
                other_sleep_count_arr.append(other_sleep_count)
                other_sleep_count = 0
                last_other_sleep = ""
            if last_wake_sleep != "":
                wake_sleep_count_arr.append(wake_sleep_count)
                wake_sleep_count = 0
                last_wake_sleep = ""

            last_light_sleep = res
        elif res == "3":
            rem_sleep_total_count = rem_sleep_total_count + 1

            if last_rem_sleep == "":
                rem_sleep_count = 1
            else:
                rem_sleep_count += 1

            if last_light_sleep != "":
                light_sleep_count_arr.append(light_sleep_count)
                light_sleep_count = 0
                last_light_sleep = ""
            if last_deep_sleep != "":
                deep_sleep_count_arr.append(deep_sleep_count)
                deep_sleep_count = 0
                last_deep_sleep = ""
            if last_other_sleep != "":
                other_sleep_count_arr.append(other_sleep_count)
                other_sleep_count = 0
                last_other_sleep = ""
            if last_wake_sleep != "":
                wake_sleep_count_arr.append(wake_sleep_count)
                wake_sleep_count = 0
                last_wake_sleep = ""

            last_rem_sleep = res
        elif res == "4":
            other_sleep_total_count = other_sleep_total_count + 1

            if last_other_sleep == "":
                other_sleep_count = 1
            else:
                other_sleep_count += 1

            if last_light_sleep != "":
                light_sleep_count_arr.append(light_sleep_count)
                light_sleep_count = 0
                last_light_sleep = ""
            if last_deep_sleep != "":
                deep_sleep_count_arr.append(deep_sleep_count)
                deep_sleep_count = 0
                last_deep_sleep = ""
            if last_rem_sleep != "":
                rem_sleep_count_arr.append(rem_sleep_count)
                rem_sleep_count = 0
                last_rem_sleep = ""
            if last_wake_sleep != "":
                wake_sleep_count_arr.append(wake_sleep_count)
                wake_sleep_count = 0
                last_wake_sleep = ""

            last_other_sleep = res
        else:
            wake_sleep_total_count = wake_sleep_total_count + 1

            if last_wake_sleep == "":
                wake_sleep_count = 1
            else:
                wake_sleep_count += 1

            if last_light_sleep != "":
                light_sleep_count_arr.append(light_sleep_count)
                light_sleep_count = 0
                last_light_sleep = ""
            if last_rem_sleep != "":
                rem_sleep_count_arr.append(rem_sleep_count)
                rem_sleep_count = 0
                last_rem_sleep = ""
            if last_other_sleep != "":
                other_sleep_count_arr.append(other_sleep_count)
                other_sleep_count = 0
                last_other_sleep = ""
            if last_deep_sleep != "":
                deep_sleep_count_arr.append(deep_sleep_count)
                deep_sleep_count = 0
                last_deep_sleep = ""

            last_wake_sleep = res
    
    c["deep_sleep_total_count"] = str(deep_sleep_total_count)
    c["deep_sleep_count_arr"] = deep_sleep_count_arr
    c["light_sleep_total_count"] = str(light_sleep_total_count)
    c["light_sleep_count_arr"] = light_sleep_count_arr
    c["rem_sleep_total_count"] = str(rem_sleep_total_count)
    c["rem_sleep_count_arr"] = rem_sleep_count_arr
    c["other_sleep_total_count"] = str(other_sleep_total_count)
    c["other_sleep_count_arr"] = other_sleep_count_arr
    c["wake_sleep_total_count"] = str(wake_sleep_total_count)
    c["wake_sleep_count_arr"] = wake_sleep_count_arr

    c["sleep_time_arr"] = sleep_time_arr
    c["sleep_value_arr"] = sleep_value_arr
    
    mean_hr = total / count

    c["max_hr"] = "%.0f"%(max_hr)
    c["min_hr"] = "%.0f"%(min_hr)
    c["mean_hr"] = "%.0f"%(mean_hr)
    c["hr_value_arr"] = hr_value_arr
finally:
    file_obj.close()

with open("result_sleep.json","w", encoding="utf-8") as tf:
    json.dump(c, fp=tf, ensure_ascii=False)