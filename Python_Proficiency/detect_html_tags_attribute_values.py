from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if attrs:
            for a in attrs:
                print ('->',a[0], '>', a[1] )


if __name__ == '__main__':
    parser = MyHTMLParser()

    parser.feed(
        """
        <head>
        <title>HTML</title>
        </head>
        <object type="application/x-flash" 
        data="your-file.swf" 
        width="0" height="0">
        <!-- <param name="movie" value="your-file.swf" /> -->
        <param name="quality" value="high"/>
        </object>
        """
    )