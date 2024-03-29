import random

import httpx


def random_user_agents():
    """returns random user-agents from the list"""
    UA = user_agent_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    ]

    return random.choice(UA)


def whatismyip():
    from bs4 import BeautifulSoup

    # set user-agent
    headers = {"User-Agent": random_user_agents()}

    response = httpx.get("https://whatismyip.com", headers=headers)

    status_code = response.status_code
    if status_code == 403:
        print(f"Status code: {status_code}. Forbidden")
    elif status_code == 200:
        print(f"Status code: {status_code}. Success")

    soup = BeautifulSoup(response.text, "lxml")

    ip_info = soup.find_all("li", class_="py-1")

    for i in range(len(ip_info)):
        temp = ip_info[i]
        if temp:
            print(temp.text)
        else:
            continue


def ip_info():
    """using https://ipinfo.io/json to get the ip address & others"""
    # set user-agent
    headers = {"User-Agent": random_user_agents()}

    res = httpx.get("https://ipinfo.io/json", headers=headers)

    if res.status_code == 200:
        data = res.json()

        print(
            f"""
            IP: {data['ip']}
            City: {data['city']}
            Region: {data['region']}
            County: {data['country']}
            Location: {data['loc']}
            Organization: {data['org']}
            Timezone: {data['timezone']}
            """
        )
    else:
        print(f"[--] ERROR: status code => {res.status_code}")


def check_conn():
    try:
        print("[--] Checking internet connection.....")
        res = httpx.get("https://google.com")
        if res.status_code == 200:
            print("[--] All good.....\n")
    except httpx.ConnectError:
        print("[--] ERROR: No internet connection.")
        exit(123)


if __name__ == "__main__":
    check_conn()
    ip_info()
