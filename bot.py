from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage

import logging
import dialog

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

logger = logging.getLogger(__name__)
app = Flask(__name__)
viber = Api(BotConfiguration(
    name='SportLife',
    avatar='http://www.sportlife.be/img/logo_large.png',
    auth_token='4544b19471350c4b-78b3fb637fd3b07c-4a124e0b24287067'
))

# viber.set_webhook('https://2aab3c73.ngrok.io/')

@app.route('/', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        # message = viber_request.message
        app.logger.debug(viber_request)
        res_json = dialog.get_response(viber_request, viber)
        # sticker = StickerMessage(sticker_id=40100)

        # lets echo back
        viber.send_messages(viber_request.sender.id, res_json)
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
