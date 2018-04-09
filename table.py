import json
from git import Repo
from git import Actor


class Table:
    rows = None
    schema = None

    def __init__(self, schema, rows):
        self.rows = rows
        self.schema = schema
    def getSchema(self):
        return self.schema
    def getRows(self):
        return self.rows
    def getRow(self, index):
        return Row(self.rows[index], self.schema)
    def appendRow(self, row):
        self.rows.append(row)
    def insertRow(self, index, row):
        self.rows.insert(index, row)
    def deleteRow(self, index):
        self.rows.pop(index)
    def getJson(self):
        obj = {'schema':self.schema, 'rows':self.rows}
        json_obj = json.dumps(obj)
        return json_obj
    def save(self):
        with open('data.py', 'w') as file:
            file.write(self.getJson())
    @staticmethod
    def load(path):
        with open('./data.py') as data:
            table = json.load(data)
            schema = table['schema']
            rows = table['rows']
            return Table(schema, rows)

class Row:
    values = None
    schema = None
    def __init__(self, values, schema):
        self.values = values
        self.schema = schema
    def getSchema(self):
        return self.schema
    def getValue(self, column):
        for index, element in enumerate(self.getSchema()):
            if( element['column'] == column):
                return self.values[index]
        return None

schema = [{'column':'c1', 'type':'string'},{'column':'c2', 'type':'string'}]
new_row1 = ['yay1', 'nay1']
new_row2 = ['yay2', 'nay2']
new_row3 = ['yay3', 'nay3']
table = Table.load('./data')
print(table.getJson())
repo = Repo('.')
index = repo.index
#index.add(['./data.py'])


#origin = repo.remotes['github']
#assert origin.exists()
# push and pull behaves similarly to `git push|pull`
#origin.pull()
#origin.push()
# assert not empty_repo.delete_remote(ori
