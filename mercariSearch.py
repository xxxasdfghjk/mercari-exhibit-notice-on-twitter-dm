from os import access
import mercari
import tweepy
from dotenv import dotenv_values


def itemToDict(item):
    return {"id": item.id, "productURL": item.productURL, "imageURL": item.imageURL, "productName": item.productName, "price": item.price, "status": item.status, "soldOut": item.soldOut}


def sendDirectMessage(sendToScreenName, text):
    envs = dotenv_values(".env")
    auth = tweepy.OAuthHandler(envs["CONSUMER_KEY"], envs["CONSUMER_SECRET"])
    auth.set_access_token(envs["ACCESS_TOKEN_KEY"],
                          envs["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)
    user = api.get_user(screen_name=sendToScreenName)
    api.send_direct_message(user.id_str, text)


def noticeOnTwitter(item):
    sendToScreenName = "xxxasdfghjk"
    text = item["productName"] + "\n" + item["productURL"]
    sendDirectMessage(sendToScreenName, text)


if __name__ == "__main__":
    searchString = "stream palette"
    resultGenerator = mercari.search(searchString)
    for result in resultGenerator:
        noticeOnTwitter(itemToDict(result))
