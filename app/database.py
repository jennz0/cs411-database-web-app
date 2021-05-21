"""Defines all the functions related to the database"""
from app import db

""" Monitor """
def fetch_todo_monitor() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Monitor;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list


def update_task_entry_monitor(task_id: int, price: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Monitor set price = "{}" where monitor_id = {};'.format(float(price), task_id)
    conn.execute(query)
    conn.close()



def insert_new_task_monitor(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    outArray = text.split(",")
    conn = db.connect()
    query = 'Insert Into Monitor (monitor_id, make, purpose, size, price) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(
        outArray[0], outArray[1],outArray[2],outArray[3],outArray[4])

    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id_monitor(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Monitor where monitor_id={};'.format(task_id)
    conn.execute(query)
    conn.close()

#search
def seach_for_tasks_monitor(text: str) ->  dict:
    conn = db.connect()
    query = 'SELECT * FROM Monitor WHERE '
    que = text.split(",")
    for i in range(len(que)):
        item = que[i].split(':')
        if(i == 0):
            if(item[0] == "make"):
                query += item[0] + " = " + "\""+ item[1] + "\""
                #query += "make LIKE '{0}%'".format(item[1])
            elif item[0] == "purpose":
                query += item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
        else:
            if(item[0] == "make"):
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += " AND " +item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
    query +=";"
    print(query)
    conn = db.connect()
     
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list

def advance_query_monitor() -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT purpose,avg(price) From Monitor WHERE size > 30 GROUP BY purpose;").fetchall()
    conn.close()
    todo_list = []
    
    for result in query_results:
        item = {
            "id": "NOT APPLICABLE",
            "make": "NOT APPLICABLE",
            "purpose": result[0],
            "size": "NOT APPLICABLE",
            "price": result[1],
        }
        todo_list.append(item) 

    return todo_list
    
""" Storage """
def fetch_todo_storage() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Storage;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list

def advance_query_storage(text: str) -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT make,avg(price) From Storage WHERE size > 512 GROUP BY make  UNION SELECT make,avg(price) From Storage WHERE purpose = 'game' GROUP BY make;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": "-",
            "make": result[0],
            "purpose": "-",
            "size": "-",
            "price": result[1],
        }
        todo_list.append(item)

    return todo_list

def update_task_entry_storage(task_id: int, price: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Storage set price = "{}" where storage_id = {};'.format(float(price), task_id)
    conn.execute(query)
    conn.close()



def insert_new_task_storage(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    outArray = text.split(",")
    conn = db.connect()
    query = 'Insert Into Storage (storage_id,make, purpose,size,price) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(
        outArray[0], outArray[1],outArray[2],outArray[3],outArray[4])

    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id_storage(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Storage where storage_id={};'.format(task_id)
    conn.execute(query)
    conn.close()

#search
def seach_for_tasks_storage(text: str) ->  dict:
    conn = db.connect()
    query = 'SELECT * FROM Storage WHERE '
    que = text.split(",")
    for i in range(len(que)):
        item = que[i].split(':')
        if(i == 0):
            if(item[0] == "make"):
                query += item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "price":
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
            else:
                query += item[0] + " = " + item[1]
        else:
            if(item[0] == "make"):
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "price":
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += " AND " +item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
            else:
                query += " AND " +item[0] + " = " + item[1]
    query +=";"
    print(query)
    conn = db.connect()
     
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list

""" CPU """
def fetch_todo_cpu(text:int = -1, purpose:str = "all") -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    print("CALL cpu_qr({})".format(text))
    if text == -1 and purpose == "all":
        query_results = conn.execute("CALL cpu_qr2()").fetchall()
        print("1")
    elif purpose == "all":
        print("2")
        query_results = conn.execute("CALL cpu_qr({})".format(text)).fetchall() 
    else:
        query_results = conn.execute("CALL cpu_qr3({}, '{}')".format(text, purpose)).fetchall()
        
    conn.close()
    todo_list = []
    for result in query_results:

        item = {
            "id": result[0],
           "make": result[1],
           "price": result[2],
           "clock_speed": result[3],
           "purpose": result[4],
           "num_cores": result[5],
            "qr": result[6],
            "avg": round(result[7],2)
        }
        todo_list.append(item)

    return todo_list
  

def update_task_entry_cpu(task_id: int, price: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update CPU set price = "{}" where cpu_id = {};'.format(float(price), task_id)
    conn.execute(query)
    conn.close()


def insert_new_task_cpu(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    outArray = text.split(",")
    conn = db.connect()
    query = 'Insert Into CPU (cpu_id, make, price, clock_speed, purpose, num_cores) VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(
        outArray[0], outArray[1],outArray[2],outArray[3],outArray[4],outArray[5])
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id_cpu(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From CPU where cpu_id={};'.format(task_id)
    conn.execute(query)
    conn.close()


def seach_for_tasks_cpu(text: str) ->  dict:
    conn = db.connect()
    query = 'SELECT * FROM CPU WHERE '
    que = text.split(",")
    for i in range(len(que)):
        item = que[i].split(':')
        if(i == 0):
            if(item[0] == "make"):
                query += item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "price":
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
            else:
                query += item[0] + " = " + item[1]
        else:
            if(item[0] == "make"):
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "price":
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += " AND " +item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
            else:
                query += " AND " +item[0] + " = " + item[1]
    query +=";"
    print(query)
    conn = db.connect()
     
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "price": result[2],
            "clock_speed": result[3],
            "purpose": result[4],
            "num_cores": result[5],
        }
        todo_list.append(item) 

    return todo_list

def advance_query_cpu(text: str) -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT make,avg(price) From CPU WHERE num_cores > 8 GROUP BY make  UNION SELECT make,avg(price) From CPU GROUP BY make;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": "Nah",
            "make": result[0],
            "price": result[1],
            "clock_speed": "Nah",
            "purpose": "Nah",
            "num_cores": "Nah",
        }
        todo_list.append(item)

    return todo_list

""" RAM """
def fetch_todo_ram() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from RAM;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list


def update_task_entry_ram(task_id: int, price: str) -> None:
    conn = db.connect()
    query = 'Update RAM set price = "{}" where ram_id = {};'.format(float(price), task_id)
    conn.execute(query)
    conn.close()



def insert_new_task_ram(text: str) ->  int:
    conn = db.connect()
    outArray = text.split(",")
    conn = db.connect()
    query = 'Insert Into RAM (ram_id, make, purpose, size, price) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(
        outArray[0], outArray[1],outArray[2],outArray[3],outArray[4])

    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id_ram(task_id: int) -> None:
    conn = db.connect()
    query = 'Delete From RAM where ram_id={};'.format(task_id)
    conn.execute(query)
    conn.close()

#search
def seach_for_tasks_ram(text: str) ->  dict:
    conn = db.connect()
    query = 'SELECT * FROM RAM WHERE '
    que = text.split(",")
    for i in range(len(que)):
        item = que[i].split(':')
        if(i == 0):
            if(item[0] == "make"):
                query += item[0] + " = " + "\""+ item[1] + "\""
                #query += "make LIKE '{0}%'".format(item[1])
            elif item[0] == "purpose":
                query += item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
        else:
            if(item[0] == "make"):
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += " AND " +item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
    query +=";"
    print(query)
    conn = db.connect()
     
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "purpose": result[2],
            "size": result[3],
            "price": result[4],
        }
        todo_list.append(item) 

    return todo_list

def advance_query_ram() -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT purpose,avg(price) From RAM WHERE size > 30 GROUP BY purpose;").fetchall()
    conn.close()
    todo_list = []
    
    for result in query_results:
        item = {
            "id": "NOT APPLICABLE",
            "make": "NOT APPLICABLE",
            "purpose": result[0],
            "size": "NOT APPLICABLE",
            "price": result[1],
        }
        todo_list.append(item) 

    return todo_list

    """ Motherboard """
def fetch_todo_Motherboard() -> dict:

    conn = db.connect()
    query_results = conn.execute("Select * from Motherboard;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "form_factor": result[2],
            "socket": result[3],
            "purpose": result[4],
            "price": result[5],
        }
        todo_list.append(item) 

    return todo_list


def update_task_entry_Motherboard(task_id: int, price: str) -> None:
    conn = db.connect()
    query = 'Update Motherboard set price = "{}" where motherboard_id = {};'.format(float(price), task_id)
    conn.execute(query)
    conn.close()



def insert_new_task_Motherboard(text: str) ->  int:
    conn = db.connect()
    outArray = text.split(",")
    conn = db.connect()
    query = 'Insert Into Motherboard (motherboard_id, make, form_factor, socket, purpose, price) VALUES ("{}", "{}", "{}", "{}", "{}","{}");'.format(
        outArray[0], outArray[1],outArray[2],outArray[3],outArray[4],outArray[5])

    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id_Motherboard(task_id: int) -> None:
    conn = db.connect()
    query = 'Delete From Motherboard where motherboard_id={};'.format(task_id)
    conn.execute(query)
    conn.close()

#search
def seach_for_tasks_Motherboard(text: str) ->  dict:
    conn = db.connect()
    query = 'SELECT * FROM Motherboard WHERE '
    que = text.split(",")
    for i in range(len(que)):
        item = que[i].split(':')
        if(i == 0):
            if(item[0] == "make"):
                query += item[0] + " = " + "\""+ item[1] + "\""
                #query += "make LIKE '{0}%'".format(item[1])
            elif item[0] == "purpose":
                query += item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
        else:
            if(item[0] == "make"):
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            elif item[0] == "purpose":
                query += " AND " +item[0] + " = " + "\""+ item[1] + "\""
            else:
                mini = (item[1].split('-'))[0]
                maxi = (item[1].split('-'))[1]
                query += " AND " +item[0] + " > " + mini + " AND " + item[0] + "<" + maxi
    query +=";"
    print(query)
    conn = db.connect()
     
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "make": result[1],
            "form factor": result[2],
            "socket": result[3],
            "purpose": result[4],
            "price": result[5],
        }
        todo_list.append(item) 

    return todo_list

