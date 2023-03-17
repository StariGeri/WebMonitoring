import requests
import time
import functions

# url to check, it can be changed to any websites url
url = "https://triathlon.org/events/start_list/2023_world_triathlon_aquathlon_championships_ibiza/584002"
sleepTime = 600 # 600 sec - 10 min

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
           "Pragma": "no-cache", "Cache-Control": "no-cache"}

response = requests.get(url, headers=headers)


def main():
    #forever loop on purpose, to check the website every {sleepTime} seconds
    #uncomment it to run it forever
    '''while True:
        try:
            if(response.status_code == 200) == True:
                if (functions.websiteCheck(url, response)) == True:
                    print("Website is up and changed! Email sent!")
                else:
                    print("Website is up and not changed!")    

        except:
            print("Website is down, cannot check")   
        time.sleep(sleepTime)'''
        
    try:
        if(response.status_code == 200) == True:
            if (functions.websiteCheck(url, response)) == True:
                print("Website is up and changed! Email sent!")
            else:
                print("Website is up and not changed!")
    except:
        print("Website is down, cannot check")


# glue everything together
if __name__ == "__main__":
    main()
