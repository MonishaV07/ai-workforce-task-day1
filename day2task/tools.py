import requests


def get_exchange_rate():
    """
    Fetch the current USD to INR exchange rate
    from an external exchange-rate service.
    """

    url = "https://open.er-api.com/v6/latest/USD"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        raise RuntimeError("Exchange-rate API failed.")

    rate = data["rates"]["INR"]

    return {
        "base_currency": "USD",
        "target_currency": "INR",
        "rate": rate
    }


def calculate_prize_inr(usd_amount, exchange_rate):
    """
    Convert a USD amount into INR.
    """

    return usd_amount * exchange_rate