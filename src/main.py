from textnode import TextNode

def main():

    #initial test
    tn = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(tn)
    tn2 = TextNode("This is a text node", "bold")
    print(tn2)


main()