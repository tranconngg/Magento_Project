# # # # # import pandas as pd
# # # # # df=pd.read_csv("/home/trancong/Downloads/iphonee_products.csv")
# # # # # df['categories']='Iphone'
# # # # # df['product_type']='simple'

# # # # # df['visibility'] = df['visibility'].replace('Catalog,Search', 'Catalog, Search')

# # # # # # # In ra cột 'visibility' để kiểm tra
# # # # # # print(df['visibility'])

# # # # # df.to_csv("/home/trancong/Downloads/iphonee_products.csv", index=False)
# # # # # print("done")
# # # # # print(df.info())
# # # # import pandas as pd

# # # # # Dữ liệu sản phẩm
# # # # data = {
# # # #     'sku': ['IPHONE-8', 'IPHONE-XS', 'IPHONE-XR', 'IPHONE-SE', 'IPHONE-11', 
# # # #             'IPHONE-12-PRO', 'IPHONE-12', 'IPHONE-13-PRO-MAX', 'IPHONE-13-PRO', 'IPHONE-13'],
# # # #     'attribute_set_code': ['Default'] * 10,
# # # #     'product_type': ['simple'] * 10,
# # # #     'visibility': ['Catalog, Search'] * 10,
# # # #     'name': ['iPhone 8', 'iPhone XS', 'iPhone XR', 'iPhone SE', 'iPhone 11', 
# # # #              'iPhone 12 Pro', 'iPhone 12', 'iPhone 13 Pro Max', 'iPhone 13 Pro', 'iPhone 13'],
# # # #     'price': [499.99, 799.99, 649.99, 399.99, 599.99, 899.99, 699.99, 1099.99, 999.99, 799.99],
# # # #     'quantity': [10] * 10,  # Số lượng tồn kho
# # # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # # #     'description': [
# # # #         "Smartphone iPhone 8 with Retina display, A11 Bionic chip.",
# # # #         "Smartphone iPhone XS with Super Retina OLED display, A12 Bionic chip.",
# # # #         "Smartphone iPhone XR with LCD 6.1 inch, A12 Bionic chip.",
# # # #         "Smartphone iPhone SE with Retina 4 inch, A9 chip.",
# # # #         "Smartphone iPhone 11 with LCD 6.1 inch, A13 Bionic chip.",
# # # #         "Smartphone iPhone 12 Pro with OLED display, A14 Bionic chip.",
# # # #         "Smartphone iPhone 12 with OLED display, A14 Bionic chip.",
# # # #         "Smartphone iPhone 13 Pro Max with OLED 6.7 inch, A15 Bionic chip.",
# # # #         "Smartphone iPhone 13 Pro with OLED 6.1 inch, A15 Bionic chip.",
# # # #         "Smartphone iPhone 13 with OLED 6.1 inch, A15 Bionic chip."
# # # #     ],
# # # #     'categories': ['Iphone'] * 10  # Thêm cột categories với giá trị giống nhau cho tất cả sản phẩm
# # # # }

# # # # # Tạo DataFrame
# # # # df = pd.DataFrame(data)

# # # # # Xuất DataFrame ra file CSV
# # # # df.to_csv('/home/trancong/Downloads/ip_products_with_categories.csv', index=False)

# # # # # Hiển thị DataFrame
# # # # print(df)

# # # # import pandas as pd

# # # # # Dữ liệu sản phẩm Oppo
# # # # data = {
# # # #     'sku': ['OPPO-A57', 'OPPO-RENO5', 'OPPO-F11', 'OPPO-A94', 'OPPO-RENO7', 
# # # #             'OPPO-F21-PRO', 'OPPO-A74', 'OPPO-RENO8', 'OPPO-FIND-X3', 'OPPO-FIND-X5'],
# # # #     'attribute_set_code': ['Default'] * 10,
# # # #     'product_type': ['simple'] * 10,
# # # #     'visibility': ['Catalog, Search'] * 10,
# # # #     'name': ['Oppo A57', 'Oppo Reno5', 'Oppo F11', 'Oppo A94', 'Oppo Reno7', 
# # # #              'Oppo F21 Pro', 'Oppo A74', 'Oppo Reno8', 'Oppo Find X3', 'Oppo Find X5'],
# # # #     'price': [4699000, 7990000, 5990000, 7290000, 9990000, 8590000, 6490000, 12990000, 15990000, 23990000],
# # # #     'quantity': [20] * 10,  # Số lượng tồn kho
# # # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # # #     'description': [
# # # #         "Oppo A57 with IPS LCD display and MediaTek MT6765G processor.",
# # # #         "Oppo Reno5 with AMOLED display and Snapdragon 720G processor.",
# # # #         "Oppo F11 with LCD display and MediaTek Helio P70 processor.",
# # # #         "Oppo A94 with AMOLED display and MediaTek Helio P95 processor.",
# # # #         "Oppo Reno7 with AMOLED display and MediaTek Dimensity 900 processor.",
# # # #         "Oppo F21 Pro with AMOLED display and Snapdragon 680 processor.",
# # # #         "Oppo A74 with AMOLED display and Snapdragon 662 processor.",
# # # #         "Oppo Reno8 with AMOLED display and MediaTek Dimensity 1300 processor.",
# # # #         "Oppo Find X3 with AMOLED display and Snapdragon 870 processor.",
# # # #         "Oppo Find X5 with AMOLED display and Snapdragon 888 processor."
# # # #     ],
# # # #     'categories': ['Category/Oppo'] * 10  # Danh mục sản phẩm
# # # # }