def advance_query_Motherboard() -> dict:

    conn = db.connect()
    query_results = conn.execute("SELECT purpose,avg(price) From Motherboard WHERE size > 30 GROUP BY purpose;").fetchall()
    conn.close()
    todo_list = []
    
    for result in query_results:
        item = {
            "id": "NOT APPLICABLE",
            "make": "NOT APPLICABLE",
            "purpose": result[0],
            "size": "NOT APPLICABLE",
            "price": result[1],
        }
        item = {
            "id": "NOT APPLICABLE",
            "make": "NOT APPLICABLE",
            "form_factor": "NOT APPLICABLE",
            "socket": "NOT APPLICABLE",
            "purpose": result[0],
            "price": result[1],
        }
        todo_list.append(item) 

    return todo_list

'''mainpage'''
def fetch_todo_main(inputs: list) -> dict:
    conn = db.connect()
    mbi, rami, cpui, monitori, storagei = inputs
    if mbi == -1:
        query_results_motherboard = conn.execute("Select * from Motherboard WHERE motherboard_id = 0;").fetchall()
    else:
        query_results_motherboard = conn.execute("Select * from Motherboard WHERE motherboard_id = {};".format(mbi)).fetchall()
    query_results_ram = conn.execute("Select * from RAM WHERE ram_id = {};".format(rami)).fetchall()
    query_results_cpu = conn.execute("Select * from CPU WHERE cpu_id = {};".format(cpui)).fetchall()
    query_results_monitor = conn.execute("Select * from Monitor WHERE monitor_id = {};".format(monitori)).fetchall()
    query_results_storage = conn.execute("Select * from Storage WHERE storage_id = {};".format(storagei)).fetchall()
    conn.close()
    toreturn = []

    motherboard_list = []
    for result in query_results_motherboard:
        motherboard_list.append(result[0])
        motherboard_list.append(result[1])
        motherboard_list.append(result[2])
        motherboard_list.append(result[3])
        motherboard_list.append(result[4])
        motherboard_list.append(result[5])
    toreturn.append(motherboard_list)

    ram_list = []
    for result in query_results_ram:
        ram_list.append(result[0])
        ram_list.append(result[1])
        ram_list.append(result[2])
        ram_list.append(result[3])
        ram_list.append(result[4])
    toreturn.append(ram_list)
    
    cpu_list = []
    for result in query_results_cpu:
        cpu_list.append(result[0])
        cpu_list.append(result[1])
        cpu_list.append(result[2])
        cpu_list.append(result[3])
        cpu_list.append(result[4])
        cpu_list.append(result[5])
    toreturn.append(cpu_list)

    monitor_list = []
    for result in query_results_monitor:
        monitor_list.append(result[0])
        monitor_list.append(result[1])
        monitor_list.append(result[2])
        monitor_list.append(result[3])
        monitor_list.append(result[4])
    toreturn.append(monitor_list)

    storage_list = []
    for result in query_results_storage:
        storage_list.append(result[0])
        storage_list.append(result[1])
        storage_list.append(result[2])
        storage_list.append(result[3])
        storage_list.append(result[4])
    toreturn.append(storage_list)
    return toreturn
