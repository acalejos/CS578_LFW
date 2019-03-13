import sys

def progressBar(name, value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\r{2} Progress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100)),name))
        sys.stdout.flush()
