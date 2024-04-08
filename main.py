from RapidMongo.rapid_mongo import RapidMongo


test_data = [
    {
        "_id": "3",
        "item_name": "Alternating Current",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 4578,
        "category": "Current",
    },
    {
        "_id": "4",
        "item_name": "Alternating Current",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 4578,
        "category": "Current",
    }
]


def main():
    rapid_mongo_obj = RapidMongo(
        db_name="test1", collection="test", data=test_data
    ).insert_data()


if __name__ == "__main__":
    main()
