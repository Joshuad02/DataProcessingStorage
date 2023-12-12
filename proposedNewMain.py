from collections import defaultdict

class InMemoryDB:
    def __init__(self) -> None:
        # db has string : int
        self.db = defaultdict(int)
        self.currDB = defaultdict(int)
        # Whether or not a transaction is in progress
        self.trans = False
    
    def get(self, key):
        if key in self.db:
            print(self.db[key])
            return self.db[key]
        print(None)
        return None

    def put(self, key, val):
        if self.trans:
            self.currDB[key] = val
        else:
            raise Exception("Transaction not in progress")

    def begin_transaction(self):
        if not self.trans:
            self.trans = True
        else:
            raise Exception("Transaction already in progress")
    def commit(self):
        if self.trans:
            for key, val in self.currDB.items():
                self.db[key] = val
            self.trans = False
        else:
            raise Exception("Transaction not in progress")

    def rollback(self):
        self.currDB.clear()
        self.trans = False



def main():
    inmemoryDB = InMemoryDB()

    print("InMemoryDB started. Type a command to start or type EXIT to terminate program. Enter HELP for commands.")
    command = ""
    
    while command != "EXIT":
        command = input()
        currCommand = command.split()
        if currCommand[0] == "GET":
            inmemoryDB.get(currCommand[1])
        elif currCommand[0] == "PUT":
            inmemoryDB.put(currCommand[1], currCommand[2])
        elif currCommand[0] == "BEGIN" and currCommand[1] == "TRANSACTION":
            inmemoryDB.begin_transaction()
        elif currCommand[0] == "COMMIT":
            inmemoryDB.commit()
        elif currCommand[0] == "ROLLBACK":
            inmemoryDB.rollback()
        elif currCommand[0] == "HELP":
            print("GET(key)")
            print("PUT(key, val)")
            print("BEGIN TRANSACTION")
            print("COMMIT")
            print("ROLLBACK")
        else:
            print("Invalid command, try again or type EXIT to temrinate program")
        

if __name__ == '__main__':
    main()
