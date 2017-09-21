import argparse

#  命令行输入：
# python3 main.py input.csv -o output.txt --port 3306 -s 192.168.1.1 10.10.4.23 -t 3
# python3 main.py -h 查看help

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file', help="input file")  # 命令，必填
parser.add_argument('-o', '--output', required=True, help='output file')  # 既可以用-o也可以用--output表示该选项
parser.add_argument('--port', type=int, nargs='?', default=80, help="port to listen")  # 只有一个值
parser.add_argument("-s", type=str, nargs='+', help='server list to connect')  # 至少有一个值
parser.add_argument("-t", type=int, dest="threads", help='threads')  # 指定解析时的属性名

# 获取参数
args = parser.parse_args()

INPUT = args.file
OUTPUT = args.output
SERVER_LIST = args.s
PORT = args.port
THREADS = args.threads  # 不能用args.t，因为在add_argument指定了dest

print(
    "input = %s, output = %s, server list = %s, port = %d, threads = %d" % (INPUT, OUTPUT, SERVER_LIST, PORT, THREADS))