# # # # # Tạo DataFrame
# # # # df_oppo = pd.DataFrame(data)

# # # # # Xuất DataFrame ra file CSV
# # # # df_oppo.to_csv('/home/trancong/Downloads/oppo_products_vnd.csv', index=False)

# # # # # Hiển thị DataFrame
# # # # print(df_oppo)
# # # import pandas as pd

# # # # Dữ liệu sản phẩm Samsung với mô tả thông số kỹ thuật
# # # data = {
# # #     'sku': ['SAMSUNG-S23-ULTRA', 'SAMSUNG-ZFOLD5', 'SAMSUNG-A54', 
# # #             'SAMSUNG-S23', 'SAMSUNG-M14', 'SAMSUNG-A73', 
# # #             'SAMSUNG-S21', 'SAMSUNG-NOTE20', 'SAMSUNG-A34', 'SAMSUNG-S22-PLUS'],
# # #     'attribute_set_code': ['Default'] * 10,
# # #     'product_type': ['simple'] * 10,
# # #     'visibility': ['Catalog, Search'] * 10,
# # #     'name': ['Samsung Galaxy S23 Ultra', 'Samsung Galaxy Z Fold 5', 'Samsung Galaxy A54', 
# # #              'Samsung Galaxy S23', 'Samsung Galaxy M14', 'Samsung Galaxy A73', 
# # #              'Samsung Galaxy S21', 'Samsung Galaxy Note 20', 'Samsung Galaxy A34', 'Samsung Galaxy S22 Plus'],
# # #     'price': [29990000, 41990000, 8490000, 24990000, 5490000, 12490000, 
# # #               20990000, 19990000, 7990000, 23990000],
# # #     'quantity': [15] * 10,  # Số lượng tồn kho
# # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # #     'description': [
# # #         "Màn hình: 6.8 inch Dynamic AMOLED 2X, 120Hz, 3088 x 1440 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 2\n"
# # #         "RAM: 12GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB/1TB\n"
# # #         "Camera: 200MP + 12MP + 10MP + 10MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 45W",
        
# # #         "Màn hình: 7.6 inch Dynamic AMOLED 2X, 120Hz, 2176 x 1812 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 2\n"
# # #         "RAM: 12GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB/1TB\n"
# # #         "Camera: 50MP + 12MP + 10MP\n"
# # #         "Pin: 4400mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.4 inch Super AMOLED, 120Hz, 2340 x 1080 pixel\n"
# # #         "Chip xử lý: Exynos 1380\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 12MP + 5MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.1 inch Dynamic AMOLED 2X, 120Hz, 2340 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 2\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 12MP + 10MP\n"
# # #         "Pin: 3900mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.6 inch PLS LCD, 90Hz, 2408 x 1080 pixel\n"
# # #         "Chip xử lý: Exynos 1330\n"
# # #         "RAM: 4GB/6GB\n"
# # #         "Bộ nhớ trong: 64GB/128GB\n"
# # #         "Camera: 50MP + 2MP + 2MP\n"
# # #         "Pin: 6000mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.7 inch Super AMOLED Plus, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 778G\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 108MP + 12MP + 5MP + 5MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.2 inch Dynamic AMOLED 2X, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Exynos 2100\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 12MP + 12MP + 64MP\n"
# # #         "Pin: 4000mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.7 inch Super AMOLED Plus, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Exynos 990\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 256GB\n"
# # #         "Camera: 108MP + 12MP + 12MP\n"
# # #         "Pin: 4300mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.6 inch Super AMOLED, 120Hz, 2340 x 1080 pixel\n"
# # #         "Chip xử lý: Dimensity 1080\n"
# # #         "RAM: 6GB/8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 48MP + 8MP + 5MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 25W",
        
# # #         "Màn hình: 6.6 inch Dynamic AMOLED 2X, 120Hz, 2340 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 1\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 12MP + 10MP\n"
# # #         "Pin: 4500mAh, sạc nhanh 45W"
# # #     ],
# # #     'categories': ['Category/Samsung'] * 10  # Danh mục sản phẩm
# # # }

# # # # Tạo DataFrame
# # # df_samsung = pd.DataFrame(data)

# # # # Xuất DataFrame ra file CSV
# # # df_samsung.to_csv('/home/trancong/Downloads/samsung_products_specs.csv', index=False)

# # # # Hiển thị DataFrame
# # # print(df_samsung)

# # # import pandas as pd

