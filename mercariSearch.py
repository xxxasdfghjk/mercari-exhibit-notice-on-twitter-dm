import mercari
import tweepy
import sys
import os
from dotenv import load_dotenv


def itemToDict(item):
    return {"id": item.id, "productURL": item.productURL, "imageURL": item.imageURL, "productName": item.productName, "price": item.price, "status": item.status, "soldOut": item.soldOut}


def sendDirectMessage(sendToScreenName, text):
    auth = tweepy.OAuthHandler(
        os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(os.environ["ACCESS_TOKEN_KEY"],
                          os.environ["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)
    user = api.get_user(screen_name=sendToScreenName)
    api.send_direct_message(user.id_str, text)


def noticeOnTwitter(item):
    sendToScreenName = os.environ["SCREEN_NAME_TO_SEND"]
    text = item["productName"] + "\n" + item["productURL"]
    sendDirectMessage(sendToScreenName, text)


if __name__ == "__main__":
    load_dotenv()
    FIND_ITEM_LIMIT = 3
    if len(sys.argv) <= 1:
        exit()
    searchString = sys.argv[1]
    resultGenerator = mercari.search(searchString)
    count = 0
    for result in resultGenerator:
        noticeOnTwitter(itemToDict(result))
        count = count + 1
        if count == FIND_ITEM_LIMIT:
            break
