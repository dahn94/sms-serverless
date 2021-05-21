from chalice import Chalice, Response
from twilio.base.exceptions import TwilioRestException
from chalicelib import sms

app = Chalice(app_name="sms-serverless")


@app.route("/service/sms/send", methods=["POST"])
def send_sms():
    request_body = app.current_request.json_body
    if request_body:
        try:
            resp = sms.send(request_body)
            if resp:
                return Response(
                    status_code=201,
                    headers={"Content-Type": "application/json"},
                    body={
                        "status": "successo",
                        "data": resp.sid,
                        "message": "SMS enviado com sucesso",
                    },
                )
            else:
                return Response(
                    status_code=200,
                    headers={"Content-Type": "application/json"},
                    body={
                        "status": "falha",
                        "message": "Por favor, tente novamente!!!",
                    },
                )
        except TwilioRestException as exc:
            return Response(
                status_code=400,
                headers={"Content-Type": "application/json"},
                body={"status": "failure", "message": exc.msg},
            )