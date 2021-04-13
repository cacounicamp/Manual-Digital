import sys
from html.parser import HTMLParser

filename = sys.argv[1]

with open(filename) as f:
    o_html = f.read()
    f.close()

p_html = ""
indent = 0

class myparser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global p_html
        global indent
        if tag != "span":
            p_html += "\t" * indent + "<{}>\n".format(tag)
            indent += 1

    def handle_endtag(self, tag):
        global p_html
        global indent
        if tag != "span":
            indent -= 1
            p_html += "\t" * indent + "</{}>\n".format(tag)

    def handle_data(self, data):
        global p_html
        global indent
        p_html += "\t" * indent + "{}\n".format(data)

parser = myparser()
parser.feed(o_html)
parser.close()

p_html.split("\n")
#for i in range(len(p_html)):
#    if p_html[i][0] == "<":

print(p_html)