# # # # Dữ liệu sản phẩm Xiaomi với mô tả thông số kỹ thuật
# # # data = {
# # #     'sku': ['XIAOMI-13-PRO', 'XIAOMI-12T-PRO', 'XIAOMI-REDMI-NOTE12', 
# # #             'XIAOMI-MI11-LITE', 'XIAOMI-REDMI-A2', 'XIAOMI-POCO-F5', 
# # #             'XIAOMI-REDMI-K60', 'XIAOMI-MIX-FOLD3', 'XIAOMI-REDMI-NOTE11', 'XIAOMI-12X'],
# # #     'attribute_set_code': ['Default'] * 10,
# # #     'product_type': ['simple'] * 10,
# # #     'visibility': ['Catalog, Search'] * 10,
# # #     'name': ['Xiaomi 13 Pro', 'Xiaomi 12T Pro', 'Xiaomi Redmi Note 12', 
# # #              'Xiaomi Mi 11 Lite', 'Xiaomi Redmi A2', 'Xiaomi Poco F5', 
# # #              'Xiaomi Redmi K60', 'Xiaomi Mix Fold 3', 'Xiaomi Redmi Note 11', 'Xiaomi 12X'],
# # #     'price': [29990000, 16990000, 5990000, 8490000, 2990000, 9490000, 
# # #               12490000, 41990000, 4590000, 14990000],
# # #     'quantity': [20] * 10,  # Số lượng tồn kho
# # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # #     'description': [
# # #         "Màn hình: 6.73 inch AMOLED, 120Hz, 3200 x 1440 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 2\n"
# # #         "RAM: 12GB/16GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB\n"
# # #         "Camera: 50MP + 50MP + 50MP\n"
# # #         "Pin: 4820mAh, sạc nhanh 120W",
        
# # #         "Màn hình: 6.67 inch AMOLED, 120Hz, 2712 x 1220 pixel\n"
# # #         "Chip xử lý: Snapdragon 8+ Gen 1\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 200MP + 8MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 120W",
        
# # #         "Màn hình: 6.67 inch AMOLED, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 685\n"
# # #         "RAM: 6GB/8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 8MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 33W",
        
# # #         "Màn hình: 6.55 inch AMOLED, 90Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 732G\n"
# # #         "RAM: 6GB/8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 64MP + 8MP + 5MP\n"
# # #         "Pin: 4250mAh, sạc nhanh 33W",
        
# # #         "Màn hình: 6.52 inch IPS LCD, 60Hz, 1600 x 720 pixel\n"
# # #         "Chip xử lý: MediaTek Helio G36\n"
# # #         "RAM: 2GB/3GB\n"
# # #         "Bộ nhớ trong: 32GB/64GB\n"
# # #         "Camera: 8MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 10W",
        
# # #         "Màn hình: 6.67 inch AMOLED, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 7+ Gen 2\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB\n"
# # #         "Camera: 64MP + 8MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 67W",
        
# # #         "Màn hình: 6.67 inch AMOLED, 120Hz, 3200 x 1440 pixel\n"
# # #         "Chip xử lý: Snapdragon 8+ Gen 1\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 64MP + 8MP + 2MP\n"
# # #         "Pin: 5500mAh, sạc nhanh 67W",
        
# # #         "Màn hình: 8.03 inch AMOLED, 120Hz, 2160 x 1914 pixel\n"
# # #         "Chip xử lý: Snapdragon 8 Gen 2\n"
# # #         "RAM: 12GB/16GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB/1TB\n"
# # #         "Camera: 50MP + 50MP + 10MP\n"
# # #         "Pin: 4800mAh, sạc nhanh 67W",
        
# # #         "Màn hình: 6.43 inch AMOLED, 90Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 680\n"
# # #         "RAM: 4GB/6GB\n"
# # #         "Bộ nhớ trong: 64GB/128GB\n"
# # #         "Camera: 50MP + 8MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 33W",
        
# # #         "Màn hình: 6.28 inch AMOLED, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 870\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 13MP + 5MP\n"
# # #         "Pin: 4500mAh, sạc nhanh 67W"
# # #     ],
# # #     'categories': ['Category/Xiaomi'] * 10  # Danh mục sản phẩm
# # # }

# # # # Tạo DataFrame
# # # df_xiaomi = pd.DataFrame(data)

# # # # Xuất DataFrame ra file CSV
# # # df_xiaomi.to_csv('/home/trancong/Downloads/xiaomi_products_specs.csv', index=False)

# # # # Hiển thị DataFrame
# # # print(df_xiaomi)
# # # import pandas as pd

# # # # Dữ liệu sản phẩm Vivo với mô tả thông số kỹ thuật
# # # data = {
# # #     'sku': ['VIVO-X90-PRO', 'VIVO-Y36', 'VIVO-V29', 'VIVO-T2-PRO', 'VIVO-Y78', 
# # #             'VIVO-V27', 'VIVO-X80', 'VIVO-Y22', 'VIVO-S16', 'VIVO-Y100'],
# # #     'attribute_set_code': ['Default'] * 10,
# # #     'product_type': ['simple'] * 10,
# # #     'visibility': ['Catalog, Search'] * 10,
# # #     'name': ['Vivo X90 Pro', 'Vivo Y36', 'Vivo V29', 'Vivo T2 Pro', 'Vivo Y78', 
# # #              'Vivo V27', 'Vivo X80', 'Vivo Y22', 'Vivo S16', 'Vivo Y100'],
# # #     'price': [29990000, 6990000, 10990000, 8490000, 7990000, 
# # #               10990000, 19990000, 4990000, 11990000, 9990000],
# # #     'quantity': [20] * 10,  # Số lượng tồn kho
# # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # #     'description': [
# # #         "Màn hình: 6.78 inch AMOLED, 120Hz, 2800 x 1260 pixel\n"
# # #         "Chip xử lý: MediaTek Dimensity 9200\n"
# # #         "RAM: 12GB/16GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB\n"
# # #         "Camera: 50MP + 50MP + 12MP\n"
# # #         "Pin: 4870mAh, sạc nhanh 120W",
        
