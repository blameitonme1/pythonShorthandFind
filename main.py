import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <script_number>")
        sys.exit(1)
    script_num = int(sys.argv[1])
    if script_num == 1 :
        import find
        find.run()
    elif script_num == 2:
        import addItem
        addItem.run()
    else:
        print("Invalid script number. Choose 1 or 2. 1 for find, 2 for addItem")
if __name__ == "__main__":
    main()

