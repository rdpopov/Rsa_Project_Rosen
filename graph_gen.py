import csv
import sys
import os 
import numpy as np
import matplotlib.pyplot as plt

def read_csv(name):
    data  = []
    mean_time=[]
    with open(name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data.pop(0)
    for i in range(len(data)):
        mean_time.append(int(data[i][len(data[i])-1].strip(';')))
    return np.mean(mean_time)


def gen_graph(listo,n_thr):
    size_of_input_buffer = [512, 1024, 2048, 4096, 8192, 12288, 16384, 20480, 24576, 32768]
    tmp_list = []
    listo.sort()
    for i in range(len(listo)):
        tmp = read_csv(listo[i])
        tmp_list.append(tmp)
    plt.plot(tmp_list,size_of_input_buffer)
    plt.xlabel("Mean thread execution time (Threads: {})".format(str(n_thr)))
    plt.ylabel("Read buffer size")
    print("made graph for {} thread".format(n_thr))
    plt.savefig("threads" + str(n_thr) + ".png",figsize=(1920,1020))
    plt.close()
    return tmp_list



def get_names_of_files(name_wild, dir_thr):
    path = './res/'+ str(dir_thr) + '/'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if name_wild in file:
                files.append(os.path.join(r, file))
    return files

def generate_all_graphs(name,threads):
    final_info = []
    size_of_input_buffer = [512, 1024, 2048, 4096, 8192, 12288, 16384, 20480, 24576, 32768]
    colors = [   "#178b90",
                 "#2586a2",
                 "#29d5cb",
                 "#2eadd0",
                 "#37c6ed",
                 "#3e550f",
                 "#413616",
                 "#4c221d",
                 "#586bd5",
                 "#619e9a",
                 "#6399fb",
                 "#6e45ef",
                 "#7531d3",
                 "#7f78a4",
                 "#86f4dd",
                 "#8d4580",
                 "#8fb7ac",
                 "#97e31a",
                 "#a01f99",
                 "#ae009f",
                 "#af8855",
                 "#b6b44d",
                 "#ba916a",
                 "#cc065c",
                 "#cc20c2",
                 "#d8b4f3",
                 "#f62886"]
    for i in range(threads):
        res = get_names_of_files('bench-results-' + name + '-',i+1 )
        res.sort()
        final_info.append( gen_graph(res,i+1))

    for i in range(threads):
        plt.plot(size_of_input_buffer,final_info[i], label ="Threads {}".format(i+1))

    plt.legend(loc="upper right", ncol=3)
    plt.title("All threads plot")
    plt.xlabel("Input_size")
    plt.ylabel("Time")
    plt.savefig("All threads Fig",figsize=(1920,1080))

sys.argv.pop(0)
name = sys.argv[0]
threads = int(sys.argv[1])
if threads == 0 :
   threads = 16
if name == "":
    name = "lorem"
threads=16
name="lorem"
generate_all_graphs(name, threads)