# # #         "Màn hình: 6.64 inch IPS LCD, 120Hz, 2388 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 680\n"
# # #         "RAM: 6GB/8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 44W",
        
# # #         "Màn hình: 6.78 inch AMOLED, 120Hz, 2800 x 1260 pixel\n"
# # #         "Chip xử lý: Snapdragon 778G\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 8MP + 2MP\n"
# # #         "Pin: 4600mAh, sạc nhanh 80W",
        
# # #         "Màn hình: 6.62 inch AMOLED, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: MediaTek Dimensity 7200\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 64MP + 2MP\n"
# # #         "Pin: 4600mAh, sạc nhanh 66W",
        
# # #         "Màn hình: 6.64 inch AMOLED, 120Hz, 2388 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 695\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 64MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 44W",
        
# # #         "Màn hình: 6.78 inch AMOLED, 120Hz, 2800 x 1260 pixel\n"
# # #         "Chip xử lý: MediaTek Dimensity 7200\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 8MP + 2MP\n"
# # #         "Pin: 4600mAh, sạc nhanh 66W",
        
# # #         "Màn hình: 6.78 inch AMOLED, 120Hz, 2800 x 1260 pixel\n"
# # #         "Chip xử lý: MediaTek Dimensity 9000\n"
# # #         "RAM: 12GB/16GB\n"
# # #         "Bộ nhớ trong: 256GB/512GB\n"
# # #         "Camera: 50MP + 50MP + 12MP\n"
# # #         "Pin: 4700mAh, sạc nhanh 80W",
        
# # #         "Màn hình: 6.55 inch IPS LCD, 60Hz, 1612 x 720 pixel\n"
# # #         "Chip xử lý: MediaTek Helio G85\n"
# # #         "RAM: 4GB/6GB\n"
# # #         "Bộ nhớ trong: 64GB/128GB\n"
# # #         "Camera: 50MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 18W",
        
# # #         "Màn hình: 6.78 inch AMOLED, 120Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: Snapdragon 870\n"
# # #         "RAM: 8GB/12GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 50MP + 8MP + 2MP\n"
# # #         "Pin: 4600mAh, sạc nhanh 66W",
        
# # #         "Màn hình: 6.38 inch AMOLED, 90Hz, 2400 x 1080 pixel\n"
# # #         "Chip xử lý: MediaTek Dimensity 900\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB/256GB\n"
# # #         "Camera: 64MP + 2MP + 2MP\n"
# # #         "Pin: 4500mAh, sạc nhanh 44W"
# # #     ],
# # #     'categories': ['Category/Vivo'] * 10  # Danh mục sản phẩm
# # # }

# # # # Tạo DataFrame
# # # df_vivo = pd.DataFrame(data)

# # # # Xuất DataFrame ra file CSV
# # # df_vivo.to_csv('/home/trancong/Downloads/vivo_products_specs.csv', index=False)

# # # # Hiển thị DataFrame
# # # print(df_vivo)

# # # import pandas as pd

# # # # Dữ liệu sản phẩm điện thoại Lenovo với thông số kỹ thuật chi tiết
# # # data = {
# # #     'sku': ['LENOVO-K12', 'LENOVO-K12-PRO', 'LENOVO-LEGION-DUEL', 'LENOVO-LEGION-DUEL-2', 
# # #             'LENOVO-A7', 'LENOVO-A8', 'LENOVO-Z5', 'LENOVO-Z6', 'LENOVO-P2', 'LENOVO-K13-NOTE'],
# # #     'attribute_set_code': ['Default'] * 10,
# # #     'product_type': ['simple'] * 10,
# # #     'visibility': ['Catalog, Search'] * 10,
# # #     'name': ['Lenovo K12', 'Lenovo K12 Pro', 'Lenovo Legion Duel', 'Lenovo Legion Duel 2', 
# # #              'Lenovo A7', 'Lenovo A8', 'Lenovo Z5', 'Lenovo Z6', 'Lenovo P2', 'Lenovo K13 Note'],
# # #     'price': [2990000, 4290000, 13990000, 15990000, 1990000, 
# # #               2590000, 7490000, 9990000, 5990000, 3290000],
# # #     'quantity': [30] * 10,  # Số lượng tồn kho
# # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # #     'description': [
# # #         "Màn hình: 6.5 inch IPS, HD+ (720 x 1600 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 460\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 48MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 10W",
        
# # #         "Màn hình: 6.8 inch IPS, HD+ (720 x 1640 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 662\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 64MP + 2MP + 2MP\n"
# # #         "Pin: 6000mAh, sạc nhanh 20W",
        
# # #         "Màn hình: 6.65 inch AMOLED, Full HD+ (1080 x 2340 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 865+\n"
# # #         "RAM: 12GB\n"
# # #         "Bộ nhớ trong: 256GB\n"
# # #         "Camera sau: 64MP + 16MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 90W",
        
# # #         "Màn hình: 6.92 inch AMOLED, Full HD+ (1080 x 2460 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 888\n"
# # #         "RAM: 16GB\n"
# # #         "Bộ nhớ trong: 512GB\n"
# # #         "Camera sau: 64MP + 16MP\n"
# # #         "Pin: 5500mAh, sạc nhanh 90W",
        
