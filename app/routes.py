""" Specifies routing for the application"""
from flask import render_template, request, jsonify, session
from app import app
from app import database as db_helper

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        if(session['page'] == "monitor"):
            db_helper.remove_task_by_id_monitor(task_id)
        elif session['page'] == "storage":
            db_helper.remove_task_by_id_storage(task_id)
        elif session['page'] == "cpu":
            db_helper.remove_task_by_id_cpu(task_id)
        elif session['page'] == "ram":
            db_helper.remove_task_by_id_ram(task_id)
        elif session['page'] == "motherboard":
            db_helper.remove_task_by_id_Motherboard(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        if(session['page'] == "monitor"):
            db_helper.update_task_entry_monitor(task_id, data["description"])
        elif session['page'] == "storage":
            db_helper.update_task_entry_storage(task_id,data["description"])
        elif session['page'] == "cpu":
            db_helper.update_task_entry_cpu(task_id,data["description"])
        elif session['page'] == "ram":
            db_helper.update_task_entry_ram(task_id,data["description"])
        elif session['page'] == "motherboard":
            db_helper.update_task_entry_Motherboard(task_id,data["description"])
        result = {'success': True, 'response': 'Task Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
 
    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    if(session['page'] == "monitor"):
        db_helper.insert_new_task_monitor(data["description"])
    elif session['page'] == "storage":
        db_helper.insert_new_task_storage(data["description"])
    elif session['page'] == "cpu":
        db_helper.insert_new_task_cpu(data["description"])
    elif session['page'] == "ram":
        db_helper.insert_new_task_ram(data["description"])
    elif session['page'] == "motherboard":
        db_helper.insert_new_task_Motherboard(data["description"])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

""" search """
@app.route("/search", methods=['POST'])
def search():
    data = request.get_json()
    session["cmd"] = 1
    session['select'] = data["description"]

    try:
        if(session['page'] == "monitor"):
            db_helper.seach_for_tasks_monitor(data["description"])
        elif session['page'] == "storage":
            db_helper.seach_for_tasks_storage(data["description"])
        elif session['page'] == "cpu":
            db_helper.seach_for_tasks_cpu(data["description"])
        elif session['page'] == "ram":
            db_helper.seach_for_tasks_ram(data["description"])
        elif session['page'] == "motherboard":
            db_helper.seach_for_tasks_Motherboard(data["description"])
        result = {'success': True, 'response': 'Task Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

""" advance """
@app.route("/advance", methods=['POST'])
def advance():
    #data = request.get_json()
    print("advance is working")
    try:
    
        session['cmd'] = 2
        
        result = {'success': True, 'response': 'Task Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)    

@app.route("/monitor")
def monitor():
    """ returns rendered homepage """
    session['page'] = "monitor"
    try :
        selectedMonitor = session["monitorselect"]
        cmd = session['cmd'] 
        print(cmd)
        if cmd == 1:
            value = session.get('select', None)
            items = db_helper.seach_for_tasks_monitor(str(value))
            session['cmd']  = 0
        elif cmd == 2 : 
            items = db_helper.advance_query_monitor()
            session['cmd']  = 0
        else : 
            items = db_helper.fetch_todo_monitor()
    except : 
        selectedMonitor = "none"
        items = db_helper.fetch_todo_monitor()
    return render_template("monitor.html", items=items, chosenMonitor = selectedMonitor)


@app.route("/storage")
def storage():
    """ returns rendered homepage """
   
    session['page'] = "storage"
    try :
        selectStorage = session["storageselect"]
        cmd = session['cmd'] 
        print(cmd)
        if cmd == 1:
            value = session.get('select', None)
            items = db_helper.seach_for_tasks_storage(str(value))
            session['cmd']  = 0
        elif cmd == 2 : 
            items = db_helper.advance_query_storage()
            session['cmd']  = 0
        else : 
            items = db_helper.fetch_todo_storage()
    except : 
        selectStorage = "none"
        items = db_helper.fetch_todo_storage()
    return render_template("storage.html", items=items, chosenStorage = selectStorage)

@app.route("/ram")
def ram():
    """ returns rendered homepage """
   
    session['page'] = "ram"
    try :
        selectedRam = session["ramselect"]
        cmd = session['cmd'] 
        print(cmd)
        if cmd == 1:
            value = session.get('select', None)
            items = db_helper.seach_for_tasks_ram(str(value))
            session['cmd']  = 0
        elif cmd == 2 : 
            items = db_helper.advance_query_ram()
            session['cmd']  = 0
        else : 
            items = db_helper.fetch_todo_ram()
    except : 
        items = db_helper.fetch_todo_ram()
        selectedRam = session["none"]

    return render_template("ram.html", items=items, chosenRAM = selectedRam)

@app.route("/motherboard")
def motherboard():
    """ returns rendered homepage """
   
    session['page'] = "motherboard"
    try :
        cmd = session['cmd'] 
        selectedMD = session["motherboardselect"]
        print(cmd)
        if cmd == 1:
            value = session.get('select', None)
            items = db_helper.seach_for_tasks_Motherboard(str(value))
            session['cmd']  = 0
        elif cmd == 2 : 
            items = db_helper.advance_query_Motherboard()
            session['cmd']  = 0
        else : 
            items = db_helper.fetch_todo_Motherboard()
    except : 
        items = db_helper.fetch_todo_Motherboard()
        selectedMD = "none"
    return render_template("motherboard.html", items=items, chosenMD = selectedMD)

@app.route("/cpu")
def cpu():
    """ returns rendered homepage """
   
    session['page'] = "cpu"
    motherboard_id = session["motherboardselect"]
    try :
        print("1")
        cmd = session['cmd'] 
        selctedCpu = session["cpuselect"]
        purpose = session["purpose"]
        
        print("1.5")
        if cmd == 1:
            value = session.get('select', None)
            items = db_helper.seach_for_tasks_cpu(str(value))
            session['cmd']  = 0
        elif cmd == 2 : 
            items = db_helper.advance_query_cpu()
            session['cmd']  = 0
        else : 
            items = db_helper.fetch_todo_cpu(motherboard_id, purpose)
    except: 
        items = db_helper.fetch_todo_cpu(motherboard_id,purpose)
        print("2")
        selctedCpu = "none"
    print(selctedCpu)
    return render_template("cpu.html", items=items, AlreadySelectedCpu = selctedCpu)

@app.route("/")
def homepage():
    session['cmd'] = 0
    session['select'] = "none"
    try: 
        purpose = session["purpose"]
    except : 
        session["purpose"] = "all"
        purpose = session["purpose"]
    try:
        sec = session['cpuselect']
    except:
        session['cpuselect'] = 130
    try:
        sec = session['monitorselect']
    except:
        session['monitorselect'] = 130
    try:
        sec = session['ramselect']
    except:
        session['ramselect'] = 130
    try:
        sec = session['motherboardselect']
    except:
        session['motherboardselect'] = 0
    try:
        sec = session['storageselect']
    except:
        session['storageselect'] = 130
    try:
        sec = session['gpuselect']
    except:
        session['gpuselect'] = 130

    inputs = []
    for i in ['motherboardselect', 'ramselect', 'cpuselect', 'monitorselect', 'storageselect']:
        inputs.append(session[i])
        print(session[i])
    items = db_helper.fetch_todo_main(inputs)
    print(inputs)
    return render_template("homepage.html", items = items, pindex = purpose)


@app.route("/purpose", methods=['POST'])
def purpose():
    data = request.get_json()
    session["cmd"] = 1
    session['purpose'] = data["description"]
    try:
        result = {'success': True, 'response': 'Task Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/select/<int:task_id>", methods=['POST'])
def select(task_id):
    """ recieved post requests for entry delete """
    if(session['page'] == "monitor"):
        session["monitorselect"] = task_id
    elif session['page'] == "storage":
        session["storageselect"] = task_id
    elif session['page'] == "cpu":
        session["cpuselect"] = task_id
    elif session['page'] == "ram":
        session["ramselect"] = task_id
    elif session['page'] == "motherboard":
        session["motherboardselect"] = task_id
    print("motherboard:{}".format(session["motherboardselect"]))

    try:
        result = {'success': True, 'response': 'Select task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

    

