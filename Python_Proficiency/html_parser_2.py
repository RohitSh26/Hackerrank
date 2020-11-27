from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        print('>>> Single-line Comment') if ('\n' not in data) else print('>>> Multi-line Comment ')
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)

html = ""
n = int(input())
if 0 < n < 100:
    for i in range(n):
        html += input().rstrip()
        html += '\n'
        
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
    

# html = """
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->
# """      
