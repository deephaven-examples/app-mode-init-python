"""
validate.py

A python script that validates the presence of tables in Deephaven.

@author Jake Mulford
@copyright Deephaven Data Labs
"""
from pydeephaven import Session, DHError

def main(table_names, host=None):
    """
    Main method for the script. Simply validates that each table exists

    Parameters:
        table_names (list<str>): A list of table names to validate
        host (str): An optional host if not using the default

    Returns:
        None
    """
    session = None
    if host is None:
        session = Session()
    else:
        session = Session(host=host)

    table = session.empty_table(3)
    for table_name in table_names:
        try:
            #session.open_table(table_name)
            #Temporary workaround: This script is sufficient to check that the table exists
            session.run_script("{table}={table}".format(table=table_name))
        except DHError as e:
            print("Deephaven error when trying to open table {table_name}".format(table_name=table_name))
            print(e)
            exit(1)
        except Exception as e:
            print("Unexpected error when trying to open table {table_name}".format(table_name=table_name))
            print(e)
            exit(1)

usage = """
usage: python validate.py "<table-names>" host
"""

if __name__ == '__main__':
    import sys
    try:
        table_names = sys.argv[1].split(" ")
    except:
        print(usage)
        exit(1)

    host = None
    if len(sys.argv) > 2:
        host = sys.argv[2]

    main(table_names, host)
