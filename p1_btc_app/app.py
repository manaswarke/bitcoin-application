from bottle import *
import requests

application = Bottle()

@application.route("/", method=["POST", "GET"])
def home():
    if request.method == "POST":
        try:
            noc = int(request.forms.get("noc"))
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
            res = requests.get(url)
            data = res.json()
            PRICE = data["bitcoin"]["inr"]
            amt = noc * PRICE
            msg = "Amount = ₹ " + str(round(amt, 2))
            return template("home.tpl", msg=msg)
        except ValueError:
            msg = "please enter integers only"
            return template("home.tpl", msg=msg)
        except Exception as e:
            msg = "issue " + str(e)
            return template("home.tpl", msg=msg)
    else:
        return template("home.tpl", msg="")

run(application, host="localhost", port=4050, debug=True, reloader=True)