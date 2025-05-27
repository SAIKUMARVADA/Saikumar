pip install FastAPI
pip unicorn
from FastAPI , HTTException, Request
from pydantic import BaseModel

import Logging
import json

Logging.baseconfig(
    filename = 'employee_app.log',
    Level = Logging.INFO,
    formal = '%(asctime)s_%(levelname)s_%(message)s'
)

logging = loging.get logger(__name__)

app = fastAPI(title = 'Employee search API')
#====BaseModel====
class Project(BaseModel):
    Project id = str
    Name : str
    Status: str

class Employee(BaseModel):
    Emp id : str 
    name : str
    department : str
    salary :int
    designation : str
    location : str
    dob : str
    projects :list[Project]

class login Request(BaseModel):
    username : str
    password : str
     
#==== Loademployee data ====
with open("Employee details:json","r")as f:
  row Employee = json.loads(f)
Employees = [Employee(**emp) for emp in row employees]

@app.get("/employees":
    response_model = list[Employee])

async def get_all_employees
    return Employees


 @app.post("/Login")
 async def login_user(data: login Request
                      if data.username == "Sai" and data.password=="Sainani":)
                          return{"Message:login Successfull"}
raise HTTPException(status_code.401,detail="Login Failed")
                  
@app.get("/employees/bench",response_model = list[Employee])
async def get_employees_on_bench():
    return[emp for emp in Employees if not emp.projects]

@app.get("/employees/project_status/{status}", response_model = list[Employee])

async def get_employees_by_project.status(status:str):
    return[emp for emp in Employeesif any (p.status==status for pin emp.projects)]
                      
    
