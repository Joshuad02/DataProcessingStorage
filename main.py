from collections import defaultdict

class InMemoryDB:
    def __init__(self) -> None:
        self.db = defaultdict(int)
        # Make an array of tuples of key, value paair
        # If it is a commit then u iterate through this array and add to db
        # If it is a rollback then you dont commit
        self.currDB = defaultdict(int)
        # Whether or not a transaction is in progress
        self.trans = False
    
    def get(self, key):
        if key in self.db:
            print("GET", self.db[key])
            return self.db[key]
        print("GET", None)
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

    # should return null, because A doesn’t exist in the DB yet
    inmemoryDB.get("A")

    # should throw an error because a transaction is not in progress
    inmemoryDB.put("A", 5)

    # starts a new transaction
    inmemoryDB.begin_transaction();

    # set’s value of A to 5, but its not committed yet
    inmemoryDB.put("A", 5);

    # should return null, because updates to A are not committed yet
    inmemoryDB.get("A")

    # update A’s value to 6 within the transaction
    inmemoryDB.put("A", 6)

    # commits the open transaction
    inmemoryDB.commit()

    # should return 6, that was the last value of A to be committed
    inmemoryDB.get("A")

    # throws an error, because there is no open transaction
    inmemoryDB.commit()

    # throws an error because there is no ongoing transaction
    inmemoryDB.rollback()

    # should return null because B does not exist in the database
    inmemoryDB.get("B")

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # Set key B’s value to 10 within the transaction
    inmemoryDB.put("B", 10)

    # Rollback the transaction - revert any changes made to B
    inmemoryDB.rollback()

    # Should return null because changes to B were rolled back
    inmemoryDB.get("B")

if __name__ == '__main__':
    main()
