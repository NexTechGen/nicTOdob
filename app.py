from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def getMonth(days):

  global mon, day

  if days <= 31:
    day = days
    mon = "Jan"

  elif days <= 59:
    day = days - 32
    mon = "Feb"

  elif days <= 90:
    day = days - 60
    mon = "Mar"

  elif days <= 120:
    day = days - 91
    mon = "Apr"

  elif days <= 151:
    day = days - 121
    mon = "May"

  elif days <= 181:
    day = days - 152
    mon = "Jun"

  elif days <= 212:
    day = days - 182
    mon = "Jul"

  elif days <= 243:
    day = days - 213
    mon = "Arg"

  elif days <= 273:
    day = days - 244
    mon = "Sep"

  elif days <= 304:
    day = days - 273
    mon = "Oct"

  elif days <= 334:
    day = days - 305
    mon = "Now"

  elif days <= 365:
    day = days - 335
    mon = "Dec"

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
    dob = [year, mon, day, gen]
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
          year = f"{dob[0]}/{dob[1]}/{dob[2]}"
          gen = dob[3]
          return render_template("otp.html", year = year, gen = gen)
    else:
      return render_template("index.html")
  except:
    return render_template("index.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
