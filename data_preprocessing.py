import pandas as pd
import os

def read_files():
    ## dtype ensures all entries in the respective column are of the specified type
    item_categories_path = "data\item_categories.csv"
    items_path = "data\items.csv"
    sales_train_path = "data\sales_train.csv"
    sample_submission_path = "data\sample_submission.csv"
    shops_path = "data\shops.csv"
    test_path = "data\\test.csv"

    df_item_categories = pd.read_csv(item_categories_path, dtype={'item_category_name': 'str', 'item_category_id': 'int32'})
    df_items = pd.read_csv(items_path, dtype={'item_name': 'str', 'item_id': 'int32', 'item_category_id': 'int32'})
    df_sales_train = pd.read_csv(sales_train_path, dtype={'date': 'str', 'date_block_num': 'int32', 'shop_id': 'int32', 
                      'item_id': 'int32', 'item_price': 'float32', 'item_cnt_day': 'int32'})
    df_sample_submission = pd.read_csv(sample_submission_path, dtype={'ID': 'int32', 'item_cnt_month':'float32'})
    df_shops = pd.read_csv(shops_path, dtype={'shop_name': 'str', 'shop_id': 'int32'})
    df_test = pd.read_csv(test_path, dtype={'ID': 'int32', 'shop_id': 'int32', 'item_id': 'int32'})

    #print(df_item_categories.head())
    #print(df_items.head())
    #print(df_sales_train.head())
    #print(df_sample_submission.head())
    #print(df_shops.head())
    #print(df_test.head())

    return (df_item_categories, df_items, df_sales_train, df_sample_submission, df_shops, df_test)

if __name__ == "__main__":
    read_files()


