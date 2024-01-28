from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


def calculateAge(birthDate):
  today = date.today()
  age = today.year - birthDate.year - ((today.month, today.day) <
                                       (birthDate.month, birthDate.day))

  return age


def getMonth(days):

  global mon, day, m_int

  if days <= 31:
    day = days
    mon = "Jan"
    m_int = 1

  elif days <= 59:
    day = days - 32
    mon = "Feb"
    m_int = 2

  elif days <= 90:
    day = days - 60
    mon = "Mar"
    m_int = 3

  elif days <= 120:
    day = days - 91
    mon = "Apr"
    m_int = 4

  elif days <= 151:
    day = days - 121
    mon = "May"
    m_int = 5

  elif days <= 181:
    day = days - 152
    mon = "Jun"
    m_int = 6

  elif days <= 212:
    day = days - 182
    mon = "Jul"
    m_int = 7

  elif days <= 243:
    day = days - 213
    mon = "Arg"
    m_int = 8

  elif days <= 273:
    day = days - 244
    mon = "Sep"
    m_int = 9

  elif days <= 304:
    day = days - 273
    mon = "Oct"
    m_int = 10

  elif days <= 334:
    day = days - 305
    mon = "Now"
    m_int = 11

  elif days <= 365:
    day = days - 335
    mon = "Dec"
    m_int = 12

  else:
    day = "Enter Valied NIC Number"
    mon = "Enter Valied NIC Number"


def genter(days):
  global gen
  if days > 500:
    gen = "Female"
    getMonth(int(days - 500))

  elif days < 500:
    gen = "Male"
    getMonth(int(days))

  else:
    gen = "Enter Valied NIC Number"


def fDob(nic):
  global year

  if len(nic) == 12:
    year = nic[0:4]
    month = genter(int(nic[4:7]))

  elif len(nic) == 10:
    year = f"19{nic[0:2]}"
    month = genter(int(nic[2:5]))

  else:
    year = "Enter Valied NIC Number"

  if (year or mon or day or gen) == "Enter Valied NIC Number":
    return "Enter Valied NIC Number"
  else:
    dob = [year, mon, day, gen, m_int]
    return dob


@app.route('/')
def home():
  return render_template("index.html")


@app.route('/getNic', methods=["GET", "POST"])
def passNic():
  try:
    if request.method == "GET":
      nic = request.args.get('nic')
      if nic == "":
        return render_template("errr.html", error="Enter NIC Number")
      else:
        dob = fDob(nic)
        #print(nic)
        if dob == "Enter Valied NIC Number":
          return render_template("errr.html", error="Enter Valied NIC Number")
        else:
          age = calculateAge(date(int(dob[0]), int(dob[4]), int(dob[2])))
          year = f"{dob[0]}-{dob[1]}-{dob[2]}"
          gen = dob[3]
          #print(f"{age}")
          return render_template("otp.html", year=year, gen=gen, age=age)
    else:
      return render_template("index.html")
  except:
    return render_template("index.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
