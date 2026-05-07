import requests
def get_data(place,forecast=1):
    api="63db469930c47c0ef2b55fbe570b349f"
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    res=requests.get(url)
    data=res.json()
    print(data)
    if data.get("cod") != "200":
        print("Error:", data.get("message"))
        return None
    d1=data['list']
    nr_values=8*forecast
    fd=d1[:nr_values]

    return fd

if __name__=="__main__":
    print(get_data(place="tokyo"))