# # #         "Màn hình: 6.09 inch IPS, HD+ (720 x 1560 pixel)\n"
# # #         "Chip xử lý: Unisoc SC9863A\n"
# # #         "RAM: 2GB\n"
# # #         "Bộ nhớ trong: 32GB\n"
# # #         "Camera sau: 13MP + 2MP\n"
# # #         "Pin: 4000mAh, sạc thường 10W",
        
# # #         "Màn hình: 6.22 inch IPS, HD+ (720 x 1520 pixel)\n"
# # #         "Chip xử lý: MediaTek Helio P22\n"
# # #         "RAM: 3GB\n"
# # #         "Bộ nhớ trong: 32GB\n"
# # #         "Camera sau: 13MP + 5MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 15W",
        
# # #         "Màn hình: 6.2 inch IPS, Full HD+ (1080 x 2246 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 636\n"
# # #         "RAM: 6GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 16MP + 8MP\n"
# # #         "Pin: 3300mAh, sạc nhanh 18W",
        
# # #         "Màn hình: 6.39 inch AMOLED, Full HD+ (1080 x 2340 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 730\n"
# # #         "RAM: 6GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 24MP + 8MP + 5MP\n"
# # #         "Pin: 4000mAh, sạc nhanh 18W",
        
# # #         "Màn hình: 5.5 inch AMOLED, Full HD (1080 x 1920 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 625\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 13MP\n"
# # #         "Pin: 5100mAh, sạc nhanh 24W",
        
# # #         "Màn hình: 6.5 inch IPS, HD+ (720 x 1600 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 460\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 48MP + 2MP + 2MP\n"
# # #         "Pin: 5000mAh, sạc nhanh 10W"
# # #     ],
# # #     'categories': ['Category/Lenovo'] * 10  # Danh mục sản phẩm
# # # }

# # # # Tạo DataFrame
# # # df_lenovo = pd.DataFrame(data)

# # # # Xuất DataFrame ra file CSV
# # # df_lenovo.to_csv('/home/trancong/Downloads/lenovo_smartphones.csv', index=False)

# # # # Hiển thị DataFrame
# # # print(df_lenovo)

# # # import pandas as pd

# # # # Dữ liệu sản phẩm điện thoại Sony với thông số kỹ thuật chi tiết
# # # data = {
# # #     'sku': ['SONY-XPERIA-1-II', 'SONY-XPERIA-5-II', 'SONY-XPERIA-10-II', 'SONY-XPERIA-1-III', 
# # #             'SONY-XPERIA-5-III', 'SONY-XPERIA-10-III', 'SONY-XPERIA-ACE-II', 'SONY-XPERIA-L4', 
# # #             'SONY-XPERIA-8-LITE', 'SONY-XPERIA-10-LITE'],
# # #     'attribute_set_code': ['Default'] * 10,
# # #     'product_type': ['simple'] * 10,
# # #     'visibility': ['Catalog, Search'] * 10,
# # #     'name': ['Sony Xperia 1 II', 'Sony Xperia 5 II', 'Sony Xperia 10 II', 'Sony Xperia 1 III', 
# # #              'Sony Xperia 5 III', 'Sony Xperia 10 III', 'Sony Xperia Ace II', 'Sony Xperia L4', 
# # #              'Sony Xperia 8 Lite', 'Sony Xperia 10 Lite'],
# # #     'price': [24990000, 19990000, 10990000, 27990000, 22990000, 
# # #               11990000, 5990000, 4990000, 7990000, 8990000],
# # #     'quantity': [20] * 10,  # Số lượng tồn kho
# # #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# # #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# # #     'description': [
# # #         "Màn hình: 6.5 inch OLED, 4K HDR\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 865\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 256GB\n"
# # #         "Camera sau: 12MP + 12MP + 12MP\n"
# # #         "Pin: 4000mAh, sạc nhanh 21W",
        
# # #         "Màn hình: 6.1 inch OLED, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 865\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 12MP + 12MP + 12MP\n"
# # #         "Pin: 4000mAh, sạc nhanh 21W",
        
# # #         "Màn hình: 6.0 inch OLED, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 665\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 12MP + 8MP + 8MP\n"
# # #         "Pin: 3600mAh, sạc thường 18W",
        
# # #         "Màn hình: 6.5 inch OLED, 4K HDR\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 888\n"
# # #         "RAM: 12GB\n"
# # #         "Bộ nhớ trong: 256GB\n"
# # #         "Camera sau: 12MP + 12MP + 12MP + 3D iToF\n"
# # #         "Pin: 4500mAh, sạc nhanh 30W",
        
# # #         "Màn hình: 6.1 inch OLED, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 888\n"
# # #         "RAM: 8GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 12MP + 12MP + 12MP\n"
# # #         "Pin: 4500mAh, sạc nhanh 30W",
        
# # #         "Màn hình: 6.0 inch OLED, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 690\n"
# # #         "RAM: 6GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 12MP + 8MP + 8MP\n"
# # #         "Pin: 4500mAh, sạc nhanh 18W",
        
