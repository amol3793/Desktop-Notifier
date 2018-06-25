import feedparser
import notify2
import time
import os


def desktop_notifier(interval_in_seconds):
    feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    notify2.init('News Notify')

    for news in feed['items']:
        print(news['title'])
        print(news['summary'])
        print('\n')

        notification_controler = notify2.Notification(news['title'],
                                 news['summary']
                                 )

        notification_controler.set_urgency(notify2.URGENCY_NORMAL)
        notification_controler.show()
	notification_controler.timeout = 'EXPIRES_DEFAULT'
        time.sleep(interval_in_seconds)


if __name__ == '__main__':
    try:
	set_inerval=input("Please enter the interval (in seconds) of news notification (> 8 sec): ")
        desktop_notifier(set_inerval)
    except:
        print("Error")
