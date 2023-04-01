from etl import ETL
from datetime import date
from id_fetcher import get_all_plaza_ids
import concurrent.futures
from functools import partial


def create_etl_object_and_run(plaza_id, db_file_path, db_table_name):
    plaza_etl = ETL(plaza_id, db_file_path, db_table_name)
    plaza_etl.run_etl()


if __name__ == "__main__":
    db_file_path = 'toll_datak.db'
    db_table_name = f'toll_data{date.today()}'
    ids = get_all_plaza_ids()[:100]
    partial_etl_function = partial(create_etl_object_and_run, db_file_path=db_file_path, db_table_name=db_table_name)
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        executor.map(partial_etl_function, ids)