# # #         "Màn hình: 5.5 inch IPS, HD+ (720 x 1496 pixel)\n"
# # #         "Chip xử lý: MediaTek Helio P35\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 13MP\n"
# # #         "Pin: 4500mAh, sạc thường 10W",
        
# # #         "Màn hình: 6.2 inch IPS, HD+ (720 x 1680 pixel)\n"
# # #         "Chip xử lý: MediaTek Helio P22\n"
# # #         "RAM: 3GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 13MP + 5MP + 2MP\n"
# # #         "Pin: 3580mAh, sạc nhanh 18W",
        
# # #         "Màn hình: 6.0 inch IPS, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 630\n"
# # #         "RAM: 4GB\n"
# # #         "Bộ nhớ trong: 64GB\n"
# # #         "Camera sau: 12MP + 8MP\n"
# # #         "Pin: 2870mAh, sạc thường 18W",

# # #         "Màn hình: 6.0 inch OLED, Full HD+ (1080 x 2520 pixel)\n"
# # #         "Chip xử lý: Qualcomm Snapdragon 765\n"
# # #         "RAM: 6GB\n"
# # #         "Bộ nhớ trong: 128GB\n"
# # #         "Camera sau: 12MP + 8MP\n"
# # #         "Pin: 4000mAh, sạc nhanh 20W"
# # #     ],
# # #     'categories': ['Category/Sony'] * 10  # Danh mục sản phẩm
# # # }

# # # # Tạo DataFrame
# # # df_sony = pd.DataFrame(data)

# # # # Xuất DataFrame ra file CSV
# # # df_sony.to_csv('/home/trancong/Downloads/sony_smartphones.csv', index=False)

# # # # Hiển thị DataFrame
# # # print(df_sony)
# # import pandas as pd

# # # Dữ liệu sản phẩm điện thoại Realme với thông số kỹ thuật chi tiết
# # data = {
# #     'sku': ['REALME-C11', 'REALME-C21Y', 'REALME-7-PRO', 'REALME-8', 'REALME-8-PRO', 
# #             'REALME-X3-SUPERZOOM', 'REALME-NARZO-30A', 'REALME-GT-MASTER', 
# #             'REALME-GT-NEO2', 'REALME-GT2'],
# #     'attribute_set_code': ['Default'] * 10,
# #     'product_type': ['simple'] * 10,
# #     'visibility': ['Catalog, Search'] * 10,
# #     'name': ['Realme C11', 'Realme C21Y', 'Realme 7 Pro', 'Realme 8', 'Realme 8 Pro',
# #              'Realme X3 SuperZoom', 'Realme Narzo 30A', 'Realme GT Master', 
# #              'Realme GT Neo2', 'Realme GT2'],
# #     'price': [2490000, 3290000, 7490000, 5990000, 8990000, 
# #               10990000, 3690000, 8490000, 12990000, 13990000],
# #     'quantity': [25] * 10,  # Số lượng tồn kho
# #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# #     'description': [
# #         "Màn hình: 6.5 inch IPS LCD, HD+ (720 x 1600 pixel)\n"
# #         "Chip xử lý: MediaTek Helio G35\n"
# #         "RAM: 2GB\n"
# #         "Bộ nhớ trong: 32GB\n"
# #         "Camera sau: 13MP + 2MP\n"
# #         "Pin: 5000mAh, sạc thường 10W",

# #         "Màn hình: 6.5 inch IPS LCD, HD+ (720 x 1600 pixel)\n"
# #         "Chip xử lý: Unisoc T610\n"
# #         "RAM: 4GB\n"
# #         "Bộ nhớ trong: 64GB\n"
# #         "Camera sau: 13MP + 2MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.4 inch Super AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 720G\n"
# #         "RAM: 8GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 64MP + 8MP + 2MP + 2MP\n"
# #         "Pin: 4500mAh, sạc nhanh 65W",

# #         "Màn hình: 6.4 inch AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: MediaTek Helio G95\n"
# #         "RAM: 6GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 64MP + 8MP + 2MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 30W",

# #         "Màn hình: 6.4 inch Super AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 720G\n"
# #         "RAM: 8GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 108MP + 8MP + 2MP + 2MP\n"
# #         "Pin: 4500mAh, sạc nhanh 50W",

# #         "Màn hình: 6.6 inch IPS LCD, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 855+\n"
# #         "RAM: 12GB\n"
# #         "Bộ nhớ trong: 256GB\n"
# #         "Camera sau: 64MP + 8MP + 8MP + 2MP\n"
# #         "Pin: 4200mAh, sạc nhanh 30W",

# #         "Màn hình: 6.5 inch IPS LCD, HD+ (720 x 1600 pixel)\n"
# #         "Chip xử lý: MediaTek Helio G85\n"
# #         "RAM: 3GB\n"
# #         "Bộ nhớ trong: 32GB\n"
# #         "Camera sau: 13MP + 2MP\n"
# #         "Pin: 6000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.43 inch Super AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 778G\n"
# #         "RAM: 8GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 64MP + 8MP + 2MP\n"
# #         "Pin: 4300mAh, sạc nhanh 65W",

# #         "Màn hình: 6.62 inch AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 870\n"
# #         "RAM: 12GB\n"
# #         "Bộ nhớ trong: 256GB\n"
# #         "Camera sau: 64MP + 8MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 65W",

