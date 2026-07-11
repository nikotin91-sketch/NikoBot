from btcturk_api import get_markets


def main():

    print("BtcTurk bağlantı testi başlıyor...")

    markets = get_markets()

    if markets:

        print(
            "Bağlantı başarılı!"
        )

        print(
            "Bulunan TRY çiftleri:"
        )

        print(
            markets[:20]
        )

    else:

        print(
            "Market verisi alınamadı."
        )



if __name__ == "__main__":

    main()
