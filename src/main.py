import os, shutil
from textnode import TextNode, TextType



def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    #check if path exists
    dir_list = os.listdir(path='.')
    print(dir_list)

    if os.path.exists("public"): 
        print("delete the path")
        dir = "public"
        location = "public"
        path = os.path.join(location, dir)
        shutil.rmtree(path)
        print("Has been deleted")
        print("Copy dir")
        static_dir = "static"
        shutil.copy(static_dir , dir)
        print("DIR has been copied and public crated")



    else:
        print("Needs to create")
        os.mkdir("public")
        
main()