# #         "Màn hình: 6.62 inch AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 888\n"
# #         "RAM: 12GB\n"
# #         "Bộ nhớ trong: 256GB\n"
# #         "Camera sau: 50MP + 8MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 65W"
# #     ],
# #     'categories': ['Category/Realme'] * 10  # Danh mục sản phẩm
# # }

# # # Tạo DataFrame
# # df_realme = pd.DataFrame(data)

# # # Xuất DataFrame ra file CSV
# # df_realme.to_csv('/home/trancong/Downloads/realme_smartphones.csv', index=False)

# # # Hiển thị DataFrame
# # print(df_realme)

# # import pandas as pd

# # # Dữ liệu sản phẩm điện thoại Vsmart với thông số kỹ thuật chi tiết
# # data = {
# #     'sku': ['VSMART-JOY4', 'VSMART-STAR5', 'VSMART-ARIS', 'VSMART-LIVE4', 
# #             'VSMART-ARIS-PRO', 'VSMART-BEE3', 'VSMART-STAR4', 'VSMART-JOY3',
# #             'VSMART-ACTIVE3', 'VSMART-LUX'],
# #     'attribute_set_code': ['Default'] * 10,
# #     'product_type': ['simple'] * 10,
# #     'visibility': ['Catalog, Search'] * 10,
# #     'name': ['Vsmart Joy 4', 'Vsmart Star 5', 'Vsmart Aris', 'Vsmart Live 4', 
# #              'Vsmart Aris Pro', 'Vsmart Bee 3', 'Vsmart Star 4', 'Vsmart Joy 3',
# #              'Vsmart Active 3', 'Vsmart Lux'],
# #     'price': [3290000, 2690000, 7490000, 4590000, 8990000, 
# #               1990000, 2390000, 2990000, 3590000, 9990000],
# #     'quantity': [30] * 10,  # Số lượng tồn kho
# #     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
# #     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
# #     'description': [
# #         "Màn hình: 6.53 inch IPS LCD, Full HD+ (1080 x 2340 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 665\n"
# #         "RAM: 4GB\n"
# #         "Bộ nhớ trong: 64GB\n"
# #         "Camera sau: 16MP + 8MP + 2MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.52 inch IPS LCD, HD+ (720 x 1600 pixel)\n"
# #         "Chip xử lý: MediaTek Helio G35\n"
# #         "RAM: 3GB\n"
# #         "Bộ nhớ trong: 32GB\n"
# #         "Camera sau: 13MP + 2MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.39 inch AMOLED, Full HD+ (1080 x 2340 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 730\n"
# #         "RAM: 6GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 64MP + 8MP + 8MP\n"
# #         "Pin: 4000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.5 inch IPS LCD, Full HD+ (1080 x 2340 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 675\n"
# #         "RAM: 6GB\n"
# #         "Bộ nhớ trong: 64GB\n"
# #         "Camera sau: 48MP + 8MP + 5MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.39 inch AMOLED, Full HD+ (1080 x 2340 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 730\n"
# #         "RAM: 8GB\n"
# #         "Bộ nhớ trong: 128GB\n"
# #         "Camera sau: 64MP + 8MP + 8MP\n"
# #         "Pin: 4000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.0 inch IPS LCD, HD+ (720 x 1440 pixel)\n"
# #         "Chip xử lý: MediaTek MT6739\n"
# #         "RAM: 2GB\n"
# #         "Bộ nhớ trong: 16GB\n"
# #         "Camera sau: 8MP\n"
# #         "Pin: 3000mAh, sạc thường 10W",

# #         "Màn hình: 6.09 inch IPS LCD, HD+ (720 x 1560 pixel)\n"
# #         "Chip xử lý: MediaTek Helio P22\n"
# #         "RAM: 2GB\n"
# #         "Bộ nhớ trong: 16GB\n"
# #         "Camera sau: 8MP + 2MP\n"
# #         "Pin: 3500mAh, sạc thường 10W",

# #         "Màn hình: 6.5 inch IPS LCD, HD+ (720 x 1560 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 632\n"
# #         "RAM: 4GB\n"
# #         "Bộ nhớ trong: 64GB\n"
# #         "Camera sau: 13MP + 8MP + 2MP\n"
# #         "Pin: 5000mAh, sạc nhanh 18W",

# #         "Màn hình: 6.39 inch AMOLED, Full HD+ (1080 x 2340 pixel)\n"
# #         "Chip xử lý: MediaTek Helio P60\n"
# #         "RAM: 6GB\n"
# #         "Bộ nhớ trong: 64GB\n"
# #         "Camera sau: 48MP + 8MP + 2MP\n"
# #         "Pin: 4020mAh, sạc nhanh 18W",

# #         "Màn hình: 6.67 inch AMOLED, Full HD+ (1080 x 2400 pixel)\n"
# #         "Chip xử lý: Qualcomm Snapdragon 870\n"
# #         "RAM: 12GB\n"
# #         "Bộ nhớ trong: 256GB\n"
# #         "Camera sau: 64MP + 13MP + 5MP\n"
# #         "Pin: 4500mAh, sạc nhanh 33W"
# #     ],
# #     'categories': ['Category/Vsmart'] * 10  # Danh mục sản phẩm
# # }

# # # Tạo DataFrame
# # df_vsmart = pd.DataFrame(data)

