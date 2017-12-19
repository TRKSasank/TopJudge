# coding: UTF-8

import os
import json

in_path = "/disk/mysql/mysql/Law1/out.txt"
out_path = "/disk/mysql/law_data/formed_data/0"
mid_text = u"  _(:з」∠)_  "
title_list = ["docId", "caseNumber", "caseName", "spcx", "court", "time", "caseType", "bgkly", "yuanwen", "document",
              "cause", "docType", "keyword", "lawyer", "punishment", "result", "judge"]


def draw_out(in_path, out_path):
    inf = open(in_path, "r")
    ouf = open(out_path, "w")

    data_str = ""
    done_num = 0
    gg_num = 0
    for line in inf:
        try:
            data_str += line[:-1]
            cnt = data_str.count(mid_text)
            if cnt == len(title_list) - 1:
                pass
            elif cnt < len(title_list) - 1:
                continue
            else:
                gg_num += 1
                print(gg_num)
                gg
                continue

            data_str = data_str.split(mid_text)

            data = {}

            if len(data_str) == len(title_list):
                for a in range(0, len(data_str)):
                    data[title_list[a]] = data_str[a]
                for a in data:
                    if data[a] == u"\\N":
                        data[a] = ""
                data["document"] = data["document"].replace("\\", "")
                if data["document"] == "":
                    data["document"] = "{\"content\":\"\"}"
                data["documnet"] = json.loads(data["document"])

                print(json.dumps(data, ensure_ascii=False), file=ouf)
                done_num += 1
                if done_num % 100000 == 0:
                    print(done_num)

                data_str = ""
            else:
                gg

        except Exception as e:
            print(e)
            gg


def work(from_id, to_id):
    for a in range(int(from_id), int(to_id)):
        print(str(a) + " begin to work")
        draw_out(os.path.join(in_path, str(a)), os.path.join(out_path, str(a)))
        print(str(a) + " work done")


num_file = 1
num_process = 1

if __name__ == "__main__":
    draw_out(in_path,out_path)
    """
    import multiprocessing

    process_pool = []

    for a in range(0, num_process):
        process_pool.append(
            multiprocessing.Process(target=work, args=(a * num_file / num_process, (a + 1) * num_file / num_process)))

    for a in process_pool:
        a.start()

    for a in process_pool:
        a.join()"""
