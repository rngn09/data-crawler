# python modules
import os

# tool modules
from datacrawler import ContactDataCrawler

dirname = os.path.dirname(__file__)

INPUT_CSV = os.path.join(dirname, "../examples/csv_input_multi.csv")
INPUT_JSON = os.path.join(dirname, "../examples/json_input_multi.json")

OUTPUT_CSV = os.path.join(dirname, "../examples/csv_output_multi.csv")
OUTPUT_JSON = os.path.join(dirname, "../examples/json_output_multi.json")


def test_store_data_csv_to_json():
    crawler = ContactDataCrawler(input_file=INPUT_CSV,
                                 output_file=OUTPUT_JSON,
                                 reader="default",
                                 writer="default")
    crawler.store_data()
    csv_input_data = crawler.parse_csv_data()

    json_crawler = ContactDataCrawler(input_file=OUTPUT_JSON)
    json_output_data = json_crawler.parse_json_data()

    assert json_output_data == csv_input_data


def test_store_data_csv_to_json_alternative():
    crawler = ContactDataCrawler(input_file=INPUT_CSV,
                                 output_file=OUTPUT_JSON,
                                 reader="nondefault",
                                 writer="nondefault")
    crawler.store_data()
    csv_input_data = crawler.parse_csv_data()

    json_crawler = ContactDataCrawler(input_file=OUTPUT_JSON,
                                      reader="nondefault",
                                      writer="nondefault")
    json_output_data = json_crawler.parse_json_data()
    assert json_output_data == csv_input_data


def test_store_data_json_to_csv():
    crawler = ContactDataCrawler(input_file=INPUT_JSON,
                                 output_file=OUTPUT_CSV,
                                 reader="default",
                                 writer="default")
    crawler.store_data()
    json_input_data = crawler.parse_json_data()

    csv_crawler = ContactDataCrawler(input_file=OUTPUT_CSV)
    csv_output_data = csv_crawler.parse_csv_data()

    assert csv_output_data == json_input_data


def test_store_data_json_to_csv_alternative():
    crawler = ContactDataCrawler(input_file=INPUT_JSON,
                                 output_file=OUTPUT_CSV,
                                 reader="nondefault",
                                 writer="nondefault")
    crawler.store_data()
    json_input_data = crawler.parse_json_data()

    csv_crawler = ContactDataCrawler(input_file=OUTPUT_CSV,
                                     reader="nondefault",
                                     writer="nondefault")
    csv_output_data = csv_crawler.parse_csv_data()
    assert csv_output_data == json_input_data
