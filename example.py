import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

if __name__ == '__main__':
    app.run(debug=True)


import pandas as pd
import pprint as pp
​
import sqlite3
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 500)
​
def read_file(file):
    con = sqlite3.connect(file)
    sql_query = pd.read_sql_query("SELECT * FROM passenger", con)
    data = pd.DataFrame(sql_query)
    return data
​
​
def main():
    database = "titanic.sqlite"
    data_df = read_file(database)
    col_names = list(data_df.columns)
    print(col_names)
    print("############### raw DF")
    pp.pprint(data_df.head(1))
    titanic_dictionary = data_df.to_dict()
    print("############### simple DF to Dictionary")
    pp.pprint(titanic_dictionary)
    titanicD = data_df.set_index('name').T.to_dict('dict')
​
    print("############### DF with specify index to Dictionary Transposed")
    pp.pprint(titanicD)
​
    for key, value in titanicD.items():
        value["name"] = key
    list_of_dictionaries = [x for x in titanicD.values()]
    for each in list_of_dictionaries:
        print(each)
    print(col_names)
    for each in list_of_dictionaries:
        for item in col_names:
            print(each[item])
    print(col_names)
    for item in col_names:
        for each in list_of_dictionaries:
            print(each[item], end=", ")
        print()
​
main()
Collapse