# # # Xuất DataFrame ra file CSV
# # df_vsmart.to_csv('/home/trancong/Downloads/vsmart_smartphones.csv', index=False)

# # # Hiển thị DataFrame
# # print(df_vsmart)
# import pandas as pd

# # Dữ liệu sản phẩm điện thoại Huawei với thông số kỹ thuật chi tiết
# data = {
#     'sku': ['HUAWEI-P40', 'HUAWEI-P30', 'HUAWEI-NOVA7', 'HUAWEI-MATE40', 
#             'HUAWEI-Y9A', 'HUAWEI-Y7A', 'HUAWEI-P40-PRO', 'HUAWEI-NOVA9',
#             'HUAWEI-MATE30', 'HUAWEI-Y6P'],
#     'attribute_set_code': ['Default'] * 10,
#     'product_type': ['simple'] * 10,
#     'visibility': ['Catalog, Search'] * 10,
#     'name': ['Huawei P40', 'Huawei P30', 'Huawei Nova 7', 'Huawei Mate 40', 
#              'Huawei Y9a', 'Huawei Y7a', 'Huawei P40 Pro', 'Huawei Nova 9',
#              'Huawei Mate 30', 'Huawei Y6p'],
#     'price': [16990000, 13990000, 10990000, 23990000, 5990000, 
#               4690000, 22990000, 11990000, 18990000, 3290000],
#     'quantity': [25] * 10,  # Số lượng tồn kho
#     'stock_status': ['In Stock'] * 10,  # Trạng thái kho
#     'status': ['Enabled'] * 10,  # Trạng thái sản phẩm
#     'description': [
#         "Màn hình: 6.1 inch OLED, Full HD+ (1080 x 2340 pixel)\n"
#         "Chip xử lý: Kirin 990 5G\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 50MP + 16MP + 8MP\n"
#         "Pin: 3800mAh, sạc nhanh 22.5W",

#         "Màn hình: 6.1 inch OLED, Full HD+ (1080 x 2340 pixel)\n"
#         "Chip xử lý: Kirin 980\n"
#         "RAM: 6GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 40MP + 16MP + 8MP\n"
#         "Pin: 3650mAh, sạc nhanh 22.5W",

#         "Màn hình: 6.53 inch OLED, Full HD+ (1080 x 2400 pixel)\n"
#         "Chip xử lý: Kirin 985 5G\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 64MP + 8MP + 8MP + 2MP\n"
#         "Pin: 4000mAh, sạc nhanh 40W",

#         "Màn hình: 6.76 inch OLED, Full HD+ (1344 x 2772 pixel)\n"
#         "Chip xử lý: Kirin 9000 5G\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 256GB\n"
#         "Camera sau: 50MP + 20MP + 12MP\n"
#         "Pin: 4400mAh, sạc nhanh 66W",

#         "Màn hình: 6.63 inch IPS LCD, Full HD+ (1080 x 2400 pixel)\n"
#         "Chip xử lý: MediaTek Helio G80\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 64MP + 8MP + 2MP + 2MP\n"
#         "Pin: 4300mAh, sạc nhanh 22.5W",

#         "Màn hình: 6.67 inch IPS LCD, Full HD+ (1080 x 2400 pixel)\n"
#         "Chip xử lý: Kirin 710A\n"
#         "RAM: 4GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 48MP + 8MP + 2MP\n"
#         "Pin: 5000mAh, sạc nhanh 22.5W",

#         "Màn hình: 6.58 inch OLED, Full HD+ (1200 x 2640 pixel)\n"
#         "Chip xử lý: Kirin 990 5G\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 256GB\n"
#         "Camera sau: 50MP + 40MP + 12MP + TOF 3D\n"
#         "Pin: 4200mAh, sạc nhanh 40W",

#         "Màn hình: 6.57 inch OLED, Full HD+ (1080 x 2340 pixel)\n"
#         "Chip xử lý: Qualcomm Snapdragon 778G\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 128GB\n"
#         "Camera sau: 50MP + 8MP + 2MP + 2MP\n"
#         "Pin: 4300mAh, sạc nhanh 66W",

#         "Màn hình: 6.62 inch OLED, Full HD+ (1080 x 2340 pixel)\n"
#         "Chip xử lý: Kirin 990\n"
#         "RAM: 8GB\n"
#         "Bộ nhớ trong: 256GB\n"
#         "Camera sau: 40MP + 16MP + 8MP\n"
#         "Pin: 4200mAh, sạc nhanh 40W",

#         "Màn hình: 6.3 inch IPS LCD, HD+ (720 x 1600 pixel)\n"
#         "Chip xử lý: MediaTek Helio P22\n"
#         "RAM: 3GB\n"
#         "Bộ nhớ trong: 64GB\n"
#         "Camera sau: 13MP + 5MP + 2MP\n"
#         "Pin: 5000mAh, sạc thường 10W"
#     ],
#     'categories': ['Category/Huawei'] * 10  # Danh mục sản phẩm
# }

# # Tạo DataFrame
# df_huawei = pd.DataFrame(data)

# # Xuất DataFrame ra file CSV
# df_huawei.to_csv('/home/trancong/Downloads/huawei_smartphones.csv', index=False)

# # Hiển thị DataFrame
# print(df_huawei)


